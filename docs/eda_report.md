# Exploratory Data Analysis Report

## Project

AI Demand Intelligence Platform

---

# Objective

The objective of this analysis was to understand the historical demand patterns in the M5 retail dataset before building forecasting models.

The analysis focused on identifying:

- Demand trend
- Weekly seasonality
- Monthly seasonality
- Yearly trend
- Category performance
- Store performance
- Product performance
- Holiday impact
- SNAP program impact

---

# Dataset

Source:
M5 Forecasting Dataset

Time Period:
2011-01-29 to 2016-06-19

Number of Days:
1913

Warehouse:
MySQL Star Schema

Tables Used:

- sales_fact
- calendar_dim
- item_dim
- store_dim

Analytics View:

sales_enriched

---

# Trend Analysis

Average daily sales consistently increased throughout the available time period.

Observations:

- Strong growth from 2011 to 2013
- Slight plateau around 2014
- Significant increase during 2015–2016

Business Insight:

Customer demand is growing over time, indicating an expanding retail business.

---

# Weekly Seasonality

Highest Sales:

- Saturday
- Sunday

Lowest Sales:

- Tuesday
- Wednesday
- Thursday

Business Insight:

Demand increases substantially during weekends.

Recommendation:

- Increase staffing on weekends.
- Allocate additional inventory before weekends.

---

# Monthly Seasonality

Highest Average Sales:

- August
- September

Lowest Average Sales:

- May

Business Insight:

Late summer demonstrates the highest demand.

Recommendation:

Inventory planning should account for increased seasonal demand during Q3.

---

# Store Performance

Top Performing Store:

CA_3

Lowest Performing Store:

CA_4

Business Insight:

Certain stores significantly outperform others.

Recommendation:

Investigate operational differences between high-performing and low-performing stores.

---

# Category Performance

Sales Ranking:

1. FOODS
2. HOUSEHOLD
3. HOBBIES

Business Insight:

Food products dominate overall demand.

Recommendation:

Inventory optimization efforts should primarily focus on the FOODS category.

---

# Department Performance

Top Department:

FOODS_3

Lowest Department:

HOBBIES_2

Business Insight:

A small number of departments generate the majority of sales.

---

# Product Analysis

The top 20 products contribute disproportionately to overall sales.

Business Insight:

Demand follows a long-tail distribution.

Recommendation:

Prioritize forecasting accuracy for high-volume products.

---

# SNAP Analysis

Sales are consistently higher on SNAP-supported days across California, Texas, and Wisconsin.

Business Insight:

Government assistance programs have measurable effects on consumer purchasing behavior.

---

# Holiday Analysis

Holiday periods exhibit demand changes relative to non-holiday periods.

Recommendation:

Future forecasting models should incorporate holiday features.

---

# Prophet Seasonality Analysis

Prophet decomposition identified:

- Long-term upward trend
- Strong weekly seasonality
- Clear yearly seasonal cycles

The decomposition confirmed patterns identified during exploratory data analysis.

---

# Summary

Major Findings

- Demand increases year over year.
- Weekend sales significantly exceed weekday sales.
- August and September represent peak demand.
- Food products dominate total sales.
- SNAP programs influence purchasing behavior.
- Demand exhibits strong seasonal characteristics.

These findings provide a solid foundation for building forecasting models in the next milestone.