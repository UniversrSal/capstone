**Dataset Provenance**



**Source Anthropic Economic Index (Hugging Face)**

**Release** release\_2025\_09\_15

**URL** https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main/release\_2025\_09\_15/data/intermediate

**Download Date:** September 13, 2026,

**License** Mit

**Citation**  Handa et al. (2025), arXiv 2503.04761



**Files Used**



|aei\_raw\_1p\_api\_2025-08-04\_to\_2025-08-11.csv|7.03mb|Enterprise AI usage|
|-|-|-|
|<br />aei\_raw\_claude\_ai\_2025-08-04\_to\_2025-08-11.csv<br />|18.9mb|Consumer Claude.ai Usage data|
|gdp\_2024\_country.csv<br />|4.12mb|GOP by country, 2024|
|gdp\_2024\_us\_state.csv<br />|2.18kb|GOP by U.S State, 2024|
|iso\_country\_codes.csv<br />|4.56mb|Country code lookup for joins|
|iso\_country\_codes.csv<br />|3.65mb|O\*NET task definitions|
|soc\_structure.csv<br />|78.8kb|Standard Occupational Classifications hierarchy|
|working\_age\_pop\_2024\_us\_state.csv<br />|1.08kb|Working-age population by state|





**Inventory Output**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**



**$ python src/inventory.py**

**============================================================**

File: aei\_raw\_1p\_api\_2025-08-04\_to\_2025-08-11.csv

&#x20;Size: 7.027 MB

&#x20;Rows: 33794

&#x20;Columns: 10

&#x20;Column names/types:

&#x20;- geo\_id: str

&#x20;- geography: str

&#x20;- date\_start: str

&#x20;- date\_end: str

&#x20;- platform\_and\_product: str

&#x20;- facet: str

&#x20;- level: int64

&#x20;- variable: str

&#x20;- cluster\_name: str

&#x20;- value: float64

&#x20;Missing value rate per column:

&#x20;- geo\_id: 0.0

&#x20;- geography: 0.0

&#x20;- date\_start: 0.0

&#x20;- date\_end: 0.0

&#x20;- platform\_and\_product: 0.0

&#x20;- facet: 0.0

&#x20;- level: 0.0

&#x20;- variable: 0.0

&#x20;- cluster\_name: 0.0

&#x20;- value: 0.0

============================================================

File: aei\_raw\_claude\_ai\_2025-08-04\_to\_2025-08-11.csv

&#x20;Size: 18.895 MB

&#x20;Rows: 100062

&#x20;Columns: 10

&#x20;Column names/types:

&#x20;- geo\_id: str

&#x20;- geography: str

&#x20;- date\_start: str

&#x20;- date\_end: str

&#x20;- platform\_and\_product: str

&#x20;- facet: str

&#x20;- level: int64

&#x20;- variable: str

&#x20;- cluster\_name: str

&#x20;- value: float64

&#x20;Missing value rate per column:

&#x20;- geo\_id: 0.0002

&#x20;- geography: 0.0

&#x20;- date\_start: 0.0

&#x20;- date\_end: 0.0

&#x20;- platform\_and\_product: 0.0

&#x20;- facet: 0.0

&#x20;- level: 0.0

&#x20;- variable: 0.0

&#x20;- cluster\_name: 0.0045

&#x20;- value: 0.0

============================================================

File: gdp\_2024\_us\_state.csv

&#x20;Size: 0.002 MB

&#x20;Rows: 51

&#x20;Columns: 5

&#x20;Column names/types:

&#x20;- state\_code: str

&#x20;- state\_name: str

&#x20;- gdp\_total: float64

&#x20;- gdp\_millions: float64

&#x20;- year: int64

&#x20;Missing value rate per column:

&#x20;- state\_code: 0.0

&#x20;- state\_name: 0.0

&#x20;- gdp\_total: 0.0

&#x20;- gdp\_millions: 0.0

&#x20;- year: 0.0

============================================================

File: gdp\_2024\_country.csv

&#x20;Size: 0.004 MB

&#x20;Rows: 174

&#x20;Columns: 3

&#x20;Column names/types:

&#x20;- iso\_alpha\_3: str

&#x20;- gdp\_total: float64

&#x20;- year: int64

&#x20;Missing value rate per column:

&#x20;- iso\_alpha\_3: 0.0

&#x20;- gdp\_total: 0.0

&#x20;- year: 0.0

============================================================

File: working\_age\_pop\_2024\_us\_state.csv

&#x20;Size: 0.001 MB

&#x20;Rows: 51

&#x20;Columns: 3

&#x20;Column names/types:

&#x20;- state: str

&#x20;- working\_age\_pop: int64

&#x20;- state\_code: str

&#x20;Missing value rate per column:

&#x20;- state: 0.0

&#x20;- working\_age\_pop: 0.0

&#x20;- state\_code: 0.0

