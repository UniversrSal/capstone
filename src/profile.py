import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv")

# Example: distribution of usage value
plt.figure()
df["value"].hist(bins=30)
plt.title("Distribution of usage values")
plt.xlabel("value")
plt.ylabel("count")
plt.savefig("notebooks/value_distribution.png")

# Example: top geographies by total usage
top_geo = df.groupby("geography")["value"].sum().sort_values(ascending=False).head(15)
plt.figure()
top_geo.plot(kind="bar")
plt.title("Top 15 geographies by total usage value")
plt.tight_layout()
plt.savefig("notebooks/top_geography.png")