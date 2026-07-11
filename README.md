# 📊 AI Demand Intelligence Platform

> **Production-grade AI-powered Demand Forecasting & Business Intelligence Platform**

An end-to-end project demonstrating **Data Engineering**, **Business Analytics**, **Classical Time Series Forecasting**, **Deep Learning Forecasting**, **Transformer-based Forecasting**, and the roadmap toward **LLMs, RAG, Multi-Agent Systems, APIs, Dashboards, and MLOps**.

---

# 🎯 Project Overview

Demand forecasting is one of the most challenging problems in retail and supply chain management. Poor forecasts lead to stockouts, overstocking, increased inventory costs, inefficient staffing, and poor logistics planning.

Instead of building a notebook-only forecasting solution, this project focuses on developing a **production-grade AI forecasting platform** with reusable software components, experiment reproducibility, benchmarking, and modular architecture.

## Current Capabilities

- Production ETL framework
- MySQL Star Schema warehouse
- Business analytics
- Exploratory Data Analysis (EDA)
- Classical forecasting framework
- Deep Learning forecasting framework
- Transformer forecasting framework
- Experiment tracking
- Model checkpointing
- Unified benchmarking

---

# ⭐ Features

## 📦 Data Engineering

- Generic ETL framework
- Chunk-based processing
- Configuration-driven pipelines
- MySQL Data Warehouse
- Execution metrics

---

## 📊 Business Analytics

- SQL analytics layer
- Business-oriented EDA
- Prophet trend decomposition
- Prophet seasonality decomposition

---

## 📈 Classical Forecasting

Implemented Models:

- Moving Average
- ARIMA
- SARIMA
- Prophet

Framework Features:

- Common forecasting interface
- Automatic evaluation
- Benchmark runner
- Model registry
- Experiment tracking
- Automatic visualization

---

## 🧠 Deep Learning Forecasting

Implemented Models:

- LSTM
- GRU
- Seq2Seq

Framework Features:

- Sliding-window dataset generation
- CUDA / GPU Training
- Early Stopping
- Model Checkpointing
- Generic Trainer
- Generic Evaluator
- Deep Learning Benchmark

---

## 🤖 Transformer Forecasting

Implemented Models:

- PatchTST
- Informer (ProbSparse Attention)
- Temporal Fusion Transformer (TFT)

Framework Features:

- Base Transformer abstraction
- Positional Encoding
- ProbSparse Attention
- Variable Selection Network
- Gated Residual Network
- Shared training pipeline
- Shared evaluation pipeline
- Transformer Benchmark

---

# 🏗 System Architecture

```text
Raw Retail Data
        │
        ▼
ETL Pipeline
        │
        ▼
MySQL Star Schema Warehouse
        │
        ▼
Analytics & Business Intelligence
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Classical Forecasting
(Moving Average • ARIMA • SARIMA • Prophet)
        │
        ▼
Deep Learning Forecasting
(LSTM • GRU • Seq2Seq)
        │
        ▼
Transformer Forecasting
(PatchTST • Informer • TFT)
        │
        ▼
LLM + RAG + Multi-Agent AI
        │
        ▼
FastAPI Backend
        │
        ▼
React Dashboard
```

---

# 🛠 Tech Stack

## Programming

- Python 3.12

## Data Engineering

- Pandas
- NumPy
- MySQL

## Time Series Forecasting

- Statsmodels
- pmdarima
- Prophet

## Deep Learning

- PyTorch
- CUDA

## Data Visualization

- Matplotlib
- Seaborn

## Upcoming

- LangChain
- FAISS
- FastAPI
- React
- Docker
- GitHub Actions

---

# 📂 Project Structure

```text
docs/
├── business_case/
├── milestone_01_etl/
├── milestone_02_eda/
├── milestone_03_forecasting/
├── milestone_04_deep_learning/
└── milestone_05_transformers/

src/
├── analytics/
├── database/
├── etl/
├── forecasting/
│   ├── classical/
│   ├── deep_learning/
│   └── transformers/
└── utils/

artifacts/
├── models/
├── benchmarks/
└── plots/
```

