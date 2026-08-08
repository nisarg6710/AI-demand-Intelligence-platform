# 📊 AI Demand Intelligence Platform

> **Production-grade AI-powered Demand Forecasting, Explainable AI, Retrieval-Augmented Generation, and Multi-Agent Business Intelligence Platform**

An end-to-end production-oriented AI system demonstrating **Data Engineering**, **Business Analytics**, **Classical Time Series Forecasting**, **Deep Learning Forecasting**, **Transformer-based Forecasting**, **LLM-powered Explainable AI**, **Retrieval-Augmented Generation (RAG)**, and **Multi-Agent AI Systems**.

The platform progressively evolves from a traditional retail forecasting pipeline into an intelligent business decision-support system capable of answering natural-language questions using real business data, forecasting models, analytics tools, inventory intelligence, SQL, domain knowledge, and coordinated AI agents.

---

# 🎯 Project Overview

Demand forecasting is one of the most challenging problems in modern retail and supply-chain management.

Poor demand forecasts can result in:

- Stockouts
- Overstocking
- Excess inventory costs
- Inefficient replenishment
- Poor staffing decisions
- Inefficient logistics
- Lost sales
- Reduced customer satisfaction
- Lower profitability

Instead of building a notebook-only forecasting project, this project focuses on developing a **production-oriented AI Demand Intelligence Platform** with:

- Modular software architecture
- Reusable data pipelines
- MySQL data warehousing
- Business analytics
- Multiple forecasting paradigms
- Model benchmarking
- Experiment tracking
- Explainable AI
- LLM integration
- Retrieval-Augmented Generation
- Semantic search
- Vector databases
- Tool-based AI agents
- Multi-agent orchestration
- Natural-language business querying

The project is developed incrementally through a series of milestones, with each milestone adding another layer of capability to the platform.

---

# 🚀 Current Capabilities

The platform currently includes:

- Production ETL Framework
- Chunk-based ETL Processing
- MySQL Star Schema Data Warehouse
- Business Analytics
- Exploratory Data Analysis
- Classical Forecasting
- Deep Learning Forecasting
- Transformer-based Forecasting
- Forecast Benchmarking
- Experiment Tracking
- Model Checkpointing
- LLM-powered Forecast Explanations
- Explainable AI Reports
- Markdown Report Generation
- HTML Report Generation
- Retrieval-Augmented Generation
- Semantic Document Search
- FAISS Vector Database
- Knowledge Base Management
- Gemini-powered AI Responses
- Business Question Answering
- Forecast Agent
- Analytics Agent
- Inventory Agent
- SQL Agent
- Executive Agent
- Deterministic Task Routing
- Agent Orchestration
- Tool-based Agent Execution
- Natural-language Query Engine
- Multi-agent Executive Reporting

---

# ⭐ Features

## 📦 Data Engineering

The data engineering layer provides the foundation for the entire platform.

### Implemented Features

- Generic ETL Framework
- Configuration-driven Pipelines
- Chunk-based Processing
- CSV Extraction
- Data Validation
- Data Transformation
- Batch Loading
- MySQL Integration
- Star Schema Warehouse
- Execution Metrics
- Error Handling
- Structured Logging
- Reusable ETL Components

The ETL architecture follows:

