# Task 7 — Basic Sales Summary from SQLite Database
# Objective
- Use Python to fetch a basic sales summary (total quantity and total revenue) from an SQLite database and create a simple bar chart using matplotlib.
# Tools Used
- Python (sqlite3, pandas, matplotlib)
- SQLite (built into Python)
- PowerShell / Command Prompt
# Files
- sales.csv — Sample dataset
- sales_summary.py — Python script
- sales_data.db — SQLite database (generated when running the script)
- sales_summary.csv — Summary table (product, total_qty, revenue)
- sales_chart.png — Bar chart (by revenue)
  
# Step-by-Step Instructions

1) Navigate to the project folder
   cd "C:\Users\HP\Desktop\INTERNSHIP TASK\Task 7"

2) Create a Virtual Environment
  python -m venv .venv

3) Activate the Virtual Environment
   .\.venv\Scripts\Activate.ps1

4) Install required packages
  pip install pandas matplotlib

5) Run the script python sales_summary.py

6) Check the results

- sales_data.db — SQLite database

- sales_summary.csv — Summary table

- sales_chart.png — Bar chart

7) Deactivate the environment deactivate
