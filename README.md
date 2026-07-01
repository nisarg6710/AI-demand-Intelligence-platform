# 📊 AI Demand Intelligence Platform

An end-to-end AI-powered **Demand Forecasting and Business Intelligence Platform** built using modern Data Engineering, Time Series Forecasting, Machine Learning, Large Language Models (LLMs), Multi-Agent Systems, and MLOps.

The project follows a production-grade workflow, beginning with raw retail data and progressing through scalable ETL pipelines, a MySQL data warehouse, business analytics, forecasting, explainable AI, APIs, dashboards, and cloud deployment.

---

# 🎯 Project Overview

Demand forecasting is one of the most important problems in retail and supply chain management. Poor forecasts lead to:

- Overstocking
- Stockouts
- Increased inventory costs
- Inefficient staffing
- Poor logistics planning

This project aims to build a complete AI-powered demand intelligence platform capable of:

- Building scalable ETL pipelines
- Designing a production-grade data warehouse
- Performing business analytics
- Forecasting product demand
- Explaining forecasts using LLMs
- Answering business questions through AI agents
- Serving predictions through APIs
- Visualizing insights through an interactive dashboard

The emphasis is on **software engineering**, **scalability**, **modularity**, and **production-ready architecture** in addition to forecasting accuracy.

---

# 🏗 System Architecture

```text
                     Raw Retail Data
                            │
                            ▼
                  ETL Data Engineering Layer
                            │
                            ▼
                    MySQL Star Schema Warehouse
                            │
                            ▼
                  Analytics Layer (SQL Views)
                            │
                            ▼
              Exploratory Data Analysis (EDA)
                            │
                            ▼
            Classical Forecasting Models
                            │
                            ▼
          Deep Learning & Transformer Models
                            │
                            ▼
             LLM + RAG + Multi-Agent System
                            │
                            ▼
                 FastAPI Backend Services
                            │
                            ▼
                 React Business Dashboard
```

---

# 🛠 Tech Stack

## Programming

- Python 3.12

## Data Engineering

- Pandas
- NumPy
- MySQL
- YAML Configuration
- Chunk-based ETL

## Data Visualization

- Matplotlib
- Seaborn

## Time Series Analysis

- Facebook Prophet

## Machine Learning *(Upcoming)*

- Scikit-Learn
- XGBoost
- LightGBM

## Deep Learning *(Upcoming)*

- PyTorch

## LLM & AI *(Upcoming)*

- LangChain
- FAISS
- OpenAI / Open Source LLMs

## Backend *(Upcoming)*

- FastAPI

## Frontend *(Upcoming)*

- React
- Tailwind CSS

## Deployment *(Upcoming)*

- Docker
- Docker Compose
- GitHub Actions

---

# 📂 Project Structure

```text
AI-demand-intelligence-platform/
│
├── artifacts/
├── configs/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── deployment/
├── docs/
├── logs/
├── notebooks/
│
├── src/
│   ├── analytics/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── etl/
│   ├── forecasting/
│   ├── observability/
│   ├── pipelines/
│   ├── transforms/
│   └── utils/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# 📦 Dataset

This project uses the **M5 Forecasting – Accuracy** dataset.

Datasets used:

- Calendar
- Sell Prices
- Sales History

Future versions may integrate:

- Weather Data
- Promotion Data
- External Economic Indicators

---

# ⚙ ETL Pipeline

The ETL framework follows a modular and reusable architecture.

```text
Raw CSV
    │
    ▼
Extraction
    │
    ▼
Validation
    │
    ▼
Transformation
    │
    ▼
Loading
    │
    ▼
