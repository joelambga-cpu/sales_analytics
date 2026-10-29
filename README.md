# Sales Analytics

A Python learning project using a fictional sales dataset to calculate revenue and compare regions.

## Implemented workflow

- Calculate revenue as quantity × price.
- Aggregate and sort revenue by region.
- Display a regional revenue chart.
- Export the regional summary to `reports/sales_summary.xlsx`.

The chart opens in a window; close it to let the script finish the Excel export. The sample is illustrative and does not describe a real business.

## Installation and usage

From a terminal with Python available:

```powershell
git clone https://github.com/joelambga-cpu/sales_analytics.git
cd sales_analytics/sales_analytics
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m src.main
```

On macOS/Linux, replace `.\.venv\Scripts\python.exe` with `.venv/bin/python`.

## Files

- [Sample data](sales_analytics/data/sales_data.csv)
- [Source code](sales_analytics/src/)
- [Example Excel output](sales_analytics/reports/sales_summary.xlsx)
