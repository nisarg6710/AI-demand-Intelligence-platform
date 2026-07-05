# 📊 AI Demand Intelligence Platform

An end-to-end AI-powered **Demand Forecasting and Business Intelligence Platform** built using modern **Data Engineering, Time Series Forecasting, Machine Learning, Large Language Models (LLMs), Multi-Agent Systems, and MLOps**.

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
- Benchmarking multiple forecasting models
- Tracking forecasting experiments
- Storing prediction history
- Explaining forecasts using LLMs
- Answering business questions through AI agents
- Serving predictions through APIs
- Visualizing insights through an interactive dashboard

The emphasis is on **software engineering**, **scalability**, **modularity**, **experiment reproducibility**, and **production-ready architecture** in addition to forecasting accuracy.

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
            Production Forecasting Framework
                            │
            ┌───────────────┼────────────────┐
            ▼               ▼                ▼
     Moving Average      ARIMA          SARIMA
            │               │                │
            └───────────────┼────────────────┘
                            ▼
                        Prophet
                            │
                            ▼
              Experiment Tracking Database
                            │
                            ▼
             Deep Learning Forecasting (Next)
                            │
                            ▼
          Transformer Forecasting Models
                            │
                            ▼
               LLM + RAG + Multi-Agent AI
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

## Time Series Forecasting

- Statsmodels
- pmdarima
- Prophet

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
│
├── docs/
│   ├── business_case/
│   ├── milestone_01_etl/
│   ├── milestone_02_eda/
│   └── milestone_03_forecasting/
│
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
│   │   ├── base_model.py
│   │   ├── moving_average.py
│   │   ├── arima.py
│   │   ├── sarima.py
│   │   ├── prophet_model.py
│   │   ├── metrics.py
│   │   ├── registry.py
│   │   ├── pipeline.py
│   │   ├── report.py
│   │   ├── experiment.py
│   │   └── visualization.py
│   │
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

### Current ETL Features

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

## Analytics Views

- `sales_enriched`

## Forecasting Tables

- `forecast_experiments`
- `forecast_predictions`

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

# 📈 Milestone 3 — Production-grade Classical Forecasting

Unlike notebook-only forecasting projects, this milestone introduces a **modular forecasting framework** inspired by production Machine Learning systems.

## Implemented Models

- Moving Average
- ARIMA
- SARIMA
- Prophet

## Production Features

- Common forecasting interface
- Base forecasting class
- Modular forecasting pipeline
- Automatic train/test split
- Unified evaluation metrics
- Automatic visualization
- Model registry
- Benchmark runner
- Experiment tracking
- Prediction persistence
- Automatic report generation
- Reproducible forecasting experiments

## Evaluation Metrics

Every model is evaluated using:

- MAE
- RMSE
- MAPE
- Training Time
- Prediction Time

## Experiment Tracking

Every forecasting run is automatically stored inside MySQL.

Stored metadata includes:

- Model name
- Parameters
- MAE
- RMSE
- MAPE
- Training time
- Prediction time
- Timestamp

Prediction values are also persisted for later comparison and dashboard visualization.

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

## ✅ Milestone 3 — Production-grade Classical Forecasting

Completed:

- Moving Average
- ARIMA
- SARIMA
- Prophet
- Model Benchmarking
- Forecast Pipeline
- Model Registry
- Experiment Tracking
- Prediction Storage
- Forecast Reports
- Automatic Visualization

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

## Classical Forecasting Benchmark

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| Moving Average | 5255.92 | 6660.73 | 739.72 |
| ARIMA | 5102.83 | 6626.78 | 732.71 |
| SARIMA | 5176.85 | 6580.66 | 866.94 |
| **Prophet** | **4433.22** | **5560.65** | **628.44** |

**Best Performing Model:** **Prophet**
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

# 🗺 Roadmap

| Status | Milestone |
|--------|-----------|
| ✅ | Milestone 0 — Business Understanding |
| ✅ | Milestone 1 — Data Engineering & Data Warehouse |
| ✅ | Milestone 2 — Exploratory Data Analysis |
| ✅ | Milestone 3 — Production-grade Classical Forecasting |
| 🚧 | Milestone 4 — Deep Learning Forecasting |
| ⬜ | Milestone 5 — Transformer Forecasting |
| ⬜ | Milestone 6 — LLM-powered Forecast Explanations |
| ⬜ | Milestone 7 — Retrieval-Augmented Generation (RAG) |
| ⬜ | Milestone 8 — Multi-Agent AI System |
| ⬜ | Milestone 9 — FastAPI Backend |
| ⬜ | Milestone 10 — React Dashboard |
| ⬜ | Milestone 11 — Deployment & MLOps |

