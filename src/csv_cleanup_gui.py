import pandas as pd
from pathlib import Path
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

# -------------------------------
# Data processing functions
# -------------------------------
def load_and_merge_csvs(input_path):
    files = glob.glob(str(input_path / "*.csv"))
    if not files:
        raise FileNotFoundError("No CSV files found in the selected folder.")
    df_list = [pd.read_csv(file) for file in files]
    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def normalize_date_columns(df):
    for column in df.columns:
        if "date" in column:
            parsed_dates = pd.to_datetime(df[column], errors="coerce")
            df[column] = parsed_dates.dt.strftime("%m/%d/%Y")
    return df

def clean_data(df):
    df = clean_column_names(df)
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()
    df.replace(
        ["N/A", "n/a", "NA", "na", "None", "none", ""],
        pd.NA,
        inplace=True
    )
    df = normalize_date_columns(df)
    df.drop_duplicates(inplace=True)
    return df

def save_output(df, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(output_path, index=False)

# -------------------------------
# GUI Functions
# -------------------------------
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_folder.set(folder)

def run_cleanup():
    try:
        folder_path = Path(input_folder.get())
        output_path = folder_path.parent / "cleaned" / "clean_data.xlsx"

        df = load_and_merge_csvs(folder_path)
        clean_df = clean_data(df)
        save_output(clean_df, output_path)

        messagebox.showinfo("Success", f"Cleaning Complete!\nSaved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# GUI Layout
# -------------------------------
root = tk.Tk()
root.title("CSV Cleanup Tool")
root.geometry("450x150")

input_folder = tk.StringVar()

tk.Label(root, text="Select folder with CSV files:").pack(pady=5)
tk.Entry(root, textvariable=input_folder, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Clean Data", command=run_cleanup).pack(pady=10)

root.mainloop()