---

# 📦 Dataset

This project uses the **M5 Forecasting – Accuracy** dataset.

Datasets used:

- Calendar
- Sell Prices
- Sales History

Future extensions may incorporate:

- Weather Data
- Promotions
- External Economic Indicators

---

# ⚙ ETL Pipeline

```text
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
MySQL Warehouse
```

### Features

- Generic CSV Extractor
- Validation Framework
- Batch Loading
- Chunk Processing
- Execution Metrics

---

# 🗄 Data Warehouse

## Dimension Tables

- calendar_dim
- item_dim
- store_dim

## Fact Tables

- sales_fact
- price_fact

## Analytics Views

- sales_enriched

## Forecasting Tables

- forecast_experiments
- forecast_predictions

---

# 📊 Exploratory Data Analysis

Completed analyses include:

- Daily Demand Trends
- Weekly Seasonality
- Monthly Seasonality
- Year-over-Year Growth
- Holiday Impact
- SNAP Impact
- Store Performance
- Department Performance
- Category Performance
- Prophet Trend Decomposition
- Prophet Seasonality Decomposition

---

# 📈 Forecasting Framework

## Classical Models

- Moving Average
- ARIMA
- SARIMA
- Prophet

### Features

- Common forecasting interface
- Automatic evaluation
- Visualization
- Benchmark runner
- Experiment tracking
- Model registry

---

## Deep Learning Models

- LSTM
- GRU
- Seq2Seq

### Features

- Sliding-window dataset
- CUDA Support
- Early Stopping
- Model Checkpointing
- Generic Trainer
- Generic Evaluator

---

## Transformer Models

- PatchTST
- Informer
- Temporal Fusion Transformer (TFT)

### Features

- Base Transformer Framework
- Positional Encoding
- ProbSparse Attention
- Variable Selection Network
- Gated Residual Network
- Shared Trainer
- Shared Evaluator
- Transformer Benchmark

---

# 🏆 Benchmark Results

## Classical Forecasting

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| Moving Average | 5255.92 | 6660.73 | 739.72 |
| ARIMA | 5102.83 | 6626.78 | 732.71 |
| SARIMA | 5176.85 | 6580.66 | 866.94 |
| **Prophet** | **4433.22** | **5560.65** | **628.44** |

---

## Deep Learning Forecasting

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| LSTM | 5387.24 | 7125.91 | 1067.01 |
| GRU | 5550.31 | 7757.56 | 1011.50 |
| **Seq2Seq** | **5331.46** | **7111.10** | **1064.29** |

---

## Transformer Forecasting

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| PatchTST | 5576.15 | 7746.80 | 1027.00 |
| Informer | 3015.61 | 4222.57 | **940.88** |
| **Temporal Fusion Transformer (TFT)** | **2442.95** | **3731.74** | 941.51 |

**Best Transformer Model:** **Temporal Fusion Transformer (TFT)** 🏆

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
- Year-over-Year growth
- Holiday analysis
- SNAP analysis
- Store performance
- Department analysis
- Category analysis
- Prophet trend decomposition
- Prophet seasonality decomposition

---

## ✅ Milestone 3 — Production-grade Classical Forecasting

Implemented:

- Moving Average
- ARIMA
- SARIMA
- Prophet
- Unified Forecasting Framework
- Benchmark Runner
- Model Registry
- Experiment Tracking
- Prediction Storage
- Automatic Evaluation

---

## ✅ Milestone 4 — Deep Learning Forecasting

Implemented:

- LSTM
- GRU
- Seq2Seq
- Sliding-window Dataset
- CUDA / GPU Training
- Early Stopping
- Model Checkpointing
- Generic Trainer
- Generic Evaluator
- Deep Learning Benchmark

---

## ✅ Milestone 5 — Transformer Forecasting

Implemented:

- PatchTST
- Informer
- Temporal Fusion Transformer (TFT)
- Positional Encoding
- ProbSparse Attention
- Variable Selection Network
- Gated Residual Network
- Shared Transformer Framework
- Transformer Benchmark

