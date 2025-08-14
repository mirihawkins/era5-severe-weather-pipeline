\# ERA5 Severe Weather Pipeline



\## Goal

A reproducible Python pipeline that processes ERA5 weather data to detect anomalies and generate an auto-report with visualization. !\[Example Output](outputs/fig\_anomalies.png)



\## Data Sources

\- This is a template of a working model I made, so the .csv input currently holds fabricated values. However, it is intended to process NOAA/ERA5 datasets of this type.



\## Methods

The pipeline:

1\. Loads ERA5 data (sample subset for demo).

2\. Creates four predictors: CAPE, CIN, Temperature, Pressure.

3\. Calculates z-score anomalies on temperature.

4\. Flags high anomalies and creates a scatter plot.

5\. Saves processed data and a one-page auto-memo.



\## Reproduction Steps

1\. Open `notebooks/era5\_pipeline.ipynb`

2\. Run all cells

3\. Check `outputs/` for `features.csv` and `fig\_anomalies.png`





