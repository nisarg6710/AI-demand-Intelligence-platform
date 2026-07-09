# 📈 Milestone 3 — Production-grade Classical Forecasting

## Overview

This milestone implements a production-style classical forecasting framework for retail demand forecasting using the M5 Forecasting dataset.

Unlike notebook-only implementations, the forecasting system is designed as a reusable software framework with modular models, automatic evaluation, experiment tracking, and prediction persistence.

---

# Objectives

- Build a reusable forecasting framework
- Compare multiple classical forecasting algorithms
- Evaluate forecasting performance using common metrics
- Track forecasting experiments
- Store prediction history
- Prepare a common interface for future deep learning models

---

# Forecasting Pipeline

```text
Daily Sales Data
        │
        ▼
 Train/Test Split
        │
        ▼
 Forecast Model
        │
        ▼
 Prediction
        │
        ▼
 Performance Evaluation
        │
        ▼
 Experiment Tracking
        │
        ▼
 Prediction Storage
        │
        ▼
 Benchmark Report
```

---

# Models Implemented

## Moving Average

Baseline statistical forecasting model using a rolling average.

Purpose:

- Simple benchmark
- Fast execution
- Baseline comparison

---

## ARIMA

Implemented using Statsmodels.

Workflow:

- Stationarity testing
- First-order differencing
- ARIMA model fitting
- Multi-step forecasting

---

## SARIMA

Seasonal extension of ARIMA.

Includes:

- Weekly seasonality
- Seasonal autoregression
- Seasonal moving average

Model parameters were selected using Auto ARIMA and time-series diagnostics.

---

## Prophet

Implemented using Meta Prophet.

Features:

- Trend estimation
- Weekly seasonality
- Yearly seasonality
- Automatic changepoint detection

Prophet achieved the best forecasting performance among the evaluated models.

---

# Time-Series Diagnostics

Performed analyses include:

- Augmented Dickey-Fuller (ADF) Test
- First-order differencing
- ACF plots
- PACF plots
- Auto ARIMA model selection
- Residual diagnostics

These analyses guided the selection of ARIMA and SARIMA parameters.

---

# Evaluation Metrics

Every forecasting model is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)
- Training Time
- Prediction Time

---

# Benchmark Results

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| Moving Average | 5255.92 | 6660.73 | 739.72 |
| ARIMA | 5102.83 | 6626.78 | 732.71 |
| SARIMA | 5176.85 | 6580.66 | 866.94 |
| **Prophet** | **4433.22** | **5560.65** | **628.44** |

**Best Model:** Prophet

---

# Production Features

## Forecast Pipeline

Reusable forecasting pipeline supporting all implemented models.

---

## Experiment Tracking

Every forecasting run is stored in MySQL.

Stored information includes:

- Model name
- Model parameters
- MAE
- RMSE
- MAPE
- Training time
- Prediction time
- Timestamp

---

## Prediction Storage

Forecast predictions are stored in the database for future:

- Dashboard visualization
- API serving
- LLM explanations
- Historical comparisons

---

## Automatic Reporting

Benchmark reports are automatically generated and saved under the `artifacts/` directory.

---

# Key Learnings

During this milestone:

- Built a reusable forecasting framework
- Applied statistical time-series analysis
- Compared multiple forecasting models
- Implemented experiment tracking
- Integrated forecasting with the data warehouse
- Established a common interface for future deep learning models

---

# Next Milestone

Milestone 4 focuses on Deep Learning forecasting.

Planned models include:

- LSTM
- GRU
- Seq2Seq

These models will integrate with the existing forecasting pipeline and experiment tracking framework.