```text
Raw Data
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

📊 Business Analytics

The analytics layer provides business-oriented insights from the retail data warehouse.

Implemented Capabilities
Sales Summary
Monthly Sales Analysis
Weekday Sales Analysis
Store Performance
Product Performance
Category Performance
Department Performance
Price Analysis
Sales Distribution
Trend Analysis
Seasonality Analysis
Business KPI Analysis
Historical Demand Analysis

The analytics layer is designed to convert raw warehouse data into decision-support information.

📈 Classical Forecasting

The classical forecasting framework provides a common architecture for traditional time-series forecasting models.

Implemented Models
Moving Average
ARIMA
SARIMA
Prophet
Framework Features
Common Forecasting Interface
Automatic Evaluation
Forecast Persistence
Benchmark Runner
Model Registry
Experiment Tracking
Forecast Visualization
Evaluation Metrics
Reusable Training Pipeline
🧠 Deep Learning Forecasting

The deep learning forecasting framework extends the platform beyond traditional statistical forecasting.

Implemented Models
LSTM
GRU
Seq2Seq
Framework Features
Sliding-window Dataset Generation
PyTorch-based Training
CUDA / GPU Support
Early Stopping
Model Checkpointing
Generic Trainer
Generic Evaluator
Deep Learning Benchmarking
Shared Training Pipeline
Reusable Evaluation Pipeline
🤖 Transformer Forecasting

The transformer forecasting layer introduces modern sequence-modeling architectures.

Implemented Models
PatchTST
Informer
Temporal Fusion Transformer (TFT)
Framework Features
Base Transformer Abstraction
Positional Encoding
ProbSparse Attention
Variable Selection Network
Gated Residual Network
Shared Training Pipeline
Shared Evaluation Pipeline
Transformer Benchmarking
Model Checkpointing
💬 LLM-powered Explainable AI

The platform uses Large Language Models to convert forecasting outputs and statistical results into understandable business explanations.

Implemented Components
Forecast Metadata Builder
Trend Analyzer
Seasonality Analyzer
Statistical Analysis
Prompt Engineering
Gemini Integration
Forecast Explanation Pipeline
Markdown Report Generation
HTML Report Generation
Metadata Persistence
Prompt Persistence
Timestamped Reports
Structured Logging

The architecture follows:

Forecast Results
      │
      ▼
Forecast Metadata
      │
      ▼
Trend / Seasonality / Statistics
      │
      ▼
Prompt Builder
      │
      ▼
Gemini
      │
      ▼
Business Explanation
      │
      ├── Markdown Report
      └── HTML Report
📚 Retrieval-Augmented Generation (RAG)

The RAG layer provides grounded AI responses using a domain-specific business knowledge base.

Knowledge Sources

The knowledge base can contain:

Forecast Reports
Inventory Policies
Retail Reports
Business Documentation
Domain Knowledge
Implemented Components
Knowledge Base Management
Markdown Document Loader
Recursive Document Processing
Intelligent Text Chunking
SentenceTransformer Embeddings
FAISS Vector Database
Semantic Similarity Search
Top-K Retrieval
Context Builder
RAG Prompt Engineering
Gemini-powered Grounded Responses
Source Attribution
Interactive Business Q&A

The RAG architecture:

Business Documents
       │
       ▼
Document Loader
       │
       ▼
Text Chunking
       │
       ▼
Embeddings
       │
       ▼
FAISS Vector Store
       │
       ▼
Semantic Retrieval
       │
       ▼
Relevant Context
       │
       ▼
Gemini
       │
       ▼
Grounded Business Answer
🤖 Multi-Agent AI Intelligence

Milestone 9 introduces the platform's Multi-Agent AI Intelligence Layer.

The objective is to allow users to interact with the entire platform through natural-language business questions.

Instead of requiring users to manually select:

forecasting models
analytics functions
inventory reports
SQL queries

the system automatically determines which specialist agent should handle the request.

🧩 Specialist Agents

The current multi-agent system contains five major agent components.

1. Forecast Agent

Responsible for:

Forecast model selection
Model comparison
Demand predictions
Forecasting experiments
Forecast interpretation
Forecast metrics
2. Analytics Agent

Responsible for:

Sales summaries
Monthly sales trends
Weekday sales
Store performance
Product performance
Category performance
Department performance
Price statistics
Sales distributions
Business KPI analysis
3. Inventory Agent

Responsible for:

Inventory summaries
Fast-moving products
Slow-moving products
Inventory health
Reorder candidates
Store-level inventory intelligence
Replenishment insights
4. SQL Agent

Responsible for:

Natural-language-to-SQL generation
Database questions
Table selection
SQL joins
Aggregations
Query execution
SQL result interpretation

The SQL Agent uses the warehouse schema through a schema cache before generating SQL.

5. Executive Agent

The Executive Agent acts as the final business communication layer.

It combines specialist findings and produces:

Executive Summary
Key Findings
Business Risks
Recommendations
Next Steps

The Executive Agent is particularly useful when a business question requires insights from multiple domains.

🔀 Intelligent Task Routing

The platform contains a deterministic TaskRouter responsible for selecting the appropriate specialist agents.

Example:

"What is the best forecasting model?"
             │
             ▼
         TaskRouter
             │
             ▼
        Forecast Agent

Another example:

"Give me an executive report."
             │
             ▼
         TaskRouter
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
   Forecast Analytics Inventory
       │     │     │
       └─────┼─────┘
             ▼
      Executive Agent
             │
             ▼
      Executive Report
🔎 Supported Query Types

The current query system supports multiple categories of business questions.

Query Type	Example	Agent
Forecasting	What is the best forecasting model?	Forecast
Inventory	Which products are selling the fastest?	Inventory
Analytics	Show me the monthly sales trend.	Analytics
SQL	Show me the SQL query for monthly sales.	SQL
Executive	Give me an executive report.	Forecast + Analytics + Inventory
🏗️ Multi-Agent Architecture

The complete AI intelligence architecture is:

                         User
                          │
                          ▼
                Natural Language Query
                          │
                          ▼
                    Query Engine
                          │
                          ▼
                     Task Router
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   Forecast Agent   Analytics Agent   Inventory Agent
        │                 │                 │
        ▼                 ▼                 ▼
 Forecast Tool       Analytics Tool    Inventory Tool
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
                     Real Results
                          │
                          ▼
                  LLM Interpretation
                          │
                          ▼
                    Final Response

For multi-domain questions:

                         User
                          │
                          ▼
                    Task Router
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
         Forecast      Analytics    Inventory
           Agent         Agent         Agent
             │            │            │
             └────────────┼────────────┘
                          │
                          ▼
                   Executive Agent
                          │
                          ▼
                  Executive Report
🔄 Query Engine

The Query Engine provides a unified interface for interacting with the AI system.

Instead of interacting directly with individual agents, the application can call a single query interface.

Conceptually:

from src.ai.query.query_engine import QueryEngine

engine = QueryEngine()

result = engine.ask(
    "Which products are selling the fastest?"
)

The Query Engine handles:

Question validation
Agent orchestration
Query execution
Result formatting
Error handling

This creates a clean separation between the application layer and the internal AI agent architecture.

🛠️ Agent Tool Architecture

The platform follows a tool-grounded architecture.

Instead of allowing the LLM to invent business results, specialist agents select appropriate tools and retrieve actual data.

The general pattern is:

Natural Language Question
          │
          ▼
        Agent
          │
          ▼
     Tool Selection
          │
          ▼
     Tool Execution
          │
          ▼
     Real Data / Model
          │
          ▼
    LLM Interpretation
          │
          ▼
     Business Answer

This separation improves:

Reliability
Debuggability
Reproducibility
Modularity
Observability
Maintainability
🧠 Agent Responsibilities
Component	Responsibility
TaskRouter	Determines which agents should execute
ForecastAgent	Forecasting intelligence
AnalyticsAgent	Historical business analytics
InventoryAgent	Inventory intelligence
SQLAgent	Database and SQL intelligence
ExecutiveAgent	Cross-domain business synthesis
AgentOrchestrator	Coordinates specialist execution
QueryEngine	Provides unified application interface
🗄️ Data Warehouse

The platform uses a MySQL star-schema architecture.

Dimension Tables
calendar_dim
item_dim
store_dim
Fact Tables
sales_fact
price_fact
Analytics Views
sales_enriched
Forecasting Tables
forecast_experiments
forecast_predictions

The warehouse provides a centralized source of truth for analytics, SQL queries, inventory intelligence, and AI agents.

📊 Exploratory Data Analysis

Completed analyses include:

Daily Demand Trends
Weekly Seasonality
Monthly Seasonality
Year-over-Year Growth
Holiday Impact
SNAP Impact
Store Performance
Department Performance
Category Performance
Prophet Trend Decomposition
Prophet Seasonality Decomposition
Business Trend Analysis
Demand Pattern Identification
📦 Dataset

This project primarily uses the M5 Forecasting – Accuracy dataset.

The M5 dataset provides a large-scale retail demand forecasting benchmark containing hierarchical sales information across:

Products
Stores
Departments
Categories
Calendar dates
Prices
Datasets Used
Sales History
Calendar
Sell Prices
Future Data Sources

Future iterations may incorporate additional external signals such as:

Weather Data
Promotional Events
Holiday Calendars
Economic Indicators
Store-level Metadata
Competitor Pricing
External Market Signals
⚙️ ETL Pipeline

The ETL system follows a production-oriented architecture:

                Raw CSV Data
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
              MySQL Warehouse
ETL Features
Generic CSV Extractor
Data Validation Framework
Batch Loading
Chunk-based Processing
Configuration-driven Pipelines
Execution Metrics
Error Handling
Structured Logging
Reusable ETL Components
MySQL Integration

# 📈 Forecasting Framework

The forecasting framework is designed around reusable abstractions so that different forecasting paradigms can share common training, evaluation, benchmarking, and persistence infrastructure.

---

## Classical Forecasting Models

### Implemented Models

- Moving Average
- ARIMA
- SARIMA
- Prophet

### Framework Features

- Common Forecasting Interface
- Automatic Evaluation
- Visualization
- Benchmark Runner
- Experiment Tracking
- Model Registry
- Forecast Persistence
- Evaluation Metrics

---

## Deep Learning Models

### Implemented Models

- LSTM
- GRU
- Seq2Seq

### Framework Features

- Sliding-window Dataset Generation
- CUDA Support
- Early Stopping
- Model Checkpointing
- Generic Trainer
- Generic Evaluator
- Deep Learning Benchmark
- Shared Training Framework
- Reusable Evaluation Pipeline

---

## Transformer Models

### Implemented Models

- PatchTST
- Informer
- Temporal Fusion Transformer (TFT)

### Framework Features

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

# 💬 LLM Forecast Explanation Framework

The LLM explanation layer converts forecasting outputs and statistical information into business-readable insights.

### Features

- Forecast Metadata Extraction
- Trend Analysis
- Seasonality Analysis
- Statistical Analysis
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

# 📚 Retrieval-Augmented Generation

The RAG subsystem allows the platform to answer business questions using a domain-specific knowledge base.

## Knowledge Base

The knowledge base contains information such as:

- Forecast Reports
- Inventory Policies
- Retail Reports
- Business Documentation
- Domain Knowledge

## Pipeline Components

```text
Documents
    │
    ▼
