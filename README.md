# 📊 AI Demand Intelligence Platform

> **Production-grade AI-powered Demand Forecasting & Business
> Intelligence Platform**

An end-to-end project demonstrating **Data Engineering**, **Business
Analytics**, **Classical Time Series Forecasting**, **Deep Learning
Forecasting**, and the roadmap toward **Transformer Models, LLMs, RAG,
Multi-Agent Systems, APIs, Dashboards, and MLOps**.

------------------------------------------------------------------------

# 🎯 Project Overview

Demand forecasting is a critical retail and supply-chain problem. This
project builds a production-oriented forecasting platform rather than a
notebook-only solution.

## Current Capabilities

-   Production ETL framework
-   MySQL Star Schema warehouse
-   Business analytics
-   Exploratory data analysis
-   Classical forecasting framework
-   Deep learning forecasting framework
-   Experiment tracking
-   Benchmarking

------------------------------------------------------------------------

# ⭐ Features

## Data Engineering

-   Generic ETL framework
-   Chunk-based processing
-   Configuration-driven pipelines
-   MySQL data warehouse

## Analytics

-   SQL analytics layer
-   Business-oriented EDA
-   Prophet decomposition

## Classical Forecasting

-   Moving Average
-   ARIMA
-   SARIMA
-   Prophet
-   Unified forecasting pipeline
-   Benchmarking
-   Experiment tracking

## Deep Learning

-   LSTM
-   GRU
-   Seq2Seq
-   GPU Training (CUDA)
-   Early Stopping
-   Model Checkpointing
-   Generic Trainer
-   Generic Evaluator

------------------------------------------------------------------------

# 🏗 System Architecture

``` text
Raw Retail Data
      │
      ▼
ETL Pipeline
      │
      ▼
MySQL Star Schema
      │
      ▼
Analytics & EDA
      │
      ▼
Classical Forecasting
(MA • ARIMA • SARIMA • Prophet)
      │
      ▼
Deep Learning
(LSTM • GRU • Seq2Seq)
      │
      ▼
Transformer Models (Upcoming)
      │
      ▼
LLM + RAG + Multi-Agent AI
      │
      ▼
FastAPI
      │
      ▼
React Dashboard
```

------------------------------------------------------------------------

# 🛠 Tech Stack

-   Python 3.12
-   Pandas
-   NumPy
-   MySQL
-   Statsmodels
-   pmdarima
-   Prophet
-   PyTorch
-   Matplotlib
-   Seaborn

Upcoming: - XGBoost - LightGBM - LangChain - FAISS - FastAPI - React -
Docker - GitHub Actions

------------------------------------------------------------------------

# 📂 Project Structure

``` text
docs/
├── business_case/
├── milestone_01_etl/
├── milestone_02_eda/
├── milestone_03_forecasting/
└── milestone_04_deep_learning/

src/
├── analytics/
├── database/
├── etl/
├── forecasting/
│   ├── classical/
│   └── deep_learning/
└── utils/

artifacts/
├── models/
├── benchmarks/
└── plots/
```

------------------------------------------------------------------------

# 📦 Dataset

**M5 Forecasting -- Accuracy**

Datasets: - Calendar - Sell Prices - Sales History

------------------------------------------------------------------------

# ⚙ ETL Pipeline

Extraction → Validation → Transformation → Loading → MySQL Warehouse

Features: - Generic CSV extractor - Validation - Chunk processing -
Batch loading - Execution metrics

------------------------------------------------------------------------

# 🗄 Data Warehouse

## Dimension Tables

-   calendar_dim
-   item_dim
-   store_dim

## Fact Tables

-   sales_fact
-   price_fact

## Analytics

-   sales_enriched

## Forecasting

-   forecast_experiments
-   forecast_predictions

------------------------------------------------------------------------

# 📊 Exploratory Data Analysis

Completed:

-   Daily demand trends
-   Weekly & monthly seasonality
-   YoY growth
-   Holiday impact
-   SNAP impact
-   Store, department and category analysis
-   Prophet trend & seasonality decomposition

------------------------------------------------------------------------

# 📈 Forecasting Framework

## Classical Models

-   Moving Average
-   ARIMA
-   SARIMA
-   Prophet

Framework Features:

-   Common interface
-   Automatic evaluation
-   Benchmark runner
-   Visualization
-   Model registry
-   Experiment tracking

## Deep Learning Models

-   LSTM
-   GRU
-   Seq2Seq

Framework Features:

-   Sliding-window dataset
-   CUDA support
-   Early stopping
-   Checkpointing
-   Generic trainer
-   Generic evaluator
-   Deep learning benchmark

------------------------------------------------------------------------

# 🏆 Benchmark Results

## Classical Models

  Model                      MAE          RMSE         MAPE
  ---------------- ------------- ------------- ------------
  Moving Average         5255.92       6660.73       739.72
  ARIMA                  5102.83       6626.78       732.71
  SARIMA                 5176.85       6580.66       866.94
  **Prophet**        **4433.22**   **5560.65**   **628.44**

## Deep Learning Models

  Model                   MAE          RMSE          MAPE
  ------------- ------------- ------------- -------------
  LSTM                5387.24       7125.91       1067.01
  GRU                 5550.31       7757.56       1011.50
  **Seq2Seq**     **5331.46**   **7111.10**   **1064.29**

------------------------------------------------------------------------

# 🚀 Completed Milestones

-   ✅ Milestone 0 --- Business Understanding
-   ✅ Milestone 1 --- ETL & Data Warehouse
-   ✅ Milestone 2 --- Exploratory Data Analysis
-   ✅ Milestone 3 --- Production-grade Classical Forecasting
-   ✅ Milestone 4 --- Deep Learning Forecasting

------------------------------------------------------------------------

# 🗺 Roadmap

  Status   Milestone
  -------- ---------------------------
  ✅       Business Understanding
  ✅       ETL & Data Warehouse
  ✅       Exploratory Data Analysis
  ✅       Classical Forecasting
  ✅       Deep Learning Forecasting
  🚧       Transformer Forecasting
  ⬜       LLM Forecast Explanations
  ⬜       RAG
  ⬜       Multi-Agent AI
  ⬜       FastAPI
  ⬜       React Dashboard
  ⬜       Deployment & MLOps

------------------------------------------------------------------------

# 🚀 Getting Started

``` bash
git clone <repository-url>
cd AI-demand-intelligence-platform

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Configure `configs/database.yaml`, create the schema from
`src/database/schema.sql`, then run:

``` bash
python -m tests.test_sales_pipeline
python -m tests.benchmark_classical_models
python -m tests.benchmark_deep_learning
```

------------------------------------------------------------------------

# 📌 Current Status

**Version:** **v4.0.0**

Completed:

-   ETL Framework
-   MySQL Star Schema
-   EDA
-   Classical Forecasting
-   Deep Learning Forecasting
-   Benchmarking
-   Experiment Tracking

**Current Focus:** 🚧 Milestone 5 --- Transformer Forecasting

Planned: - PatchTST - Informer - Temporal Fusion Transformer (TFT)

------------------------------------------------------------------------

# 🌟 Project Highlights

-   Production-ready architecture
-   58M+ row retail warehouse
-   Reusable forecasting framework
-   Multiple benchmarked forecasting models
-   Modular deep learning pipeline
-   Strong software engineering practices

------------------------------------------------------------------------

# 🤝 Contributing

Contributions, suggestions, improvements, and feature requests are
welcome.

------------------------------------------------------------------------

# 📄 License

MIT License