---

# 🔒 Configuration

Sensitive configuration files are **not tracked** by Git.

Create your own configuration file:

```text
configs/database.yaml
```

using

```text
configs/database.example.yaml
```

and update it with your MySQL credentials.

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone <repository-url>
cd AI-demand-intelligence-platform
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

---

## 3. Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure MySQL

Copy

```text
configs/database.example.yaml
```

to

```text
configs/database.yaml
```

and update your credentials.

---

## 6. Create the database schema

Execute

```text
src/database/schema.sql
```

using MySQL Workbench.

---

## 7. Run ETL Pipelines

Example

```bash
python -m tests.test_sales_pipeline
```

---

## 8. Run Exploratory Data Analysis

Open

```text
notebooks/02_m2_eda.ipynb
```

and execute the notebook.

---

## 9. Run Individual Forecasting Models

### Moving Average

```bash
python -m tests.test_moving_average
```

### ARIMA

```bash
python -m tests.test_arima
```

### SARIMA

```bash
python -m tests.test_sarima
```

### Prophet

```bash
python -m tests.test_prophet
```

---

## 10. Benchmark All Classical Models

```bash
python -m tests.benchmark_classical_models
```

This will automatically:

- Train every forecasting model
- Evaluate forecasting performance
- Generate comparison metrics
- Save experiments into MySQL
- Store prediction history
- Produce a benchmarking summary

---

# 📈 Current Forecasting Results

| Model | MAE | RMSE | MAPE | Status |
|------|------:|------:|------:|--------|
| Moving Average | 5255.92 | 6660.73 | 739.72 | ✅ |
| ARIMA | 5102.83 | 6626.78 | 732.71 | ✅ |
| SARIMA | 5176.85 | 6580.66 | 866.94 | ✅ |
| Prophet | **4433.22** | **5560.65** | **628.44** | 🏆 Best |

---

# 📌 Current Status

## Current Version

# **v3.0.0**

---

## Completed

- ✅ Business Understanding
- ✅ Production-grade ETL Framework
- ✅ MySQL Star Schema
- ✅ Analytics SQL View
- ✅ Exploratory Data Analysis
- ✅ Prophet Trend & Seasonality Analysis
- ✅ Production-grade Classical Forecasting Framework
- ✅ Forecast Benchmarking
- ✅ Model Registry
- ✅ Experiment Tracking
- ✅ Prediction Storage
- ✅ Automatic Forecast Reports

---

## Current Focus

🚧 **Milestone 4 — Deep Learning Forecasting**

Upcoming work includes:

- LSTM Forecasting
- GRU Forecasting
- Seq2Seq Models
- Encoder–Decoder Architectures
- Deep Learning Benchmark Suite
- Hyperparameter Optimization
- Model Comparison Dashboard

---

# 🌟 Project Highlights

This project now includes:

### Data Engineering

- Production ETL framework
- Chunk-based processing
- MySQL Star Schema
- Configuration-driven pipelines

### Analytics

- Business-oriented EDA
- SQL analytics layer
- Prophet decomposition
- Seasonality analysis

### Forecasting

- Modular forecasting framework
- Four forecasting algorithms
- Unified forecasting interface
- Automatic benchmarking
- Automatic visualization
- Automatic evaluation

### Experiment Tracking

- Forecast registry
- MySQL experiment database
- Prediction persistence
- Forecast reports
- Performance benchmarking

### Software Engineering

- Modular architecture
- Reusable components
- Separation of concerns
- Production-ready project structure
- Extensible forecasting framework

---

# 🎯 Next Milestone

The next major milestone focuses on **Deep Learning for Time Series Forecasting**, where the project will transition from classical statistical models to neural-network-based forecasting.

Planned implementations include:

- LSTM
- GRU
- Seq2Seq
- Model checkpointing
- Training history visualization
- GPU support
- Early stopping
- Learning rate scheduling
- Deep Learning experiment tracking

---

# 🤝 Contributing

Contributions, suggestions, improvements, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!

It helps others discover the project and motivates future development.