Document Loader
    │
    ▼
Text Chunker
    │
    ▼
Embedding Generator
    │
    ▼
FAISS Vector Store
    │
    ▼
Retriever
    │
    ▼
Context Builder
    │
    ▼
RAG Prompt
    │
    ▼
Gemini
    │
    ▼
Grounded Business Answer

Implemented Features
Document Loading
Recursive Text Processing
Intelligent Chunking
SentenceTransformer Embeddings
FAISS Vector Database
Semantic Similarity Search
Top-K Retrieval
Context Construction
RAG Prompt Engineering
Grounded Gemini Responses
Source Attribution
Interactive Business Q&A
🤖 Multi-Agent AI System

The Multi-Agent AI layer represents the next major evolution of the platform.

The system transforms the project from a collection of independent AI capabilities into a coordinated business intelligence system.

Instead of manually selecting a tool or model, users can ask questions in natural language.

For example:

"What is the best forecasting model?"

is automatically routed to the Forecast Agent.

"Which products are selling the fastest?"

is automatically routed to the Inventory Agent.

"Show me the monthly sales trend."

is automatically routed to the Analytics Agent.

"Show me the SQL query for monthly sales."

is automatically routed to the SQL Agent.

And:

"Give me an executive report."

can involve multiple specialist agents before the Executive Agent synthesizes their findings.