============================================================

File: working\_age\_pop\_2024\_country.csv

&#x20;Size: 0.006 MB

&#x20;Rows: 194

&#x20;Columns: 5

&#x20;Column names/types:

&#x20;- iso\_alpha\_3: str

&#x20;- year: int64

&#x20;- working\_age\_pop: float64

&#x20;- country\_code: str

&#x20;- country\_name: str

&#x20;Missing value rate per column:

&#x20;- iso\_alpha\_3: 0.0

&#x20;- year: 0.0

&#x20;- working\_age\_pop: 0.0

&#x20;- country\_code: 0.0052

&#x20;- country\_name: 0.0

============================================================

File: iso\_country\_codes.csv

&#x20;Size: 0.005 MB

&#x20;Rows: 252

&#x20;Columns: 3

&#x20;Column names/types:

&#x20;- iso\_alpha\_2: str

&#x20;- iso\_alpha\_3: str

&#x20;- country\_name: str

&#x20;Missing value rate per column:

&#x20;- iso\_alpha\_2: 0.004

&#x20;- iso\_alpha\_3: 0.0

&#x20;- country\_name: 0.0

============================================================

File: onet\_task\_statements.csv

&#x20;Size: 3.651 MB

&#x20;Rows: 19530

&#x20;Columns: 9

&#x20;Column names/types:

&#x20;- O\*NET-SOC Code: str

&#x20;- Title: str

&#x20;- Task ID: int64

&#x20;- Task: str

&#x20;- Task Type: str

&#x20;- Incumbents Responding: float64

&#x20;- Date: str

&#x20;- Domain Source: str

&#x20;- soc\_major\_group: int64

&#x20;Missing value rate per column:

&#x20;- O\*NET-SOC Code: 0.0

&#x20;- Title: 0.0

&#x20;- Task ID: 0.0

&#x20;- Task: 0.0

&#x20;- Task Type: 0.0337

&#x20;- Incumbents Responding: 0.0337

&#x20;- Date: 0.0

&#x20;- Domain Source: 0.0

&#x20;- soc\_major\_group: 0.0

============================================================

File: soc\_structure.csv

&#x20;Size: 0.079 MB

&#x20;Rows: 1596

&#x20;Columns: 7

&#x20;Column names/types:

&#x20;- Major Group: str

&#x20;- Minor Group: str

&#x20;- Broad Occupation: str

&#x20;- Detailed Occupation: str

&#x20;- Detailed O\*NET-SOC: str

&#x20;- SOC or O\*NET-SOC 2019 Title: str

&#x20;- soc\_major\_group: float64

&#x20;Missing value rate per column:

&#x20;- Major Group: 0.9856

&#x20;- Minor Group: 0.9386

&#x20;- Broad Occupation: 0.7124

&#x20;- Detailed Occupation: 0.4568

&#x20;- Detailed O\*NET-SOC: 0.9066

&#x20;- SOC or O\*NET-SOC 2019 Title: 0.0

&#x20;- soc\_major\_group: 0.9856



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



| File | Claimed (from data\_documentation.md) | Actual (from inventory script) | Match? |

|------|----------------------------------------|----------------------------------|--------|

| aei\_raw\_1p\_api\_2025-08-04\_to\_2025-08-11.csv | Date range: \[8/4/25-???] / Rows: \[33795] | Date range: 2025-08-04 to 2025-08-11 / Rows: 33,794 / Columns: 10 | |

| aei\_raw\_claude\_ai\_2025-08-04\_to\_2025-08-11.csv | Date range: \[8/4/25-???] / Rows: \[100,063] | Date range: 2025-08-04 to 2025-08-11 / Rows: 100,062 / Columns: 10 | |

| gdp\_2024\_us\_state.csv | Should cover 50 states + DC | Rows: \[51] | |

| gdp\_2024\_country.csv | \[check doc for country count] | Rows: \[174] | |

| working\_age\_pop\_2024\_us\_state.csv | Should cover 50 states + DC | Rows: \[51] | |

| working\_age\_pop\_2024\_country.csv | \[check doc for country count] | Rows: \[194] | |

| iso\_country\_codes.csv | Standard ISO list (\~249 entries) | Rows: \[252] | |

| onet\_task\_statements.csv | \~20,000 O\*NET tasks (per brief) | Rows: \[19530] | |

| soc\_structure.csv | \~1,000 occupations (per brief) | Rows: \[1596] | |



\*\*Notes on mismatches:\*\*

aei\_raw\_1p\_api\_2025-08-04\_to\_2025-08-11.csv doesn't specify end date range,

iso\_country\_codes.csv documentation list 249 entries when actual is 252 rows

Onet\_task\_statements.csv specifies 20000 tasks per brief when actual is 19530

soc\_Structure.csv specifies 1000 occupations per brief when actual is 1596.

&#x20;



