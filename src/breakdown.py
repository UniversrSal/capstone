import pandas as pd

# Load the raw usage data and the two lookup tables
df = pd.read_csv("data/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv")
iso = pd.read_csv("data/iso_country_codes.csv")
states = pd.read_csv("data/working_age_pop_2024_us_state.csv")

# --- All countries ---
country_df = df[df["geography"] == "country"]
country_totals = (
    country_df.groupby("geo_id")["value"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
country_totals.columns = ["geo_id", "total_value"]

# Map ISO alpha-2 codes to full country names
country_totals = country_totals.merge(
    iso[["iso_alpha_2", "country_name"]],
    left_on="geo_id",
    right_on="iso_alpha_2",
    how="left",
)
country_totals["country_name"] = country_totals["country_name"].fillna("Not classified")
country_totals = country_totals[["geo_id", "country_name", "total_value"]]

country_totals.to_csv("notebooks/all_countries.csv", index=False)
print(f"Countries: {len(country_totals)} rows")

# --- All US states ---
state_df = df[df["geography"] == "state_us"]
state_totals = (
    state_df.groupby("geo_id")["value"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
state_totals.columns = ["geo_id", "total_value"]

# Map state codes to full state names
state_totals = state_totals.merge(
    states[["state_code", "state"]],
    left_on="geo_id",
    right_on="state_code",
    how="left",
)
state_totals = state_totals[["geo_id", "state", "total_value"]]

state_totals.to_csv("notebooks/all_states.csv", index=False)
print(f"States: {len(state_totals)} rows")