🧩 Multi-Agent Components
Forecast Agent

Responsible for forecasting-related intelligence.

Supported Actions
get_best_model
compare_models
get_predictions
get_experiments
Responsibilities
Forecast model evaluation
Model comparison
Prediction retrieval
Forecast experiment analysis
Forecast result interpretation
Analytics Agent

Responsible for historical business analytics.

Supported Actions
get_sales_summary
get_top_stores
get_top_products
get_monthly_sales
get_weekday_sales
get_store_performance
get_price_summary
get_sales_distribution
get_category_performance
get_department_performance
Responsibilities
Sales analytics
KPI analysis
Store comparison
Product comparison
Trend analysis
Category analysis
Department analysis
Price analysis
Inventory Agent

Responsible for inventory and replenishment intelligence.

Supported Actions
get_inventory_summary
get_fast_moving_products
get_slow_moving_products
get_store_inventory
get_reorder_candidates
get_inventory_health
Responsibilities
Inventory summaries
Fast-moving product identification
Slow-moving product identification
Store-level demand analysis
Replenishment prioritization
Inventory health analysis
SQL Agent

Responsible for database-related intelligence.

Responsibilities
Natural-language-to-SQL
SQL query generation
Table selection
SQL joins
Aggregations
Database queries
Forecasting table queries
Query result interpretation

The SQL Agent uses the database schema through a schema cache before generating SQL.

Example:

User:
Show me the SQL query for monthly sales.

        │
        ▼

SQL Agent

        │
        ▼

Schema Cache

        │
        ▼

SQL Generation

        │
        ▼

SELECT c.year,
       c.month,
       SUM(s.sales)
FROM sales_fact s
JOIN calendar_dim c
    ON s.d = c.d
GROUP BY c.year, c.month;
👔 Executive Agent

The Executive Agent acts as the final business communication layer.

It is responsible for combining information from multiple specialist agents and converting technical findings into a concise business report.

Output Structure
Executive Summary
Key Findings
Business Risks
Recommendations
Next Steps

The Executive Agent is intentionally separated from specialist agents.

Specialist agents answer:

"What does the data/model/tool say?"

The Executive Agent answers:

"What does this mean for the business, and what should we do?"

🔀 Task Router

The TaskRouter determines which specialist agents should handle a user's question.

The router currently supports the following categories:

Category	Example Keywords	Agent
Forecasting	forecast, predict, prediction, demand	Forecast
Analytics	trend, analysis, analytics, EDA, historical, seasonality, KPI	Analytics
Inventory	inventory, stock, reorder, safety stock, fast-moving	Inventory
SQL	SQL, database, query, table, select, join	SQL
Executive	report, summary, executive, business	Multiple Agents

The router removes duplicate agents while preserving the intended execution order.

🧠 Agent Orchestrator

The AgentOrchestrator coordinates specialist agents.

