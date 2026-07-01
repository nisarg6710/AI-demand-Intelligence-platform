# Milestone 2 — Exploratory Data Analysis

## Objective

Analyze historical retail demand patterns using the data warehouse created during Milestone 1.

---

## Data Source

M5 Forecasting Dataset

---

## Warehouse

The analysis uses the MySQL star schema created in Milestone 1.

Tables:

- sales_fact
- calendar_dim
- item_dim
- store_dim

Analytics View:

- sales_enriched

---

## Exploratory Analysis

The following analyses were performed:

### Trend Analysis

- Daily demand
- Moving averages
- Yearly growth

### Seasonality Analysis

- Weekly seasonality
- Monthly seasonality
- Yearly seasonality

### Store Analysis

- Top stores
- Lowest-performing stores

### Product Analysis

- Best-selling products
- Category performance
- Department performance

### External Factors

- Holiday impact
- SNAP program impact

---

## Prophet Analysis

Facebook Prophet was used to decompose the time series into:

- Trend
- Weekly Seasonality
- Yearly Seasonality

The model was also evaluated using time-series cross-validation.

---

## Key Insights

- Demand grows over time.
- Weekend demand is substantially higher.
- August–September show peak seasonal demand.
- Food products dominate total sales.
- SNAP events positively affect sales.
- Prophet confirms strong seasonal structure.

---

## Deliverables

- Exploratory analysis notebook
- Prophet decomposition notebook
- Business insights report
- Visualizations
- Seasonality analysis

---

## Next Milestone

Milestone 3 focuses on classical forecasting techniques including:

- Moving Average
- ARIMA
- SARIMA
- Prophet

The models will be compared using:

- MAE
- RMSE
- MAPE

to identify the best-performing forecasting approach.