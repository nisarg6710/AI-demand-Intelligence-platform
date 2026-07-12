# 📊 AI Demand Intelligence Platform

> **Production-grade AI-powered Demand Forecasting & Business Intelligence Platform**

An end-to-end project demonstrating **Data Engineering**, **Business Analytics**, **Classical Time Series Forecasting**, **Deep Learning Forecasting**, **Transformer-based Forecasting**, **LLM-powered Explainable AI**, and the roadmap toward **RAG, Multi-Agent Systems, APIs, Dashboards, and MLOps**.

---

# 🎯 Project Overview

Demand forecasting is one of the most challenging problems in retail and supply chain management. Poor forecasts lead to stockouts, overstocking, increased inventory costs, inefficient staffing, and poor logistics planning.

Instead of building a notebook-only forecasting solution, this project focuses on developing a **production-grade AI forecasting platform** with reusable software components, experiment reproducibility, benchmarking, modular architecture, and AI-generated business explanations.

## Current Capabilities

- Production ETL framework
- MySQL Star Schema warehouse
- Business analytics
- Exploratory Data Analysis (EDA)
- Classical forecasting framework
- Deep Learning forecasting framework
- Transformer forecasting framework
- LLM-powered forecast explanations
- Explainable AI reports
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

## 💬 LLM-powered Explainable AI

Implemented Features:

- Forecast Metadata Builder
- Trend Analyzer
- Seasonality Analyzer
- Statistics Analyzer
- Prompt Engineering
- Gemini Integration
- Forecast Explanation Pipeline
- Markdown Report Generation
- HTML Report Generation
- Metadata Persistence
- Prompt Persistence
- Timestamped Reports
- Structured Logging

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
LLM Forecast Explanation
(Metadata • Prompt Engineering • Gemini)
        │
        ▼
Retrieval-Augmented Generation (Upcoming)
        │
        ▼
Multi-Agent AI (Upcoming)
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

## Explainable AI

- Google Gemini
- Prompt Engineering
- Markdown
- HTML Report Generation

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
├── milestone_05_transformers/
└── milestone_06_llm/

src/
├── ai/
│   ├── llm/
│   ├── prompts/
│   ├── metadata.py
│   ├── pipeline.py
│   ├── report.py
│   └── html_report.py
│
├── analytics/
├── database/
├── etl/
├── forecasting/
│   ├── classical/
│   ├── deep_learning/
│   └── transformers/
└── utils/

artifacts/
├── benchmarks/
├── metadata/
├── models/
├── prompts/
└── reports/
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

## 💬 LLM Forecast Explanation Framework

### Features

- Forecast Metadata Builder
- Trend Analysis
- Seasonality Analysis
- Statistics Analysis
- Prompt Builder
- Gemini Integration
- Forecast Explanation Pipeline
- Markdown Report Generation
- HTML Report Generation
- Metadata & Prompt Persistence
- Timestamped Report Generation
- Structured Logging

---

# 🏆 Benchmark Results

*(Keep all benchmark tables exactly as they are.)*

---

# 🚀 Completed Milestones

- ✅ Milestone 0 — Business Understanding
- ✅ Milestone 1 — ETL & Data Warehouse
- ✅ Milestone 2 — Exploratory Data Analysis
- ✅ Milestone 3 — Classical Forecasting
- ✅ Milestone 4 — Deep Learning Forecasting
- ✅ Milestone 5 — Transformer Forecasting
- ✅ Milestone 6 — LLM-powered Forecast Explanations

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
| ✅ | Milestone 6 — LLM Forecast Explanations |
| 🚧 | Milestone 7 — Retrieval-Augmented Generation (RAG) |
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

## 6. Configure Gemini API

Create

```text
configs/llm.yaml
```

and add your Gemini API configuration.

Example:

```yaml
provider: gemini

model: gemini-3.5-flash

api_key: YOUR_API_KEY
```

---

## 7. Create the database schema

Execute

```text
src/database/schema.sql
```

using MySQL Workbench.

---

## 8. Run the ETL Pipeline

```bash
python -m tests.test_sales_pipeline
```

---

## 9. Run Benchmark Suites

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

## 10. Generate an AI Forecast Explanation

```bash
python -m tests.llm.test_pipeline
```

This automatically:

- Builds forecast metadata
- Generates structured prompts
- Calls Gemini
- Produces a business explanation
- Saves Markdown report
- Saves HTML report
- Persists prompts and metadata
- Logs the execution

---

# 📌 Current Status

## Current Version

# **v6.0.0**

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
- ✅ LLM-powered Forecast Explanations
- ✅ Explainable AI Pipeline
- ✅ Unified Benchmarking
- ✅ Experiment Tracking
- ✅ Model Checkpointing
- ✅ GPU Training
- ✅ Automatic Markdown & HTML Report Generation

---

## Current Focus

🚧 **Milestone 7 — Retrieval-Augmented Generation (RAG)**

Upcoming work includes:

- Vector Database
- Document Chunking
- Embedding Generation
- Semantic Search
- Retrieval Pipeline
- Context-aware Forecast Explanations
- Hybrid AI Reasoning

---

# 🌟 Project Highlights

## 📦 Data Engineering

- Production-grade ETL Framework
- Chunk-based Processing
- MySQL Star Schema
- Configuration-driven Pipelines

---

## 📊 Business Analytics

- SQL Analytics Layer
- Business-oriented EDA
- Prophet Trend Analysis
- Prophet Seasonality Analysis

---

## 📈 Forecasting

Implemented **10 forecasting models** across three forecasting paradigms.

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

## 💬 Explainable AI

- Forecast Metadata Extraction
- Trend Analysis
- Seasonality Detection
- Statistical Analysis
- Prompt Engineering
- Gemini Integration
- AI-generated Business Explanations
- Markdown Reports
- HTML Reports
- Timestamped Artifact Generation

---

## 🏗 Software Engineering

- Modular Architecture
- Reusable Components
- Shared Training Framework
- Shared Evaluation Framework
- Shared Explanation Pipeline
- Automatic Benchmarking
- Experiment Tracking
- Timestamped Artifacts
- Structured Logging
- Production-ready Project Structure

---

# 📊 Project Statistics

| Category | Count |
|----------|------:|
| ETL Pipelines | 5 |
| Forecasting Models | **10** |
| Forecasting Paradigms | **3** |
| Benchmark Suites | **3** |
| Deep Learning Models | 3 |
| Transformer Models | 3 |
| LLM Pipeline | **1** |
| AI Report Formats | **2** |
| Dataset Size | **58M+ Records** |

---

# 🎯 Next Milestone

The next milestone introduces **Retrieval-Augmented Generation (RAG)** into the forecasting platform.

Planned features include:

- Document Ingestion
- Business Knowledge Base
- Embedding Generation
- Vector Database
- Semantic Retrieval
- Context-aware Prompt Construction
- Retrieval-Augmented Forecast Explanations
- Source Attribution
- Knowledge-enhanced Business Reports

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