MySQL Data Warehouse
```

Current ETL Features

- Generic CSV extractor
- Configuration-driven pipelines
- Generic transformer interface
- Data validation
- Batch loading using `executemany()`
- Chunk-based processing
- Execution metrics
- Reusable pipeline architecture

---

# 🗄 Data Warehouse

The project uses a **Star Schema** optimized for analytical workloads.

## Dimension Tables

- `calendar_dim`
- `item_dim`
- `store_dim`

## Fact Tables

- `sales_fact`
- `price_fact`

## Analytics View

- `sales_enriched`

---

# 📊 Exploratory Data Analysis

Business-oriented exploratory analysis has been performed directly on the MySQL warehouse.

Completed analyses include:

- Daily demand trend
- Weekly seasonality
- Monthly seasonality
- Year-over-year growth
- Holiday impact
- SNAP impact
- Store performance
- Category performance
- Department performance
- Top-selling products
- Prophet trend decomposition
- Prophet seasonality decomposition

---

# 🚀 Completed Milestones

## ✅ Milestone 0 — Business Understanding

- Business problem definition
- Project objectives
- Business value analysis
- Project planning

---

## ✅ Milestone 1 — Data Engineering & Data Warehouse

- Generic ETL framework
- Configuration-driven pipelines
- MySQL Star Schema
- Calendar ETL
- Store Dimension ETL
- Item Dimension ETL
- Sell Price ETL
- Sales Fact ETL
- Chunk-based processing
- Execution metrics
- Analytics SQL View (`sales_enriched`)

---

## ✅ Milestone 2 — Exploratory Data Analysis

Completed analyses:

- Demand trend analysis
- Weekly seasonality
- Monthly seasonality
- Year-over-year growth
- Holiday analysis
- SNAP analysis
- Store performance
- Category analysis
- Department analysis
- Product analysis
- Prophet decomposition
- Business insights

---

# ⚡ Performance Benchmarks

## Sell Prices ETL

| Metric | Value |
|---------|------:|
| Rows Processed | **6,841,121** |
| Chunk Processing | ✅ |
| Batch Loading | `executemany()` |
| Execution Time | ~10 minutes |
| Throughput | ~11,300 rows/sec |

---

## Sales History ETL

| Metric | Value |
|---------|------:|
| Rows Processed | **58,326,370** |
| Chunk Processing | ✅ |
| Chunk Size | 50,000 |
| Execution Metrics | ✅ |
| Warehouse Loaded | ✅ |

---

# 🗺 Roadmap

| Status | Milestone |
|--------|-----------|
| ✅ | Milestone 0 — Business Understanding |
| ✅ | Milestone 1 — Data Engineering |
| ✅ | Milestone 2 — Exploratory Data Analysis |
| 🚧 | Milestone 3 — Classical Forecasting |
| ⬜ | Milestone 4 — Deep Learning Forecasting |
| ⬜ | Milestone 5 — Transformer Forecasting |
| ⬜ | Milestone 6 — LLM Forecast Explanations |
| ⬜ | Milestone 7 — Retrieval-Augmented Generation |
| ⬜ | Milestone 8 — Multi-Agent AI System |
| ⬜ | Milestone 9 — FastAPI Backend |
| ⬜ | Milestone 10 — React Frontend |
| ⬜ | Milestone 11 — Deployment & MLOps |

---

# 🔒 Configuration

Sensitive configuration files are **not tracked** by Git.

Create your own configuration file:

```text
configs/database.yaml
```

using:

```text
configs/database.example.yaml
```

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone <repository-url>
cd AI-demand-intelligence-platform
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure MySQL

Copy:

```text
configs/database.example.yaml
```

to

```text
configs/database.yaml
```

and update your credentials.

## Create Database Schema

Execute:

```text
src/database/schema.sql
```

using MySQL Workbench.

## Run ETL

Example:

```bash
python -m tests.test_sales_pipeline
```

---

# 📌 Current Status

**Current Version:** **v2.0**

### Completed

- Business Understanding
- Production-grade ETL Framework
- MySQL Star Schema
- Analytics SQL View
- Exploratory Data Analysis
- Prophet Seasonality Analysis

### Current Focus

🚧 **Milestone 3 — Classical Time Series Forecasting**

Upcoming models:

- Moving Average
- ARIMA
- SARIMA
- Prophet Evaluation

---

# 🤝 Contributing

Contributions, suggestions, improvements, and feature requests are welcome.

Feel free to fork the repository and open a pull request.

---

# 📄 License

This project is licensed under the MIT License.