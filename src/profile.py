import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv")

# Example: distribution of usage value
plt.figure()
df["value"].hist(bins=30)
plt.title("Distribution of usage values")
plt.xlabel("value")
plt.ylabel("count")
plt.tight_layout()
plt.savefig("notebooks/value_distribution.png")

# NOTE: "geography" is a category label (global / country / state_us),
# not an actual place. The real country/state codes live in "geo_id".
# Grouping by "geography" directly collapses everything into 3 bars,
# which is why the old top_geography.png chart was unreliable.

# Top 15 countries by total usage (geography == "country")
country_df = df[(df["geography"] == "country") & (df["facet"] == "country") & (df["variable"] == "usage_count")]
top_country = (
    country_df.groupby("geo_id")["value"].sum().sort_values(ascending=False).head(15)
)
plt.figure()
top_country.plot(kind="bar")
plt.title("Top 15 countries by total usage value")
plt.xlabel("country (ISO code)")
plt.ylabel("total value")
plt.tight_layout()
plt.savefig("notebooks/top_country.png")

# Top 15 US states by total usage (geography == "state_us")
state_df = df[(df["geography"] == "state_us") & (df["facet"] == "state_us") & (df["variable"] == "usage_count")]
top_state = (
    state_df.groupby("geo_id")["value"].sum().sort_values(ascending=False).head(15)
)
plt.figure()
top_state.plot(kind="bar")
plt.title("Top 15 US states by total usage value")
plt.xlabel("state code")
plt.ylabel("total value")
plt.tight_layout()
plt.savefig("notebooks/top_state_us.png")