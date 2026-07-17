# 📊 AI Demand Intelligence Platform

> **Production-grade AI-powered Demand Forecasting, Explainable AI & Retrieval-Augmented Business Intelligence Platform**

An end-to-end project demonstrating **Data Engineering**, **Business Analytics**, **Classical Time Series Forecasting**, **Deep Learning Forecasting**, **Transformer-based Forecasting**, **LLM-powered Explainable AI**, **Retrieval-Augmented Generation (RAG)**, and the roadmap toward **Multi-Agent AI Systems, FastAPI APIs, Interactive Dashboards, and MLOps**.

---

# 🎯 Project Overview

Demand forecasting is one of the most challenging problems in retail and supply chain management. Poor forecasts lead to stockouts, overstocking, increased inventory costs, inefficient staffing, poor logistics planning, and ultimately reduced business profitability.

Rather than building a notebook-only forecasting solution, this project focuses on developing a **production-grade AI Demand Intelligence Platform** with reusable software components, modular architecture, experiment reproducibility, benchmarking, explainable AI, semantic knowledge retrieval, and production-ready software engineering practices.

The platform evolves through multiple milestones, gradually transforming from a traditional forecasting system into a complete AI-powered business intelligence solution capable of answering business questions using historical reports, inventory policies, and domain knowledge.

## Current Capabilities

- Production ETL Framework
- MySQL Star Schema Data Warehouse
- Business Analytics
- Exploratory Data Analysis (EDA)
- Classical Forecasting Framework
- Deep Learning Forecasting Framework
- Transformer Forecasting Framework
- LLM-powered Forecast Explanations
- Retrieval-Augmented Generation (RAG)
- Interactive AI Business Assistant
- Explainable AI Reports
- Semantic Document Search
- Vector Database Indexing
- Experiment Tracking
- Model Checkpointing
- Unified Benchmarking

---

# ⭐ Features

## 📦 Data Engineering

- Generic ETL Framework
- Chunk-based Processing
- Configuration-driven Pipelines
- MySQL Star Schema Warehouse
- Data Validation Framework
- Batch Processing
- Execution Metrics
- Modular Pipeline Architecture

---

## 📊 Business Analytics

- SQL Analytics Layer
- Business-oriented EDA
- Prophet Trend Decomposition
- Prophet Seasonality Decomposition
- Trend Analysis
- Seasonality Analysis
- Business KPI Exploration

---

## 📈 Classical Forecasting

### Implemented Models

- Moving Average
- ARIMA
- SARIMA
- Prophet

### Framework Features

- Common Forecasting Interface
- Automatic Evaluation
- Benchmark Runner
- Model Registry
- Experiment Tracking
- Automatic Visualization
- Forecast Persistence

---

## 🧠 Deep Learning Forecasting

### Implemented Models

- LSTM
- GRU
- Seq2Seq

### Framework Features

- Sliding-window Dataset Generation
- CUDA / GPU Training
- Early Stopping
- Model Checkpointing
- Generic Trainer
- Generic Evaluator
- Deep Learning Benchmark
- Shared Training Pipeline

---

## 🤖 Transformer Forecasting

### Implemented Models

- PatchTST
- Informer (ProbSparse Attention)
- Temporal Fusion Transformer (TFT)

### Framework Features

- Base Transformer Abstraction
- Positional Encoding
- ProbSparse Attention
- Variable Selection Network
- Gated Residual Network
- Shared Training Pipeline
- Shared Evaluation Pipeline
- Transformer Benchmark
- Model Checkpointing

---

## 💬 LLM-powered Explainable AI

### Implemented Features

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

## 📚 Retrieval-Augmented Generation (RAG)

### Implemented Components

- Knowledge Base Management
- Markdown Document Loader
- Recursive Document Processing
- Intelligent Text Chunking
- SentenceTransformer Embeddings
- FAISS Vector Database
- Semantic Similarity Search
- Top-K Document Retrieval
- Context Builder
- RAG Prompt Engineering
- Gemini-powered Grounded Responses
- Source Attribution
- Interactive Business Q&A Assistant

---

# 🏗 System Architecture

```text
                         Raw Retail Data
                                │
                                ▼
                     Production ETL Pipeline
                                │
                                ▼
                 MySQL Star Schema Warehouse
                                │
                                ▼
               Analytics & Business Intelligence
                                │
                                ▼
                 Exploratory Data Analysis (EDA)
                                │
                                ▼
             Classical Forecasting Models
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
        LLM-powered Forecast Explanation
     (Metadata • Prompt Engineering • Gemini)
                                │
                                ▼
     Retrieval-Augmented Generation (RAG)
(Document Loader • Embeddings • FAISS • Retrieval)
                                │
                                ▼
      Interactive AI Business Assistant
                                │
                                ▼
        Multi-Agent AI System (Upcoming)
                                │
                                ▼
             FastAPI Backend (Upcoming)
                                │
                                ▼
          React Dashboard (Upcoming)
                                │
                                ▼
      Production Deployment & MLOps
```