Its workflow is:

User Question
      │
      ▼
Task Router
      │
      ▼
Selected Agents
      │
      ├───────────────┐
      │               │
      ▼               ▼
Specialist Agents   Specialist Agents
      │               │
      └───────┬───────┘
              │
              ▼
       Specialist Results
              │
              ▼
      Executive Agent
              │
              ▼
      Executive Report

For questions requiring only one specialist, the specialist response can be returned directly.

For multi-domain questions, the system invokes the Executive Agent to synthesize the results.

🔎 Agent Query System

Milestone 9 also introduces the Agent Query System.

The Query Engine provides a single entry point for natural-language interaction with the entire AI system.

Conceptually:

from src.ai.query.query_engine import QueryEngine

engine = QueryEngine()

result = engine.ask(
    "Which products are selling the fastest?"
)

The Query Engine coordinates:

Natural Language Question
          │
          ▼
     Query Engine
          │
          ▼
     Task Router
          │
          ▼
   Agent Orchestrator
          │
          ▼
   Specialist Agents
          │
          ▼
      Tool Layer
          │
          ▼
      Real Results
          │
          ▼
    LLM Explanation
          │
          ▼
     Final Response

This creates a clean abstraction between the future application/API layer and the internal AI architecture.

🧪 Multi-Agent Validation

The multi-agent architecture has been validated using dedicated test suites.

Query Routing Tests

The following representative questions have been tested:

What is the best forecasting model?
Which products are selling the fastest?
Show me the monthly sales trend.
Show me the SQL query for monthly sales.
Give me an executive report.

Expected routing:

"What is the best forecasting model?"
→ forecast

"Which products are selling the fastest?"
→ inventory

"Show me the monthly sales trend."
→ analytics

"Show me the SQL query for monthly sales."
→ sql

"Give me an executive report."
→ forecast + analytics + inventory

All routing tests currently pass.

✅ Milestone 9 Validation

The following components have been successfully implemented and tested:

Component	Status
Forecast Agent	✅
Analytics Agent	✅
Inventory Agent	✅
SQL Agent	✅
Executive Agent	✅
Task Router	✅
Agent Orchestrator	✅
Agent Tool Execution	✅
Agent Result Explanation	✅
Multi-Agent Executive Report	✅
Query Engine	✅
Query Routing	✅
Natural-language Business Queries	✅
🏆 Benchmark Results

The project contains dedicated benchmark suites for the implemented forecasting paradigms.

Classical Forecasting
Moving Average
ARIMA
SARIMA
Prophet
Deep Learning
LSTM
GRU
Seq2Seq
Transformers
PatchTST
Informer
Temporal Fusion Transformer

Benchmark artifacts are stored under:

artifacts/
└── benchmarks/

Forecast experiments are persisted in the MySQL forecasting tables.

🗂️ Project Structure

The project follows a modular architecture separating data engineering, analytics, forecasting, AI, tools, agents, and query orchestration.

AI-demand-intelligence-platform/
│
├── configs/
│   ├── database.example.yaml
│   ├── database.yaml
│   └── llm.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── knowledge_base/
│       ├── forecast_reports/
│       ├── inventory_policies/
│       └── retail_reports/
│
├── docs/
│   ├── business_case/
│   ├── milestone_01_etl/
│   ├── milestone_02_eda/
│   ├── milestone_03_forecasting/
│   ├── milestone_04_deep_learning/
│   ├── milestone_05_transformers/
│   ├── milestone_06_llm/
│   ├── milestone_07_rag/
│   └── milestone_09_multi_agent/
│
├── artifacts/
│   ├── benchmarks/
│   ├── faiss/
│   ├── metadata/
│   ├── models/
│   ├── prompts/
│   └── reports/
│
├── src/
│   ├── ai/
│   │   ├── agents/
│   │   │   ├── base_agent.py
│   │   │   ├── forecast_agent.py
│   │   │   ├── analytics_agent.py
│   │   │   ├── inventory_agent.py
│   │   │   ├── sql_agent.py
│   │   │   ├── executive_agent.py
│   │   │   ├── orchestrator.py
│   │   │   └── router.py
│   │   │
│   │   ├── tools/
│   │   │   ├── forecast_tool.py
│   │   │   ├── analytics_tool.py
│   │   │   ├── inventory_tool.py
│   │   │   └── sql_tool.py
│   │   │
│   │   ├── query/
│   │   │   ├── query_engine.py
│   │   │   └── query_router.py
│   │   │
│   │   ├── knowledge/
│   │   │   └── schema_cache.py
│   │   │
│   │   ├── llm/
│   │   ├── prompts/
│   │   ├── rag/
│   │   │   ├── document_loader.py
│   │   │   ├── text_chunker.py
│   │   │   ├── embedding_generator.py
│   │   │   ├── vector_store.py
│   │   │   ├── retriever.py
│   │   │   ├── context_builder.py
│   │   │   └── pipeline.py
│   │   │
│   │   ├── metadata.py
│   │   ├── pipeline.py
│   │   ├── report.py
│   │   └── html_report.py
│   │
│   ├── analytics/
│   ├── database/
│   ├── etl/
│   ├── forecasting/
│   │   ├── classical/
│   │   ├── deep_learning/
│   │   └── transformers/
│   │
│   └── utils/
│
├── tests/
│   ├── agents/
│   ├── inventory/
│   ├── query/
│   ├── tools/
│   ├── rag/
│   ├── forecasting/
│   ├── transformers/
│   └── llm/
│
├── requirements.txt
├── README.md
└── .gitignore
🛠️ Tech Stack
Programming
Python 3.12
Data Engineering
Pandas
NumPy
MySQL
Forecasting
Statsmodels
pmdarima
Prophet
Deep Learning
PyTorch
CUDA
Transformers
PyTorch
Custom Transformer Architectures
LLM
Google Gemini
Prompt Engineering
RAG
SentenceTransformers
all-MiniLM-L6-v2
FAISS
Semantic Search
Vector Embeddings
Data Visualization
Matplotlib
Seaborn
Database
MySQL
MySQL Workbench
Upcoming Application Technologies
FastAPI
React
Tailwind CSS
Docker
GitHub Actions
MLflow
DVC
🚀 Getting Started
1. Clone the Repository
git clone <repository-url>
cd AI-demand-intelligence-platform
2. Create a Virtual Environment
python -m venv venv
3. Activate the Environment
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Configure MySQL

