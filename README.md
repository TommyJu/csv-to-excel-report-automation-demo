# Coffee Shop Sales Report Automation ☕

An automated reporting pipeline that transforms raw coffee shop sales data into a professional Excel business report.

This project simulates a real-world workflow where a business exports sales data from a system and needs recurring insights without manually cleaning spreadsheets, creating formulas, or building reports.


## 📌 Overview

Many small businesses rely on spreadsheets for reporting, but manually creating weekly/monthly reports can be repetitive and error-prone.

This automation tool:

1. Reads raw CSV sales data
2. Cleans and processes the data
3. Analyzes sales performance
4. Generates an Excel report with business insights

The goal is to turn raw operational data into a report that helps answer:

- What products sell best?
- When are sales strongest?
- Which menu items perform well?
- How do promotions affect product sales?


## ✨ Features

### Data Processing

- Reads CSV sales exports
- Cleans and prepares data
- Handles date formatting
- Organizes sales data for analysis

### Sales Analysis

Generates insights including:

- Total items sold
- Best-selling menu items
- Best sales days
- Monthly sales trends
- Product performance rankings
- Promotion effectiveness

### Automated Excel Report

Creates a formatted Excel workbook containing:

#### Dashboard

- Key performance indicators
- Business summary

#### Product Performance

- Menu rankings
- Top-selling products

#### Sales Trends

- Monthly sales patterns
- Daily sales analysis

#### Promotion Analysis

- Promoted vs non-promoted product performance


## 🚀 Usage

### Install dependencies
> pip install -r requirements.txt
### Add your CSV file
Place your sales data inside:
> input/

Example:
>input/sales.csv

### Run the automation
>python3 main.py
### View your report
The generated Excel report will appear in:
>output/sales_report.xlsx

## 📈 Business Value

Instead of manually creating recurring sales reports, businesses can drop in their latest data export and automatically receive a ready-to-use performance report.

This reduces repetitive spreadsheet work and allows teams to focus on making decisions from their data.

## 🔮 Future Improvements
- Add PDF report generation
- Automatically email reports
- Create interactive dashboards
- Schedule recurring report generation
- Package as a standalone application