# CSV Cleanup Tool (GUI Version)

A **one-click GUI Python tool** to clean, merge, and standardize CSV files into Excel-ready datasets. Designed for **non-technical users**.

---

## Purpose

This tool helps you:

- Merge multiple CSV files into a single dataset
- Standardize column names (lowercase, underscores instead of spaces)
- Remove duplicates and extra spaces
- Normalize date columns to **MM/DD/YYYY**
- Handle missing values safely
- Output a clean Excel file ready for analysis or reporting

All of this is done with a **simple graphical interface** — no Python knowledge required.

---

## How to Use

1. **Download the project folder** from GitHub.  
2. **Build the executable** (if not already provided):

```powershell
python -m PyInstaller --onefile src/csv_cleanup_gui.py