---

# 🛠 Tech Stack

## Programming

- Python 3.12

---

## Data Engineering

- Pandas
- NumPy
- MySQL

---

## Time Series Forecasting

- Statsmodels
- pmdarima
- Prophet

---

## Deep Learning

- PyTorch
- CUDA

---

## Explainable AI

- Google Gemini
- Prompt Engineering
- Markdown Report Generation
- HTML Report Generation

---

## Retrieval-Augmented Generation

- SentenceTransformers
- all-MiniLM-L6-v2
- FAISS
- Semantic Search
- Vector Embeddings

---

## Data Visualization

- Matplotlib
- Seaborn

---

## Upcoming Technologies

- LangChain
- FastAPI
- React
- Docker
- GitHub Actions
- MLflow
- DVC

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
├── milestone_06_llm/
└── milestone_07_rag/

src/
├── ai/
│   ├── llm/
│   ├── prompts/
│   ├── rag/
│   │   ├── document_loader.py
│   │   ├── text_chunker.py
│   │   ├── embedding_generator.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── context_builder.py
│   │   └── pipeline.py
│   │
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

data/
└── knowledge_base/
    ├── forecast_reports/
    ├── inventory_policies/
    └── retail_reports/

artifacts/
├── benchmarks/
├── faiss/
├── metadata/
├── models/
├── prompts/
└── reports/
```

---
# 📦 Dataset

This project uses the **M5 Forecasting – Accuracy** dataset, one of the most widely used public benchmarks for large-scale retail demand forecasting.

### Datasets Used

- Calendar
- Sell Prices
- Sales History

### Future Data Sources

To further improve forecasting performance and business insights, future milestones may incorporate:

- Weather Data
- Promotional Events
- Holiday Calendars
- Economic Indicators
- Store-level Metadata
- Competitor Pricing
- External Market Signals

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
MySQL Star Schema Warehouse
```

### Features

- Generic CSV Extractor
- Data Validation Framework
- Batch Loading
- Chunk-based Processing
- Configuration-driven Pipelines
- Execution Metrics
- Error Handling
- Logging
- Reusable ETL Components

---

# 🗄 Data Warehouse

## Dimension Tables

- calendar_dim
- item_dim
- store_dim

---

## Fact Tables

- sales_fact
- price_fact

---

## Analytics Views

- sales_enriched

---

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
- Business Trend Analysis
- Demand Pattern Identification

---

# 📈 Forecasting Framework

The forecasting framework is designed around reusable abstractions, allowing different forecasting paradigms to share common evaluation, benchmarking, and experiment tracking pipelines.

---

## Classical Forecasting Models

Implemented Models

- Moving Average
- ARIMA
- SARIMA
- Prophet

### Features

- Common Forecasting Interface
- Automatic Evaluation
- Visualization
- Benchmark Runner
- Experiment Tracking
- Model Registry
- Forecast Persistence

---

## Deep Learning Models

Implemented Models

- LSTM
- GRU
- Seq2Seq

### Features

- Sliding-window Dataset Generation
- CUDA Support
- Early Stopping
- Model Checkpointing
- Generic Trainer
- Generic Evaluator
- Deep Learning Benchmark
- Shared Training Framework

---

## Transformer Models

Implemented Models

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
- Model Checkpointing

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
- Metadata Persistence
- Prompt Persistence
- Timestamped Report Generation
- Structured Logging

---

## 📚 Retrieval-Augmented Generation (RAG)

### Knowledge Base

The AI assistant retrieves information from:

- Forecast Reports
- Inventory Policies
- Retail Market Reports

### Pipeline Components

- Document Loader
- Intelligent Text Chunking
- SentenceTransformer Embeddings
- FAISS Vector Store
- Semantic Retrieval
- Context Builder
- RAG Prompt Builder
- Gemini-powered Answer Generation
- Source Attribution

### Interactive Features

- Business Question Answering
- Knowledge-grounded Responses
- Semantic Document Search
- AI-powered Business Assistant

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
- ✅ Milestone 7 — Retrieval-Augmented Generation (RAG)

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
| ✅ | Milestone 7 — Retrieval-Augmented Generation (RAG) |
| 🚧 | Milestone 8 — Multi-Agent AI System |
| ⬜ | Milestone 9 — FastAPI Backend |
| ⬜ | Milestone 10 — React Dashboard |
| ⬜ | Milestone 11 — Deployment & MLOps |

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-demand-intelligence-platform
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

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

model: gemini-3.1-flash-lite

