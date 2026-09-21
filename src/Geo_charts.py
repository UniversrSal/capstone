import os
import pandas as pd
import plotly.express as px

DATA = "data/"
OUT = "notebooks/"
MIN_COUNTRY = 200
MIN_STATE = 100
os.makedirs(OUT, exist_ok=True)

raw = pd.read_csv(
    DATA + "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
    keep_default_na=False,
    na_values=[""],
)

iso = pd.read_csv(DATA + "iso_country_codes.csv", keep_default_na=False)
gdp_c = pd.read_csv(DATA + "gdp_2024_country.csv")
pop_c = pd.read_csv(DATA + "working_age_pop_2024_country.csv")
pop_c = pop_c[pop_c.year == 2024][["iso_alpha_3", "working_age_pop"]]

c = raw[(raw.geography == "country") & (raw.facet == "country") & (raw.variable == "usage_count")]
TOTAL_USAGE = c.value.sum()
WORLD_POP = pop_c.working_age_pop.sum()
c = c[["geo_id", "value"]].rename(columns={"geo_id": "iso_alpha_2", "value": "usage"})
c = c.merge(iso, on="iso_alpha_2")
c = c.merge(gdp_c[["iso_alpha_3", "gdp_total"]], on="iso_alpha_3")
c = c.merge(pop_c, on="iso_alpha_3")
c = c[c.usage >= MIN_COUNTRY]
c["aui"] = (c.usage / TOTAL_USAGE) / (c.working_age_pop / WORLD_POP)
c["gdp_per_worker"] = c.gdp_total / c.working_age_pop
c.sort_values("aui", ascending=False).to_csv(OUT + "country_aui.csv", index=False)

top = c.nlargest(20, "aui").sort_values("aui")
fig = px.bar(top, x="aui", y="country_name", orientation="h",
             title="Top 20 countries by AI usage index")
fig.write_image(OUT + "top_countries.png", width=1200, height=700, scale=2)

fig = px.scatter(c, x="gdp_per_worker", y="aui", hover_name="country_name",
                 log_x=True, log_y=True, trendline="ols",
                 trendline_options=dict(log_x=True, log_y=True),
                 title="AI usage index vs GDP per working-age person")
fig.write_image(OUT + "gdp_vs_usage.png", width=1200, height=700, scale=2)

fig = px.choropleth(c, locations="iso_alpha_3", color="aui", hover_name="country_name",
                    color_continuous_scale="Viridis", title="AI usage index by country")
fig.write_image(OUT + "world_map.png", width=1200, height=700, scale=2)

gdp_s = pd.read_csv(DATA + "gdp_2024_us_state.csv")
pop_s = pd.read_csv(DATA + "working_age_pop_2024_us_state.csv")

s = raw[(raw.geography == "state_us") & (raw.facet == "state_us") & (raw.variable == "usage_count")]
s = s[["geo_id", "value"]].rename(columns={"geo_id": "state_code", "value": "usage"})
s = s.merge(pop_s[["state_code", "state", "working_age_pop"]], on="state_code")
s = s.merge(gdp_s[["state_code", "gdp_millions"]], on="state_code")
s = s[s.usage >= MIN_STATE]
s["aui"] = (s.usage / s.usage.sum()) / (s.working_age_pop / s.working_age_pop.sum())
s["gdp_per_worker"] = s.gdp_millions * 1e6 / s.working_age_pop
s.sort_values("aui", ascending=False).to_csv(OUT + "state_aui.csv", index=False)

fig = px.choropleth(s, locations="state_code", locationmode="USA-states", scope="usa",
                    color="aui", hover_name="state",
                    color_continuous_scale="Viridis", title="AI usage index by US state")
fig.write_image(OUT + "us_states.png", width=1200, height=700, scale=2)