import pandas as pd
import os

# List all the data files you're using
DATA_DIR = "data"
FILES = [
        "aei_raw_1p_api_2025-08-04_to_2025-08-11.csv",
        "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv",
        "gdp_2024_us_state.csv",
        "gdp_2024_country.csv",
        "working_age_pop_2024_us_state.csv",
        "working_age_pop_2024_country.csv",
        "iso_country_codes.csv",
        "onet_task_statements.csv",
        "soc_structure.csv",
]

def inventory_file(filename):
    path = os.path.join(DATA_DIR, filename)
    print("=" * 60)
    print(f"File: {filename}")

    if not os.path.exists(path):
        print(" NOT FOUND in data/ — check filename or download")
        return

    size_bytes = os.path.getsize(path)
    print(f" Size: {size_bytes / 1e6:.3f} MB")

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f" Could not read as CSV: {e}")
        return

    print(f" Rows: {len(df)}")
    print(f" Columns: {len(df.columns)}")
    print(f" Column names/types:")
    for col, dtype in df.dtypes.items():
     print(f" - {col}: {dtype}")
    print(f" Missing value rate per column:")
    missing = df.isnull().mean().round(4)
    for col, rate in missing.items():
        print(f" - {col}: {rate}")

def main():
    for f in FILES:
        inventory_file(f)

if __name__ == "__main__":
    main()