# CSV Data Cleanup & Standardization Tool

A **business-friendly Python automation tool** that cleans, merges, and standardizes CSV files into Excel-ready datasets.

## Purpose

This tool is designed to:

- Merge multiple CSV files into a single dataset
- Standardize column names (lowercase, underscores instead of spaces)
- Remove exact duplicate rows
- Trim extra spaces in text columns
- Handle missing values safely
- Normalize date columns to **MM/DD/YYYY** format
- Output a clean Excel file ready for reporting or analysis

It is **file-agnostic**, works with any CSV, and preserves the integrity of your original data.

## How to Use

1. Place all CSV files to be cleaned into the folder:

data/raw


2. Run the cleanup tool from the project root:

```powershell
python src/csv_cleanup_tool.py

3. When complete, your cleaned dataset will appear in:

data/cleaned/clean_data.xlsx