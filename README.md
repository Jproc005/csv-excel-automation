# CSV Cleanup & Standardization Tool

A **business-friendly Python automation tool** that cleans, merges, and standardizes messy CSV files into an **Excel-ready output** — designed for **non-technical users**.

Users simply drop CSVs into a folder and run the tool to receive a clean, consistent dataset for reporting, budgeting, or importing into other systems.

---

## What This Tool Does

* Merges multiple CSV files into one dataset
* Standardizes column headers (lowercase, underscores)
* Trims whitespace and normalizes text
* Removes exact duplicate rows
* Normalizes date formats (e.g., to MM/DD/YYYY)
* Handles missing values safely (no silent deletions)
* Exports a clean Excel or CSV output
* Optional GUI build (PyInstaller)

---

## Non‑Technical User Workflow

1. Place your CSV files into:

```
data/raw/
```

2. Run the tool:

* Double-click the executable (if using GUI/EXE), **or**
* Run from terminal:

```
python src/csv_cleanup_tool.py
```

3. Open the cleaned output in:

```
data/output/
```

---

## Example Use Cases

* Cleaning bank or transaction exports
* Preparing data for accounting systems
* Normalizing reports from multiple vendors
* Removing duplicates and formatting issues
* Preparing files for import into ERP/CRM systems

---

## Project Structure

```
csv-excel-automation/
│
├─ data/
│   ├─ raw/            # user drops CSVs here
│   └─ output/         # cleaned files appear here
│
├─ src/
│   └─ csv_cleanup_tool.py
│
├─ README.md
├─ README_GUI.md
├─ requirements.txt
└─ run_tool.bat (if applicable)
```

---

## Developer Setup

Install dependencies:

```
pip install -r requirements.txt
```

Run from terminal:

```
python src/csv_cleanup_tool.py
```

---

## Tech Stack

* Python
* Pandas
* Excel / CSV I/O
* PyInstaller (optional GUI build)

---

## Why This Project Matters

This is not a toy script. It demonstrates:

* Real-world data cleaning logic
* Business-focused automation
* Non-technical usability
* File-based ETL workflows
* Professional project structure

---

## License

MIT
