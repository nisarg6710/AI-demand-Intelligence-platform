# M15 — Model & Data Monitoring

## Overview

This milestone introduces lightweight monitoring capabilities for
the AI Demand Intelligence Platform.

The monitoring layer covers:

- Data quality
- Forecasting model performance
- Distribution drift

The implementation is designed to operate on sampled or aggregated
data rather than repeatedly scanning the complete 58M+ row warehouse.

---

## Architecture

```text
                 MySQL Warehouse
                       |
                       v
              Data Quality Monitor
                       |
                       v
                Quality Report


              Forecasting System
                       |
                       v
                ForecastEvaluator
                       |
                       v
                 Model Monitor
                       |
                       v
                Metric Alerts


          Reference Data + Current Data
                       |
                       v
                 Drift Monitor
                       |
                       v
                 Drift Report


Components
Data Quality Monitor
File:
src/monitoring/data_quality.py

Checks:
- Required columns
- Missing values
- Duplicate records
- Negative numeric values
- Overall validation status
The monitor produces a structured DataQualityReport.
Model Monitor
File:
src/monitoring/model_monitor.py

The model monitor reuses the existing forecasting evaluation layer.
Metrics:
- MAE
- RMSE
- MAPE
Configurable thresholds allow the system to generate alerts when
forecasting performance deteriorates.
Drift Monitor
File:
src/monitoring/drift.py

The drift monitor compares reference and current numerical
distributions using a lightweight standardized mean-shift statistic.
It avoids introducing an additional monitoring framework while
providing a foundation for production drift detection.
Design Decisions
Lightweight
The project already contains:
- PySpark
- MySQL
- MLflow
- forecasting models
- CI/CD
A separate monitoring framework was intentionally avoided.
Scalable
Monitoring should not repeatedly process the complete 58M+ row
sales warehouse.
Instead, monitoring can operate on:
- Aggregated analytics tables
- Samples
- Forecast evaluation windows
- Feature summaries
Reusable
The monitoring classes are independent of individual forecasting
models and can therefore be reused for:
- ARIMA
- SARIMA
- Prophet
- Moving Average
- Future forecasting models
Testing
Run:
python -m pytest tests/monitoring -v

The monitoring layer is covered by unit tests for:
- Successful data-quality validation
- Negative-value detection
- Successful model monitoring
- Model degradation detection
- Drift detection
- Invalid input handling