api_key: YOUR_API_KEY
```

---

## 7. Create the Database Schema

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

- Builds Forecast Metadata
- Generates Structured Prompts
- Calls Gemini
- Produces Business Explanations
- Saves Markdown Reports
- Saves HTML Reports
- Persists Metadata & Prompts
- Logs Execution

---

## 11. Run the RAG Business Assistant

```bash
python -m tests.rag.rag_assistant
```

Example questions:

- Have we seen this demand pattern before?
- Which inventory policy applies?
- What does the retail report recommend?
- Should safety stock be increased?
- How should increasing demand be handled?

The assistant retrieves relevant business documents using semantic search before generating grounded AI responses with source attribution.

---
# 📌 Current Status

## Current Version

# **v7.0.0**

---

## Completed

- ✅ Business Understanding
- ✅ Production ETL Framework
- ✅ MySQL Star Schema Warehouse
- ✅ Business Analytics
- ✅ Exploratory Data Analysis
- ✅ Classical Forecasting Framework
- ✅ Deep Learning Forecasting Framework
- ✅ Transformer Forecasting Framework
- ✅ LLM-powered Forecast Explanations
- ✅ Explainable AI Pipeline
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ AI Business Knowledge Base
- ✅ Semantic Document Search
- ✅ FAISS Vector Database
- ✅ Interactive Business Assistant
- ✅ Unified Benchmarking
- ✅ Experiment Tracking
- ✅ Model Checkpointing
- ✅ GPU Training
- ✅ Automatic Markdown & HTML Report Generation

---

## Current Focus

🚧 **Milestone 8 — Multi-Agent AI System**

Upcoming work includes:

- Forecast Analyst Agent
- Inventory Advisor Agent
- Business Intelligence Agent
- Report Generation Agent
- Agent Orchestrator
- Agent Communication
- Tool Calling
- Multi-Agent Decision Making

---

# 🌟 Project Highlights

## 📦 Data Engineering

- Production-grade ETL Framework
- Chunk-based Processing
- Configuration-driven Pipelines
- MySQL Star Schema Warehouse
- Modular ETL Components
- Data Validation Framework

---

## 📊 Business Analytics

- SQL Analytics Layer
- Business-oriented EDA
- Trend Analysis
- Seasonality Analysis
- Prophet Decomposition
- Business KPI Exploration

---

## 📈 Forecasting

Implemented **10 forecasting models** across **three forecasting paradigms**.

### Classical Forecasting

- Moving Average
- ARIMA
- SARIMA
- Prophet

### Deep Learning

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

## 📚 Retrieval-Augmented Generation

- Business Knowledge Base
- Recursive Document Loader
- Intelligent Text Chunking
- SentenceTransformer Embeddings
- FAISS Vector Database
- Semantic Similarity Search
- Top-K Document Retrieval
- Context Builder
- RAG Prompt Engineering
- Source-aware AI Responses
- Interactive Business Q&A Assistant

---

## 🏗 Software Engineering

- Modular Architecture
- Reusable Components
- Shared Training Framework
- Shared Evaluation Framework
- Shared Explanation Pipeline
- Shared Retrieval Pipeline
- Automatic Benchmarking
- Experiment Tracking
- Timestamped Artifacts
- Structured Logging
- Production-ready Project Structure

---

# 📊 Project Statistics

| Category | Count |
|----------|------:|
| ETL Pipelines | **5** |
| Forecasting Models | **10** |
| Forecasting Paradigms | **3** |
| Benchmark Suites | **3** |
| Deep Learning Models | **3** |
| Transformer Models | **3** |
| LLM Pipelines | **2** |
| AI Report Formats | **2** |
| Knowledge Base Categories | **3** |
| Vector Database | **1** |
| Interactive AI Assistant | **1** |
| Dataset Size | **58M+ Records** |

---

# 🎯 Next Milestone

The next milestone introduces a **Multi-Agent AI System** that transforms the platform from a single AI assistant into a collaborative team of specialized AI agents.

Planned capabilities include:

- Forecast Analyst Agent
- Inventory Advisor Agent
- Business Intelligence Agent
- Report Generation Agent
- Agent Orchestrator
- Tool Calling
- Shared Memory
- Multi-Agent Collaboration
- Autonomous Business Reasoning
- End-to-end Decision Support

This milestone will move the platform beyond Retrieval-Augmented Generation and toward an enterprise-grade AI decision support system capable of coordinating multiple specialized agents.

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

# ⭐ Support the Project

If you found this repository useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---


> **AI Demand Intelligence Platform** is an end-to-end production-oriented project demonstrating the complete evolution of a modern AI application—from data engineering and forecasting to explainable AI, semantic retrieval, and the future of collaborative multi-agent business intelligence.