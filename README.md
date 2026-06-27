# 📊 AI Demand Intelligence Platform

An end-to-end AI-powered **Demand Forecasting and Business Intelligence Platform** built using modern Data Engineering, Machine Learning, Large Language Models (LLMs), Multi-Agent Systems, and MLOps practices.

The project follows a production-style workflow that starts with raw retail data and progresses through ETL, analytics, forecasting, explainable AI, APIs, dashboards, and cloud deployment.

---

# 🎯 Project Overview

Demand forecasting is one of the most important problems in retail and supply chain management. Poor forecasts lead to:

* Overstocking
* Stockouts
* Increased inventory costs
* Inefficient staffing
* Poor logistics planning

This project aims to build a complete AI-powered demand intelligence platform capable of:

* Building scalable ETL pipelines
* Designing a data warehouse
* Performing business analytics
* Forecasting product demand
* Explaining forecasts using LLMs
* Answering business questions through AI agents
* Serving predictions through APIs
* Visualizing insights via a modern web dashboard

The project emphasizes **software engineering**, **scalability**, **modularity**, and **production-ready architecture** in addition to machine learning performance.

---

# 🏗 System Architecture

```text
                     Raw Retail Data
                            │
                            ▼
                  ETL Data Engineering Layer
                            │
                            ▼
                     MySQL Data Warehouse
                            │
                            ▼
                 Feature Engineering Pipeline
                            │
                            ▼
                Forecasting Models (ML / DL)
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

* Python 3.12

## Data Engineering

* Pandas
* NumPy
* MySQL
* YAML Configuration
* Chunk-based ETL

## Data Visualization

* Matplotlib
* Seaborn

## Machine Learning *(Upcoming)*

* Scikit-Learn
* XGBoost
* LightGBM

## Deep Learning *(Upcoming)*

* PyTorch

## LLM & AI *(Upcoming)*

* LangChain
* FAISS
* OpenAI / Open Source LLMs

## Backend *(Upcoming)*

* FastAPI

## Frontend *(Upcoming)*

* React
* Tailwind CSS

## Deployment *(Upcoming)*

* Docker
* Docker Compose
* GitHub Actions

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
├── model-files/
├── notebooks/
│
├── src/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── etl/
│   ├── features/
│   ├── frontend/
│   ├── models/
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

Current datasets:

* Calendar
* Sell Prices

Upcoming datasets:

* Sales History
* Weather Data
* Holiday Data

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

Current ETL features:

* Generic CSV extractor
* Configuration-driven pipelines
* Generic transformer interface
* Data validation
* Batch loading using `executemany()`
* Chunk-based processing
* Execution metrics
* Reusable pipeline architecture

---

# 🗄 Data Warehouse

Current database tables:

## Dimension Tables

* `calendar_dim`
* `store_dim`
* `item_dim`

## Fact Tables

* `price_fact`

Future milestones will introduce:

* `sales_fact`
* Weather tables
* Feature tables
* Prediction tables
* Model metrics tables

---

# 📈 Milestone 1 Achievements

### ✅ Completed

* Project architecture
* Configuration management
* Generic ETL framework
* MySQL integration
* Dynamic SQL generation
* Generic data loader
* Validation framework
* Modular ETL pipelines
* Chunk-based processing
* Execution metrics
* Calendar ETL
* Store dimension ETL
* Item dimension ETL
* Sell Price ETL

---

# ⚡ Performance Benchmark

Largest ETL execution completed successfully:

| Metric           |            Value |
| ---------------- | ---------------: |
| Dataset          |      Sell Prices |
| Rows Processed   |    **6,841,121** |
| Chunk Processing |      ✅ Supported |
| Batch Loading    |  `executemany()` |
| Execution Time   |      ~10 minutes |
| Throughput       | ~11,300 rows/sec |

---

# 🗺 Project Roadmap

## ✅ Milestone 0 — Business Understanding

* Business problem definition
* Project objectives
* Business value analysis
* Project planning

---

## ✅ Milestone 1 — Data Engineering & Data Warehouse

* Generic ETL framework
* Configuration-driven pipelines
* MySQL data warehouse
* Calendar ETL
* Store & Item dimension ETL
* Sell Price ETL (6.8M+ rows)
* Chunk-based processing
* Execution metrics
* Database schema design

---

## 🚧 Milestone 2 — Exploratory Data Analysis

* Demand trend analysis
* Seasonality analysis
* Holiday impact analysis
* Price analysis
* Hierarchical demand analysis
* Business insights

---

## 🚧 Milestone 3 — Classical Forecasting

* Moving Average
* ARIMA
* SARIMA
* Prophet
* Forecast evaluation

---

## 🚧 Milestone 4 — Deep Learning Forecasting

* LSTM
* GRU
* Seq2Seq
* Model comparison

---

## 🚧 Milestone 5 — Transformer-based Forecasting

* PatchTST
* Informer
* Temporal Fusion Transformer (TFT)

---

## 🚧 Milestone 6 — LLM-powered Forecast Explanations

* Natural language forecast summaries
* Business recommendations
* Explainable AI

---

## 🚧 Milestone 7 — Retrieval-Augmented Generation (RAG)

* FAISS Vector Database
* Historical report retrieval
* Retail policy retrieval

---

## 🚧 Milestone 8 — Multi-Agent AI System

* Forecast Agent
* Analytics Agent
* Inventory Agent
* SQL Agent
* Executive Reporting Agent

---

## 🚧 Milestone 9 — FastAPI Backend

* Forecast API
* Chat API
* Analytics API
* Report API

---

## 🚧 Milestone 10 — React Frontend

* Business Dashboard
* Forecast Visualization
* Analytics Dashboard
* AI Chat Interface
* Agent Control Panel

---

## 🚧 Milestone 11 — Deployment & MLOps

* Docker
* Docker Compose
* CI/CD
* Cloud Deployment
* Production Monitoring

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

## Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure the database

Copy:

```text
configs/database.example.yaml
```

to:

```text
configs/database.yaml
```

and update your MySQL credentials.

## Create the database schema

Execute:

```text
src/database/schema.sql
```

using MySQL Workbench.

## Run an ETL pipeline

Example:

```bash
python -m tests.test_price_pipeline
```

---

# 📌 Current Status

**Current Version:** v1.0 (Milestone 1)

Completed:

* Generic ETL Framework
* MySQL Data Warehouse
* Data Engineering Pipeline

Next Objective:

**Milestone 2 — Exploratory Data Analysis & Business Insights**

---

# 🤝 Contributing

Contributions, suggestions, improvements, and feature requests are welcome.

Feel free to fork the repository and open a pull request.

---

# 📄 License

This project is licensed under the MIT License.
