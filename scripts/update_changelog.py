#!/usr/bin/env python3
"""
Regenerates CHANGELOG.md from git history, grouped by day, and refreshes
the "Recent Changes" section in README.md.

Can be run:
  - standalone, any time, to rebuild the full changelog from git log
  - from the post-commit hook (see .githooks/post-commit), to update it
    automatically after every commit
  - from CI (see .github/workflows/changelog.yml), to catch commits made
    outside your local machine (e.g. edited on github.com)
"""
import re
import subprocess
from collections import OrderedDict
from pathlib import Path

REPO_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
)
CHANGELOG_PATH = REPO_ROOT / "CHANGELOG.md"
README_PATH = REPO_ROOT / "README.md"
RECENT_DAYS_IN_README = 3  # how many days of history to mirror into README.md

MARKER_START = "<!-- CHANGELOG:START -->"
MARKER_END = "<!-- CHANGELOG:END -->"


def get_commits():
    """Return (date, short_hash, message) tuples, newest first."""
    log = subprocess.check_output(
        ["git", "log", "--date=short", "--pretty=format:%ad|%h|%s"],
        text=True,
    )
    commits = []
    for line in log.splitlines():
        if not line.strip():
            continue
        date, short_hash, message = line.split("|", 2)
        commits.append((date, short_hash, message))
    return commits


def group_by_day(commits):
    grouped = OrderedDict()
    for date, short_hash, message in commits:
        grouped.setdefault(date, []).append((short_hash, message))
    return grouped


def build_changelog_text(grouped):
    lines = ["# Changelog", "", "_Grouped by day, generated from git history._", ""]
    for date, entries in grouped.items():
        lines.append(f"## {date}")
        for short_hash, message in entries:
            lines.append(f"- `{short_hash}` {message}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_recent_block(grouped):
    lines = []
    for date, entries in list(grouped.items())[:RECENT_DAYS_IN_README]:
        lines.append(f"**{date}**")
        for short_hash, message in entries:
            lines.append(f"- `{short_hash}` {message}")
        lines.append("")
    return "\n".join(lines).rstrip()


def update_readme(grouped):
    if not README_PATH.exists():
        return

    readme = README_PATH.read_text()
    recent_block = build_recent_block(grouped)

    if MARKER_START in readme and MARKER_END in readme:
        pattern = re.compile(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.DOTALL
        )
        replacement = f"{MARKER_START}\n{recent_block}\n{MARKER_END}"
        readme = pattern.sub(replacement, readme)
    else:
        readme = (
            readme.rstrip()
            + f"\n\n## Recent Changes\n\n{MARKER_START}\n{recent_block}\n{MARKER_END}\n"
        )

    README_PATH.write_text(readme)


def main():
    commits = get_commits()
    if not commits:
        return
    grouped = group_by_day(commits)
    CHANGELOG_PATH.write_text(build_changelog_text(grouped))
    update_readme(grouped)


if __name__ == "__main__":
    main()
