"""Compare 2024 GDP and private AI investment for the dataset's top five.

Run from the project root: python src/gdp_ai_visualization.py
Requires pandas and matplotlib. All inputs are local CSVs; no network needed.
Investment: Stanford HAI, 2025 AI Index, Figure 4.3.8 (Quid, 2024).
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


ROOT = Path(__file__).resolve().parent
if ROOT.name == "src":
    ROOT = ROOT.parent
COLORS = ["#168A86", "#3976BF", "#8C62AE", "#D99A24", "#D85D60"]
INK = "#172D40"
MUTED = "#526575"


def load_comparison_data(data_dir=None, year=2024):
    """Rank GDP before joining investment; never drop missing top-five entries."""
    data_dir = Path(data_dir) if data_dir is not None else ROOT / "data"
    gdp = pd.read_csv(data_dir / "gdp_2024_country.csv")
    iso = pd.read_csv(data_dir / "iso_country_codes.csv", keep_default_na=False)
    investment = pd.read_csv(data_dir / "ai_private_investment_2024_country.csv")
    gdp = gdp.loc[gdp["year"].eq(year)].copy()
    investment = investment.loc[investment["year"].eq(year)].copy()
    for frame, value_col in [(gdp, "gdp_total"), (investment, "ai_investment_usd")]:
        frame[value_col] = pd.to_numeric(frame[value_col], errors="raise")
        if frame["iso_alpha_3"].duplicated().any():
            raise ValueError("Duplicate country entries for the selected year.")
        if frame[value_col].isna().any() or (frame[value_col] < 0).any():
            raise ValueError(f"Missing or negative values in {value_col}.")
    if len(gdp) < 5:
        raise ValueError("At least five GDP country records are required.")
    top = gdp.nlargest(5, "gdp_total").merge(
        iso[["iso_alpha_3", "country_name"]], on="iso_alpha_3", how="left",
        validate="one_to_one",
    ).merge(
        investment[["iso_alpha_3", "ai_investment_usd"]],
        on="iso_alpha_3", how="left", validate="one_to_one",
    )
    if top[["country_name", "ai_investment_usd"]].isna().any().any():
        raise ValueError("A GDP top-five country is missing a name or investment value.")
    total = top["ai_investment_usd"].sum()
    if total <= 0:
        raise ValueError("Investment total must be positive to create a pie chart.")
    top.insert(0, "gdp_rank_in_dataset", range(1, 6))
    top["gdp_trillions_usd"] = top["gdp_total"] / 1e12
    top["ai_investment_billions_usd"] = top["ai_investment_usd"] / 1e9
    top["ai_investment_share_pct"] = top["ai_investment_usd"] / total * 100
    return top


def draw_gdp(ax, data, year):
    ax.set_facecolor("white")
    bars = ax.barh(data["country_name"], data["gdp_trillions_usd"],
                   color=COLORS, height=0.60, zorder=3)
    ax.invert_yaxis()
    ax.set_xlim(0, data["gdp_trillions_usd"].max() * 1.17)
    ax.set_title(f"National economic output ({year})", loc="left",
                 fontsize=17, fontweight="bold", color=INK, pad=23)
    ax.set_xlabel("Nominal GDP · trillions of US dollars", color=MUTED, labelpad=13)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"${value:.0f}T"))
    ax.grid(axis="x", color="#E4EAF0", linewidth=0.8, zorder=0)
    ax.tick_params(axis="both", length=0, colors=INK, labelsize=12, pad=9)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for bar, value in zip(bars, data["gdp_trillions_usd"]):
        ax.text(value + 0.40, bar.get_y() + bar.get_height() / 2,
                f"${value:.2f}T", va="center", color=INK, fontsize=12,
                fontweight="bold")


def draw_investment(ax, data, year):
    ax.set_title(f"Private AI investment share ({year})", loc="left",
                 fontsize=17, fontweight="bold", color=INK, pad=23)
    wedges, _, labels = ax.pie(
        data["ai_investment_usd"], colors=COLORS, startangle=90,
        counterclock=False, radius=0.96,
        autopct=lambda pct: f"{pct:.1f}%" if pct >= 5 else "",
        pctdistance=0.62, wedgeprops={"edgecolor": "white", "linewidth": 1.2},
        textprops={"fontsize": 17, "color": "white", "fontweight": "bold"},
    )
    legend = [
        f"{row.country_name}   ${row.ai_investment_billions_usd:.2f}B · "
        f"{row.ai_investment_share_pct:.1f}%"
        for row in data.itertuples()
    ]
    ax.legend(wedges, legend, loc="upper center", bbox_to_anchor=(0.5, -0.02),
              frameon=False, fontsize=11, labelcolor=INK, handlelength=1.0,
              labelspacing=0.75)


def create_gdp_ai_comparison(data=None, data_dir=None, year=2024):
    """Return the combined bar and pie figure, using measured CSV values."""
    if data is None:
        data = load_comparison_data(data_dir, year)
    fig, (bar_ax, pie_ax) = plt.subplots(1, 2, figsize=(16, 8.5),
                                        gridspec_kw={"width_ratios": [1.15, 1]})
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.13, right=0.96, top=0.78, bottom=0.30, wspace=0.26)
    fig.text(0.055, 0.93, "Economic output & AI investment", color=INK,
             fontsize=26, fontweight="bold")
    fig.text(0.055, 0.88, f"Top 5 countries by {year} GDP in the capstone dataset",
             color=MUTED, fontsize=14)
    draw_gdp(bar_ax, data, year)
    draw_investment(pie_ax, data, year)
    total = data["ai_investment_billions_usd"].sum()
    fig.text(0.055, 0.11, f"Selected-country private AI investment total: ${total:.2f}B",
             color=INK, fontsize=12, fontweight="bold")
    fig.text(0.055, 0.069,
             "GDP: project gdp_2024_country.csv | AI investment: Stanford HAI, "
             "2025 AI Index, Fig. 4.3.8 (Quid, 2024).", color=MUTED, fontsize=10)
    return fig


def print_analysis_summary(data=None, data_dir=None, year=2024):
    if data is None:
        data = load_comparison_data(data_dir, year)
    columns = ["gdp_rank_in_dataset", "country_name", "gdp_trillions_usd",
               "ai_investment_billions_usd", "ai_investment_share_pct"]
    print(f"\n{year}: TOP FIVE GDP COUNTRIES IN THE DATASET")
    print(data[columns].to_string(index=False, float_format=lambda x: f"{x:.2f}"))
    print("\nPie denominator: private AI investment in these five countries only.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "notebooks")
    parser.add_argument("--year", type=int, default=2024)
    parser.add_argument("--show", action="store_true", help="Open the combined figure")
    args = parser.parse_args()
    data = load_comparison_data(args.data_dir, args.year)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    fig = create_gdp_ai_comparison(data, year=args.year)
    fig.savefig(args.output_dir / "gdp_ai_comparison.png", dpi=240)
    fig.savefig(args.output_dir / "gdp_ai_comparison.svg")
    for name, draw in [("economic_output_top5", draw_gdp),
                       ("ai_investment_top5", draw_investment)]:
        single, ax = plt.subplots(figsize=(10, 8), facecolor="white")
        single.subplots_adjust(left=0.21 if draw is draw_gdp else 0.08,
                               right=0.95, top=0.83, bottom=0.35)
        single.text(0.06, 0.94, "Top 5 GDP countries in the dataset", fontsize=19,
                    color=INK, fontweight="bold")
        draw(ax, data, args.year)
        single.text(0.06, 0.03, "Sources: project GDP CSV; Stanford HAI, 2025 "
                    "AI Index, Fig. 4.3.8 (Quid, 2024).", fontsize=10, color=MUTED)
        single.savefig(args.output_dir / f"{name}.png", dpi=240)
        plt.close(single)
    data.to_csv(args.output_dir / "top5_gdp_ai_comparison.csv", index=False)
    print_analysis_summary(data, year=args.year)
    print(f"\nCharts and summary saved to {args.output_dir.resolve()}")
    if args.show:
        plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