---

# 🗺 Roadmap

| Status | Milestone |
|--------|-----------|
| ✅ | Milestone 0 — Business Understanding |
| ✅ | Milestone 1 — ETL & Data Warehouse |
| ✅ | Milestone 2 — Exploratory Data Analysis |
| ✅ | Milestone 3 — Classical Forecasting |
| ✅ | Milestone 4 — Deep Learning Forecasting |
| ✅ | Milestone 5 — Transformer Forecasting |
| 🚧 | Milestone 6 — LLM Forecast Explanations |
| ⬜ | Milestone 7 — Retrieval-Augmented Generation (RAG) |
| ⬜ | Milestone 8 — Multi-Agent AI System |
| ⬜ | Milestone 9 — FastAPI Backend |
| ⬜ | Milestone 10 — React Dashboard |
| ⬜ | Milestone 11 — Deployment & MLOps |

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

and update your database credentials.

---

## 6. Create the database schema

Execute

```text
src/database/schema.sql
```

using MySQL Workbench.

---

## 7. Run the ETL Pipeline

```bash
python -m tests.test_sales_pipeline
```

---

## 8. Run Benchmark Suites

### Classical Forecasting

```bash
python -m tests.benchmark_classical_models
```

### Deep Learning

```bash
python -m tests.benchmark_deep_learning
```

### Transformer Models

```bash
python -m tests.transformers.benchmark_transformers
```

---

# 📌 Current Status

## Current Version

# **v5.0.0**

---

## Completed

- ✅ Business Understanding
- ✅ Production ETL Framework
- ✅ MySQL Star Schema
- ✅ Business Analytics
- ✅ Exploratory Data Analysis
- ✅ Classical Forecasting Framework
- ✅ Deep Learning Forecasting Framework
- ✅ Transformer Forecasting Framework
- ✅ Unified Benchmarking
- ✅ Experiment Tracking
- ✅ Model Checkpointing
- ✅ GPU Training

---

## Current Focus

🚧 **Milestone 6 — LLM-powered Forecast Explanations**

Upcoming work includes:

- Natural Language Forecast Explanations
- Explainable AI for Forecasting
- Prompt Engineering
- LLM Integration
- Forecast Reasoning
- Business-friendly Narrative Generation

---

# 🌟 Project Highlights

## Data Engineering

- Production-grade ETL Framework
- Chunk-based Processing
- MySQL Star Schema
- Configuration-driven Pipelines

---

## Business Analytics

- SQL Analytics Layer
- Business-oriented EDA
- Prophet Trend Analysis
- Prophet Seasonality Analysis

---

## Forecasting

Implemented **10 forecasting models** across three forecasting paradigms:

### Classical Models

- Moving Average
- ARIMA
- SARIMA
- Prophet

### Deep Learning Models

- LSTM
- GRU
- Seq2Seq

### Transformer Models

- PatchTST
- Informer
- Temporal Fusion Transformer (TFT)

---

## Software Engineering

- Modular Architecture
- Reusable Components
- Shared Training Framework
- Shared Evaluation Framework
- Automatic Benchmarking
- Experiment Tracking
- Production-ready Project Structure

---

# 📊 Project Statistics

| Category | Count |
|----------|------:|
| ETL Pipelines | 5 |
| Forecasting Models | **10** |
| Benchmark Suites | 3 |
| Deep Learning Models | 3 |
| Transformer Models | 3 |
| Forecasting Paradigms | 3 |
| Dataset Size | 58M+ Records |

---

# 🎯 Next Milestone

The next milestone introduces **Large Language Models (LLMs)** into the forecasting workflow.

Planned features include:

- LLM-powered Forecast Explanations
- Business-friendly Forecast Narratives
- Explainable AI
- Prompt Templates
- Forecast Interpretation
- Executive Summary Generation

---

# 🤝 Contributing

Contributions, suggestions, improvements, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support the Project

If you found this repository useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.