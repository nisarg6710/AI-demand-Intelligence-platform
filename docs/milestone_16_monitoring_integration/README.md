# Milestone 16 — Production Monitoring Integration

## Overview

Milestone 16 integrates the project's data quality monitoring, model performance monitoring, and data drift detection into a unified monitoring workflow.

The goal is to move monitoring from isolated validation utilities into a reusable production-oriented reporting layer.

The monitoring system can:

- Validate incoming data quality.
- Evaluate forecasting model performance.
- Detect statistical drift between reference and current data.
- Combine monitoring results into a single structured report.
- Persist monitoring reports as JSON artifacts.
- Log monitoring metrics and reports to MLflow.

---

## Architecture

```text
                    ┌─────────────────────────┐
                    │    MonitoringReporter   │
                    └────────────┬────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ▼                   ▼                   ▼
    ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
    │ Data Quality   │  │ Model Monitor  │  │ Drift Monitor  │
    │    Monitor     │  │                │  │                │
    └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
            │                   │                   │
            └───────────────────┼───────────────────┘
                                ▼
                     ┌─────────────────────┐
                     │ Structured Report   │
                     │      (JSON)         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │       MLflow        │
                     │ Metrics + Artifact  │
                     └─────────────────────┘


Monitoring Components
1. Data Quality Monitoring
src/monitoring/data_quality.py
The DataQualityMonitor validates incoming datasets for common quality problems.
It checks:
- Required columns.
- Missing values.
- Duplicate records.
- Negative values in configured non-negative columns.
- Overall data quality status.
The result is represented using:
DataQualityReport


Example:
row_count: 1000
duplicate_count: 0
missing_values: {}
negative_values: {}
passed: True

2. Model Performance Monitoring
src/monitoring/model_monitor.py
The ModelMonitor evaluates forecasting predictions against actual values.
It uses the existing forecasting evaluation layer to calculate:
- MAE
- RMSE
- MAPE
Optional thresholds can be configured to generate alerts when model performance degrades.
Example:
MAE: 3.33
RMSE: 4.08
MAPE: 1.39
passed: True
alerts: []

3. Drift Monitoring
src/monitoring/drift.py
The DriftMonitor compares a reference dataset with current data.
The current implementation uses a standardized mean-shift statistic:
|current_mean - reference_mean| / reference_std

A configurable threshold determines whether drift is detected.
This provides a lightweight monitoring mechanism that can later be replaced or extended with more advanced statistical drift methods.
Unified Monitoring Reporter
src/monitoring/reporter.py
The MonitoringReporter acts as the orchestration layer for all monitoring components.
It can combine:
Data Quality
     +
Model Performance
     +
Data Drift
     ↓
Unified Monitoring Report

Example usage:
from src.monitoring.reporter import MonitoringReporterreporter = MonitoringReporter()report = reporter.generate_report(    data=data,    actual=actual,    predicted=predicted,    reference=reference,    current=current,)reporter.save_report(report)


The resulting report contains:
{
    "timestamp": "...",
    "status": "healthy",
    "data_quality": {},
    "model_performance": {},
    "drift": {}
}

Monitoring Status
The reporter assigns an overall monitoring status.
Healthy
The system reports:
status = healthy

when:
- Data quality checks pass.
- Model performance remains within configured thresholds.
- No significant drift is detected.
Warning
The system reports:
status = warning

when:
- Data quality validation fails.
- Model performance exceeds configured thresholds.
- Data drift is detected.
This provides a simple production-facing health signal.
MLflow Integration
Monitoring results can also be logged to the existing MLflow tracking infrastructure.
The reporter logs:
Tags
project
stage
monitoring_status

Metrics
monitoring_mae
monitoring_rmse
monitoring_mape
drift_statistic

Artifacts
The complete monitoring report is stored as:
monitoring/monitoring_report.json

This allows monitoring history to be tracked alongside forecasting experiments.
Generated Monitoring Artifact
A local monitoring run generates:
artifacts/
└── monitoring/
    └── monitoring_report.json

This is a runtime-generated artifact and is intentionally excluded from Git.
The generated artifact is useful for local inspection but should not be committed to the repository.
Example Integration Run
A small integration test was performed using sample data:
report = reporter.generate_report(    data=data,    actual=actual,    predicted=predicted,)


The resulting report successfully returned:
status: healthy

data_quality:
    row_count: 3
    duplicate_count: 0
    missing_values: {}
    negative_values: {}
    passed: True

model_performance:
    MAE: 3.3333
    RMSE: 4.0825
    MAPE: 1.3889
    passed: True

The report was successfully persisted to:
artifacts/monitoring/monitoring_report.json

Testing
Monitoring functionality is covered by dedicated tests:
tests/
└── monitoring/
    ├── test_data_quality.py
    ├── test_model_monitor.py
    ├── test_drift.py
    └── test_reporter.py

The complete monitoring test suite passed:
10 passed

Existing regression tests were also executed successfully:
12 passed

This confirms that the monitoring integration did not break the existing forecasting and MLflow functionality.
Files Added
src/
└── monitoring/
    ├── __init__.py
    ├── data_quality.py
    ├── model_monitor.py
    ├── drift.py
    └── reporter.py

tests/
└── monitoring/
    ├── __init__.py
    ├── test_data_quality.py
    ├── test_model_monitor.py
    ├── test_drift.py
    └── test_reporter.py

docs/
└── milestone_16_monitoring_integration/
    └── README.md

Technologies
- Python
- Pandas
- NumPy
- MLflow
- Pytest
- JSON-based monitoring reports
Production Value
This milestone establishes the monitoring layer required to operate the forecasting platform beyond offline experimentation.
The system now provides visibility into three important areas:
Data Health
     ↓
Model Health
     ↓
Behavior / Drift

The architecture is intentionally modular so that more sophisticated monitoring methods can be introduced later without changing the overall reporting interface.