Copy:

configs/database.example.yaml

to:

configs/database.yaml

and configure the local MySQL connection.

Do not commit credentials or secrets to GitHub.

6. Configure Gemini

Create/configure:

configs/llm.yaml

Example:

provider: gemini
model: YOUR_MODEL
api_key: YOUR_API_KEY

Keep API keys outside version control.

7. Create the Database Schema

Execute:

src/database/schema.sql

using MySQL Workbench or the MySQL CLI.

8. Run the ETL Pipeline

Example:

python -m tests.test_sales_pipeline

Individual ETL pipeline tests can also be executed separately.

🧪 Testing

The project contains dedicated test modules for major subsystems.

Forecasting
python -m tests.benchmark_classical_models
Deep Learning
python -m tests.benchmark_deep_learning
Transformers
python -m tests.transformers.benchmark_transformers
LLM Pipeline
python -m tests.llm.test_pipeline
RAG
python -m tests.rag.rag_assistant
🤖 Testing the Multi-Agent System
Test Agent Routing
python -m tests.agents.test_router
Test Inventory Agent
python -m tests.agents.test_inventory_agent
Test Inventory Execution
python -m tests.agents.test_inventory_execution
Test Full Inventory Agent
python -m tests.agents.test_inventory_agent_full
Test Orchestrator
python -m tests.agents.test_orchestrator
Test SQL Agent
python -m tests.agents.test_sql_agent
Test Query Routing
python -m tests.query.test_query_routing
Test Query Engine
python -m tests.query.test_query_engine
💬 Example Business Questions

The platform can answer questions such as:

Forecasting
What is the best forecasting model?
Compare the forecasting models.
Show Prophet predictions.
Analytics
Show me the monthly sales trend.
Which stores performed the best?
What are the top-selling products?
Inventory
Which products are selling the fastest?
Which products are slow moving?
Which products should we prioritize for replenishment?
How healthy is our inventory?
SQL
Show me the SQL query for monthly sales.
Which tables contain product information?
Executive Intelligence
Give me an executive report.
Summarize the current business situation.
What are the biggest business risks?
📌 Current Status
Current Version
v9.0.0
Completed Milestones
✅ Milestone 0 — Business Understanding
✅ Milestone 1 — ETL & MySQL Data Warehouse
✅ Milestone 2 — Exploratory Data Analysis
✅ Milestone 3 — Classical Forecasting
✅ Milestone 4 — Deep Learning Forecasting
✅ Milestone 5 — Transformer Forecasting
✅ Milestone 6 — LLM-powered Forecast Explanations
✅ Milestone 7 — Retrieval-Augmented Generation
✅ Milestone 9 — Multi-Agent AI & Agent Query System
🗺️ Project Roadmap
Status	Milestone	Description
✅	Milestone 0	Business Understanding
✅	Milestone 1	ETL & MySQL Data Warehouse
✅	Milestone 2	Exploratory Data Analysis
✅	Milestone 3	Classical Forecasting
✅	Milestone 4	Deep Learning Forecasting
✅	Milestone 5	Transformer Forecasting
✅	Milestone 6	LLM Forecast Explanations
✅	Milestone 7	Retrieval-Augmented Generation
✅	Milestone 9	Multi-Agent AI & Agent Query System
🚧	Milestone 10	FastAPI Application Layer
⬜	Milestone 11	React Dashboard
⬜	Milestone 12	Deployment & MLOps
🏆 Milestone 9 — Final Achievement

