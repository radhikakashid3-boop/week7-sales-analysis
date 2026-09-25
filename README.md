# Sales Data Analysis Dashboard

## Project Overview

The Sales Data Analysis Dashboard is a Python-based data analysis project developed as part of the Arena Internship Week 7 assignment.

The project analyzes sales data using Pandas, NumPy, Matplotlib, and Jupyter Notebook. It performs data loading, cleaning, exploration, analysis, visualization, and report generation.

## Objectives

- Load sales data from CSV files
- Explore and understand the dataset
- Clean and preprocess sales data
- Calculate important sales metrics
- Analyze sales by category and city
- Identify top-selling products
- Analyze monthly sales trends
- Create data visualizations
- Export processed data and reports
- Perform unit testing

## Features

- CSV data loading
- Data cleaning and preprocessing
- Duplicate detection and removal
- Missing-value handling
- Date conversion
- Sales calculations
- Category-wise analysis
- City-wise analysis
- Product-wise analysis
- Monthly sales trend analysis
- Bar charts
- Line charts
- Pie charts
- Excel report generation
- Text report generation
- CSV export
- Unit testing
- Command-line execution

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- OpenPyXL
- unittest

## Project Structure

```text
week7-sales-analysis/
│
├── sales_analyzer/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── reporter.py
│
├── notebooks/
│   ├── exploration.ipynb
│   └── analysis.ipynb
│
├── data/
│   ├── raw/
│   │   └── sales_data.csv
│   │
│   ├── processed/
│   │   ├── cleaned_sales_data.csv
│   │   ├── exploration_data.csv
│   │   ├── analysis_results.csv
│   │   └── sales_summary.csv
│   │
│   └── reports/
│       ├── sales_analysis_report.xlsx
│       ├── sales_summary.txt
│       └── charts/
│
├── tests/
│   └── test_sales_analyzer.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore