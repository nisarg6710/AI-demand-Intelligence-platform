# Milestone 2: Exploratory Data Analysis (EDA)

## Overview

After successfully building the ETL pipeline in Milestone 1, the cleaned retail sales data is now stored in a MySQL database. The objective of this milestone is to perform Exploratory Data Analysis (EDA) to understand the underlying characteristics of the dataset, identify patterns, detect anomalies, and extract meaningful business insights.

This analysis serves as the foundation for feature engineering and machine learning models that will be developed in the upcoming milestones.

---

# Objectives

The primary objectives of this milestone are:

- Connect to the MySQL database and load cleaned data.
- Validate data quality after the ETL process.
- Explore the distribution of numerical and categorical variables.
- Analyze relationships between different features.
- Identify trends, seasonality, and business patterns.
- Detect outliers and potential data quality issues.
- Generate actionable business insights.
- Prepare the dataset for feature engineering and forecasting.

---

# Business Questions

This analysis aims to answer several important business questions:

### Sales Performance

- Which products generate the highest revenue?
- Which categories contribute most to total sales?
- Which stores perform the best?
- Which products have consistently low sales?

### Customer Behavior

- Which customers purchase most frequently?
- What is the average order value?
- Are there repeat purchasing patterns?

### Time-Based Trends

- How do sales change over time?
- Are there seasonal patterns?
- Which months generate the highest revenue?
- Which weekdays have maximum sales?

### Profitability

- Which products generate the highest profit?
- How do discounts affect profit?
- Which categories have poor profit margins?

### Inventory Planning

- Which products have stable demand?
- Which products experience sudden demand spikes?
- Which items may require better inventory planning?

---

# Folder Structure

```
milestone_2/

│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_data_quality_checks.ipynb
│   ├── 03_univariate_analysis.ipynb
│   ├── 04_bivariate_analysis.ipynb
│   ├── 05_correlation_analysis.ipynb
│   ├── 06_time_series_analysis.ipynb
│   └── 07_business_insights.ipynb
│
├── src/
│   ├── database.py
│   ├── data_loader.py
│   ├── plotting.py
│   └── utils.py
│
├── visuals/
│   ├── distributions/
│   ├── correlations/
│   ├── time_series/
│   ├── stores/
│   ├── products/
│   ├── outliers/
│   └── business/
│
├── reports/
│   ├── business_insights.md
│   └── eda_summary.pdf
│
└── README.md
```

---

# Workflow

```
MySQL Database
        │
        ▼
Load Data into Pandas
        │
        ▼
Data Quality Checks
        │
        ▼
Exploratory Data Analysis
        │
        ├── Univariate Analysis
        ├── Bivariate Analysis
        ├── Correlation Analysis
        ├── Time Series Analysis
        ├── Store Analysis
        ├── Product Analysis
        └── Business Insights
        │
        ▼
Feature Engineering (Next Milestone)
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLAlchemy
- PyMySQL
- Jupyter Notebook
- MySQL

---

# Deliverables

At the end of this milestone, the following outputs will be available:

- Data quality assessment
- Exploratory analysis notebooks
- Professional visualizations
- Business insights report
- Correlation analysis
- Time-series trends
- Saved charts and figures
- EDA summary report

---

# Expected Outcomes

By completing this milestone, we will gain a comprehensive understanding of the retail sales dataset, including:

- Key revenue drivers
- Product performance
- Customer purchasing behavior
- Seasonal sales trends
- Store-level performance
- Impact of discounts
- Potential forecasting challenges

These insights will directly guide the feature engineering and forecasting models developed in the next milestones.

---

# Next Milestone

Milestone 3 focuses on Feature Engineering, where the insights obtained during EDA will be transformed into machine learning features for demand forecasting and business intelligence.