import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

# -----------------------------
# Configuration
# -----------------------------
RAW_DATA_PATH = "../data/raw/*.csv"
OUTPUT_CSV = "../data/cleaned/merged_clean_data.csv"
OUTPUT_EXCEL = "../data/cleaned/merged_clean_data.xlsx"

# -----------------------------
# Load and Merge CSV Files
# -----------------------------
def load_and_merge_csvs(path):
    csv_files = glob.glob(path)
    df_list = []

    for file in csv_files:
        df = pd.read_csv(file)
        df_list.append(df)

    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df

# -----------------------------
# Clean Data
# -----------------------------
def clean_data(df):
    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Drop completely empty rows
    df.dropna(how="all", inplace=True)

    # Attempt to parse dates
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Convert numeric columns
    for col in df.select_dtypes(include=["object"]).columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass

    return df

# -----------------------------
# Save Outputs
# -----------------------------
def save_outputs(df):
    os.makedirs("../data/cleaned", exist_ok=True)

    df.to_csv(OUTPUT_CSV, index=False)
    df.to_excel(OUTPUT_EXCEL, index=False)

# -----------------------------
# Optional Plot
# -----------------------------
def generate_plot(df):
    if "date" in df.columns and "amount" in df.columns:
        summary = df.groupby("date")["amount"].sum()

        summary.plot(title="Total Amount Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.show()

# -----------------------------
# Main Pipeline
# -----------------------------
def main():
    print("Loading CSV files...")
    merged_df = load_and_merge_csvs(RAW_DATA_PATH)

    print("Cleaning data...")
    clean_df = clean_data(merged_df)

    print("Saving cleaned files...")
    save_outputs(clean_df)

    print("Pipeline completed successfully.")

    # Optional visualization
    generate_plot(clean_df)

if __name__ == "__main__":
    print("Running full pipeline...")
    merged_df = load_and_merge_csvs(RAW_DATA_PATH)
    clean_df = clean_data(merged_df)
    save_outputs(clean_df)
    print("Pipeline completed successfully.")

    # Optional: generate and save plot
    # Only run if columns exist
    if "date" in clean_df.columns and "amount" in clean_df.columns:
        import matplotlib.pyplot as plt
        summary = clean_df.groupby("date")["amount"].sum()
        summary.plot(title="Total Amount Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.savefig("../data/cleaned/plot.png")
        plt.show()
        print("Plot generated and saved as ../data/cleaned/plot.png")
    else:
        print("Plot not generated: 'date' or 'amount' column not found.")