Milestone 9 transforms the project from an AI forecasting platform into a broader AI-powered business intelligence system.

The platform can now:

Understand a Business Question
            │
            ▼
      Route the Question
            │
            ▼
    Select Specialist Agent(s)
            │
            ▼
      Execute Real Tools
            │
            ▼
     Retrieve Real Data
            │
            ▼
     Interpret the Results
            │
            ▼
    Synthesize if Necessary
            │
            ▼
     Return Business Answer

This establishes the foundation for the next application layer.

📊 Project Statistics
Category	Count / Status
ETL Pipelines	5
Forecasting Models	10
Forecasting Paradigms	3
Benchmark Suites	3
Deep Learning Models	3
Transformer Models	3
LLM Pipelines	2
AI Report Formats	2
Knowledge Base Categories	3
Vector Databases	1
Specialist AI Agents	4
Executive Agent	1
Agent Router	1
Agent Orchestrator	1
Query Engine	1
Query Routing Tests	Validated
Dataset Size	58M+ Records
🌟 Project Highlights
📦 Data Engineering
Production-oriented ETL Framework
Chunk-based Processing
Configuration-driven Pipelines
MySQL Star Schema
Data Validation
Execution Metrics
Structured Logging
📊 Business Intelligence
SQL Analytics Layer
Business-oriented EDA
KPI Analysis
Trend Analysis
Seasonality Analysis
Store Performance
Product Performance
Category Analysis
Department Analysis
📈 Forecasting

Implemented 10 forecasting models across three forecasting paradigms.

Classical
Moving Average
ARIMA
SARIMA
Prophet
Deep Learning
LSTM
GRU
Seq2Seq
Transformers
PatchTST
Informer
Temporal Fusion Transformer
💬 Explainable AI
Forecast Metadata Extraction
Trend Analysis
Seasonality Detection
Statistical Analysis
Prompt Engineering
Gemini Integration
AI-generated Business Explanations
Markdown Reports
HTML Reports
Timestamped Artifacts
📚 Retrieval-Augmented Generation
Business Knowledge Base
Recursive Document Loading
Intelligent Text Chunking
SentenceTransformer Embeddings
FAISS Vector Database
Semantic Similarity Search
Top-K Retrieval
Context Building
RAG Prompt Engineering
Source-aware Responses
Interactive Business Q&A
🤖 Multi-Agent AI
Forecast Agent
Analytics Agent
Inventory Agent
SQL Agent
Executive Agent
Deterministic Task Router
Agent Orchestrator
Tool Calling
Real Database Access
Result Interpretation
Multi-agent Collaboration
Executive Report Synthesis
Natural-language Query Engine
🧱 Software Engineering Highlights

The project emphasizes production-oriented software engineering rather than notebook-only experimentation.

Architecture
Modular Components
Separation of Concerns
Reusable Abstractions
Configuration-driven Execution
Tool-based AI Architecture
Agent-based Architecture
AI Engineering
Specialized Agents
Deterministic Routing
Tool Grounding
LLM-based Interpretation
Structured Agent Outputs
Multi-agent Orchestration
Query Abstraction
ML Engineering
Shared Training Frameworks
Shared Evaluation Frameworks
Model Registry
Experiment Tracking
Checkpointing
Benchmarking
Artifact Persistence
Data Engineering
ETL Validation
Chunk Processing
MySQL Warehouse
Structured Schema
Data Quality Checks
Execution Metrics
🎯 Next Milestone
🚧 Milestone 10 — FastAPI Application Layer

The next major milestone will expose the existing AI platform through a production-oriented API.

The goal is to transform:

Python AI System

into:

FastAPI Backend
       │
       ▼
Query API
       │
       ▼
Agent Query Engine
       │
       ▼
Multi-Agent System
       │
       ▼
Tools / Database / Models / RAG
Planned Components
FastAPI Application
API Routers
Request Schemas
Response Schemas
Query Endpoint
Health Endpoint
Forecast Endpoint
Analytics Endpoint
Inventory Endpoint
SQL Endpoint
Error Handling
API Logging
API Documentation
CORS Configuration
Service Layer
Dependency Injection

This API will later become the backend consumed by the React dashboard.

🖥️ Future Dashboard

The planned frontend will provide an interactive business intelligence interface.

