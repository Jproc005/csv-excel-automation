import pandas as pd
import glob
import os

RAW_DATA_PATH = "../data/raw/*.csv"
OUTPUT_DIR = "../data/cleaned"

def load_csv_files():
    files = glob.glob(RAW_DATA_PATH)

    if not files:
        raise FileNotFoundError("No CSV files found in data/raw")

    dataframes = [pd.read_csv(file) for file in files]
    return pd.concat(dataframes, ignore_index=True)

def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def remove_empty_rows(df):
    return df.dropna(how="all")

def parse_date_columns(df):
    for column in df.columns:
        if "date" in column:
            parsed_dates = pd.to_datetime(df[column], errors="coerce")

	    # Format as M/D/YYYY, keep blanks as blank
            df[column] = parsed_dates.dt.strftime("%m/%d/%Y")
    return df

def convert_numeric_columns(df):
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="ignore")
    return df

def generate_summary(df):
    numeric_data = df.select_dtypes(include="number")
    return numeric_data.describe()

def save_outputs(df, summary):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df.to_csv(f"{OUTPUT_DIR}/clean_data.csv", index=False)
    df.to_excel(f"{OUTPUT_DIR}/clean_data.xlsx", index=False)
    summary.to_csv(f"{OUTPUT_DIR}/summary_report.csv")

def main():
    print("Starting CSV Cleanup Tool...")

    try:
        df = load_csv_files()
        print(f"Loaded {len(df)} rows")

        df = standardize_columns(df)
        df = remove_empty_rows(df)
        df = parse_date_columns(df)
        df = convert_numeric_columns(df)

        summary = generate_summary(df)
        save_outputs(df, summary)

        print("Cleanup complete.")
        print("Open the cleaned files in data/cleaned/")
    except Exception as error:
        print("ERROR:", error)

if __name__ == "__main__":
    main()