Potential dashboard sections:

Dashboard
│
├── Executive Overview
├── Sales Analytics
├── Demand Forecasts
├── Inventory Intelligence
├── Store Performance
├── Product Performance
├── AI Business Assistant
└── SQL Explorer

The AI Assistant will allow users to interact with the platform using natural language.

Example:

User:
Which products should we prioritize for replenishment?

                 │
                 ▼

             React UI

                 │
                 ▼

            FastAPI API

                 │
                 ▼

          Query Engine

                 │
                 ▼

        Inventory Agent

                 │
                 ▼

         Inventory Tool

                 │
                 ▼

          MySQL Warehouse

                 │
                 ▼

          Business Answer
🚀 Long-Term Vision

The final objective is to build an intelligent retail decision-support platform capable of connecting:

Data Engineering
       │
       ▼
Data Warehouse
       │
       ▼
Analytics
       │
       ▼
Forecasting
       │
       ▼
Deep Learning
       │
       ▼
Transformers
       │
       ▼
Explainable AI
       │
       ▼
RAG
       │
       ▼
Multi-Agent AI
       │
       ▼
FastAPI
       │
       ▼
Interactive Dashboard
       │
       ▼
MLOps
       │
       ▼
Production Deployment

The ultimate system should allow a business user to ask a question in natural language and receive a grounded, explainable, data-backed recommendation.

🔐 Security & Configuration

Sensitive credentials should never be committed to the repository.

Examples include:

MySQL passwords
Gemini API keys
Database credentials
Cloud credentials
Authentication secrets

Use local configuration files and environment variables where appropriate.

Example:

configs/
├── database.example.yaml
├── database.yaml        # local only
└── llm.yaml             # local only

Ensure sensitive files are included in .gitignore.

🧪 Reproducibility

The project is structured to make experiments and pipeline execution reproducible.

Important reproducibility components include:

Configuration files
Fixed project structure
Model checkpoints
Experiment metadata
Benchmark artifacts
Persisted prompts
Timestamped reports
Structured logs
Database schemas
Dedicated test suites
📁 Important Artifact Directories
artifacts/
│
├── benchmarks/
│   └── Model benchmark results
│
├── faiss/
│   └── Vector indexes
│
├── metadata/
│   └── Forecast metadata
│
├── models/
│   └── Saved model checkpoints
│
├── prompts/
│   └── Persisted prompts
│
└── reports/
    ├── markdown/
    └── html/
🧭 Development Philosophy

This project follows several engineering principles.

1. Modularity

Each major capability is implemented as an independent component.

2. Reusability

Common functionality is abstracted into reusable frameworks.

3. Separation of Concerns

Data engineering, modeling, analytics, AI, and application layers remain logically separated.

4. Tool Grounding

LLMs should interpret real data rather than invent business metrics.

5. Explainability

AI-generated outputs should be understandable to business users.

6. Reproducibility

Experiments and model outputs should be traceable and reproducible.

7. Production Orientation

The project is structured with eventual deployment, APIs, observability, and MLOps in mind.

🤝 Contributing

Contributions, suggestions, improvements, and feature requests are welcome.

If you would like to contribute:

Fork the repository.
Create a feature branch.
Make your changes.
Add or update tests.
Commit your changes.
Push the branch.
Open a Pull Request.
📄 License

This project is licensed under the MIT License.

⭐ Support the Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

It helps the project gain visibility and motivates continued development.

🏁 Final Project Summary

The AI Demand Intelligence Platform demonstrates the evolution of a modern AI system from raw retail data to intelligent business decision support.

It combines:

                 ┌──────────────────────┐
                 │    Raw Retail Data   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Production ETL    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    MySQL Warehouse   │
                 └──────────┬───────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         Analytics     Forecasting     Inventory
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Explainable AI    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │         RAG          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Multi-Agent AI    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Query Engine     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    FastAPI Backend   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   React Dashboard    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Production / MLOps   │
                 └──────────────────────┘

The project has progressed from a traditional forecasting pipeline into a broader AI-powered Demand Intelligence Platform capable of combining:

Data Engineering
Business Analytics
Statistical Forecasting
Deep Learning
Transformers
Explainable AI
Retrieval-Augmented Generation
Semantic Search
Tool Calling
Multi-Agent AI
Natural-language Querying
Executive Decision Support

The completed Multi-Agent layer establishes the foundation for the next stage:

Turning the AI system into a production API and eventually an interactive enterprise business intelligence application.

📌 Project Status

Current Milestone:

✅ Milestone 9 — Multi-Agent AI & Agent Query System

Next Milestone:

🚧 Milestone 10 — FastAPI Application Layer

Overall Direction:

From Data → Intelligence → Agents → APIs → Applications → Production