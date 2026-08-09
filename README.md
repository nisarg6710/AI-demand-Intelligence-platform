# 📊 AI Demand Intelligence Platform

> **Production-oriented AI-powered Demand Forecasting, Business Intelligence, RAG, Multi-Agent AI, and FastAPI Platform**

An end-to-end AI system that transforms large-scale retail sales data into **forecasting insights, business analytics, inventory intelligence, grounded AI answers, multi-agent decision support, and executive reports**.

The project combines:

- Data Engineering
- MySQL Data Warehousing
- Business Analytics
- Classical Time-Series Forecasting
- Deep Learning
- Transformer-based Forecasting
- Explainable AI
- Large Language Models
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Tool-Grounded AI Agents
- Multi-Agent Orchestration
- FastAPI REST APIs

The ultimate goal is to allow a business user to ask a question in natural language and receive a **data-backed, explainable, and actionable answer**.

---

# 🎯 Why This Project?

Retail businesses generate enormous amounts of transactional data, but raw data alone does not provide decision-making value.

A business may know:

- How much it sold
- Which products exist
- Which stores exist
- Historical demand
- Forecasting model metrics

but still struggle to answer questions such as:

> **"Which products should we prioritize for replenishment?"**

> **"What is driving our recent sales growth?"**

> **"Which forecasting model should we trust?"**

> **"Show me the monthly sales trend."**

> **"Give me an executive summary of the current business situation."**

Traditional data-science projects often stop at a notebook, model, or dashboard.

This project goes further by building a complete pipeline from:

**Raw Data → Data Warehouse → Analytics → Forecasting → AI → Agents → API**

---

# 💡 Problem Statement

Poor demand planning can lead to:

- Stockouts
- Overstocking
- Excess inventory costs
- Inefficient replenishment
- Lost sales
- Poor resource allocation
- Unreliable business planning

At the same time, business users generally cannot interact directly with forecasting models, SQL databases, analytics pipelines, and machine-learning systems.

The problem addressed by this project is therefore:

> **How can large-scale retail data, forecasting models, analytics systems, domain knowledge, and modern LLMs be combined into a single system that provides reliable, explainable, and actionable business intelligence through natural language?**

---

# 🧠 Solution

The platform solves this problem through a layered architecture.

```text
                    Raw Retail Data
                          │
                          ▼
                   Production ETL
                          │
                          ▼
                 MySQL Data Warehouse
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
          Analytics   Forecasting   Inventory
              │           │           │
              └───────────┼───────────┘
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
                    Query Engine
                          │
                          ▼
                    FastAPI API
                          │
                          ▼
                Future React Dashboard

The key design principle is:

LLMs do not directly invent business results.

Agents use deterministic tools to retrieve actual information from databases, forecasting experiments, analytics pipelines, and knowledge bases.

The LLM is then used primarily for:

Reasoning
Interpretation
Explanation
Natural-language interaction
Business-oriented summarization

This creates a more reliable architecture than allowing an LLM to directly answer numerical business questions from its internal knowledge.

🚀 What the Platform Can Do

The current system can:

📦 Data Engineering
Process large-scale retail datasets
Validate incoming data
Transform raw data
Perform chunk-based ETL
Load data into MySQL
Track ETL execution metrics
Maintain a structured warehouse
📊 Business Intelligence
Analyze sales trends
Analyze monthly and weekday sales
Compare stores
Analyze products and categories
Analyze departments
Analyze prices
Calculate business KPIs
Analyze historical demand
📈 Forecasting

Supports three forecasting paradigms:

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

The forecasting framework also supports:

Common model interfaces
Evaluation
Benchmarking
Experiment tracking
Model persistence
Checkpointing
Visualization
💬 Explainable AI

Forecast outputs are converted into business-readable explanations using:

Forecast metadata
Trend analysis
Seasonality analysis
Statistical analysis
Prompt engineering
Gemini

Reports can be generated in:

Markdown
HTML
📚 RAG

The platform can retrieve information from a domain-specific knowledge base using:

Document loading
Text chunking
SentenceTransformer embeddings
FAISS
Semantic retrieval
Context construction
Gemini

This allows the AI to provide knowledge-grounded responses with retrieved context.

🤖 Multi-Agent AI

The platform contains specialized agents for:

Forecasting
Analytics
Inventory
SQL
Executive reporting

A task router determines which agent or agents should handle a question.

🌐 FastAPI

The AI platform is exposed through REST APIs:

GET  /health
POST /chat
POST /forecast
POST /analytics
POST /report

Interactive API documentation is automatically available through FastAPI/Swagger.

🏗️ System Architecture

The complete application currently follows:

                         User
                          │
                          ▼
                  Natural Language Query
                          │
                          ▼
                     FastAPI API
                          │
                          ▼
                    Query Engine
                          │
                          ▼
                     Task Router
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
       Forecast       Analytics      Inventory
         Agent          Agent          Agent
            │             │             │
            ▼             ▼             ▼
       Forecast        Analytics      Inventory
         Tool            Tool           Tool
            │             │             │
            └─────────────┼─────────────┘
                          ▼
                    Real Results
                          │
                          ▼
                  Executive Agent
                          │
                          ▼
                   Business Answer

For questions requiring only one specialist, the relevant agent can return the result directly.

For cross-domain questions, multiple agents execute and the Executive Agent synthesizes their findings.

🤖 Multi-Agent Intelligence

The platform currently contains five major AI agents.

Agent	Responsibility
Forecast Agent	Forecast models, predictions, metrics, experiments
Analytics Agent	Sales, trends, stores, products, KPIs
Inventory Agent	Fast-moving products, inventory health, replenishment
SQL Agent	Natural-language SQL and database intelligence
Executive Agent	Cross-domain business synthesis

A deterministic TaskRouter decides which agents are relevant.

For example:

"What is the best forecasting model?"
              │
              ▼
        Forecast Agent
"Which products are selling the fastest?"
              │
              ▼
        Inventory Agent
"Show me the monthly sales trend."
              │
              ▼
        Analytics Agent
"Show me the SQL query for monthly sales."
              │
              ▼
           SQL Agent

For an executive question:

"Give me an executive report."
              │
              ▼
         Task Router
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
   Forecast Analytics Inventory
       │      │      │
       └──────┼──────┘
              ▼
       Executive Agent
              │
              ▼
       Executive Report
🔎 Natural-Language Query System

The Query Engine provides a unified interface over the entire AI system.

Conceptually:

from src.ai.query.query_engine import QueryEngine

engine = QueryEngine()

result = engine.ask(
    "Which products are selling the fastest?"
)

The Query Engine coordinates:

Question
   ↓
Task Routing
   ↓
Agent Selection
   ↓
Tool Execution
   ↓
Real Data / Model Results
   ↓
LLM Interpretation
   ↓
Business Response

This creates a clean abstraction between the application layer and the internal AI architecture.

📊 Example Business Questions
Forecasting
What is the best forecasting model?
Compare the forecasting models.
Show me the forecast predictions.
Analytics
Show me the monthly sales trend.
Which stores performed the best?
What are the top-selling products?
Inventory
Which products are selling the fastest?
Which products are slow-moving?
Which products should we prioritize for replenishment?
How healthy is our inventory?
SQL
Show me the SQL query for monthly sales.
Which tables contain product information?
Executive Intelligence
Give me an executive report.
What are the biggest business risks?
Summarize the current business situation.
🗄️ Data Warehouse

The platform uses a MySQL star-schema architecture.

Dimension Tables
calendar_dim
item_dim
store_dim
Fact Tables
sales_fact
price_fact
Analytics
sales_enriched
Forecasting
forecast_experiments
forecast_predictions

The warehouse acts as a centralized source of truth for:

Analytics
SQL queries
Inventory intelligence
Forecasting
AI agents
📦 Dataset

The primary dataset is the:

M5 Forecasting – Accuracy Dataset

The dataset provides large-scale retail demand data containing:

Product information
Store information
Department information
Category information
Historical sales
Calendar information
Prices

The project works with approximately 58M+ sales records.

Future versions can incorporate external signals such as:

Weather
Promotions
Holiday calendars
Economic indicators
Competitor pricing
Store-level information
⚙️ ETL Architecture

The data engineering layer follows:

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
Chunk Processing
     │
     ▼
MySQL Loading
     │
     ▼
Data Warehouse

The ETL framework includes:

Configuration-driven execution
CSV extraction
Data validation
Transformation
Chunk-based processing
Batch loading
MySQL integration
Execution metrics
Logging
Error handling

This makes the project closer to a reusable data pipeline rather than a single preprocessing notebook.

📈 Forecasting Framework

The forecasting system is built around reusable abstractions so that different models can share:

Training interfaces
Evaluation
Benchmarking
Experiment tracking
Persistence
Visualization
Classical Models
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

The project therefore demonstrates multiple forecasting paradigms rather than relying on a single model.

📚 Retrieval-Augmented Generation

The RAG subsystem provides access to external business knowledge.

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
FAISS
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
Grounded Answer

The knowledge base can contain:

Forecast reports
Inventory policies
Retail reports
Business documentation
Domain knowledge

RAG allows the system to combine structured business data with unstructured business knowledge.

🌐 FastAPI Backend

The current application exposes the AI platform through FastAPI.

Health
GET /health
Chat
POST /chat

General-purpose natural-language business assistant.

Forecast
POST /forecast

Forecasting-specific intelligence.

Analytics
POST /analytics

Business analytics queries.

Report
POST /report

Multi-agent executive reporting.

Interactive API documentation:

http://127.0.0.1:8000/docs

OpenAPI specification:

http://127.0.0.1:8000/openapi.json
🧪 Testing

The project contains dedicated tests for major subsystems.

API tests:

python -m pytest tests/api -v

The current API integration suite validates:

/health       ✅
/chat         ✅
/forecast     ✅
/analytics    ✅
/report       ✅

Current result:

5 passed

Additional tests exist for:

ETL
Forecasting
Transformers
LLM pipelines
RAG
Agents
Tools
Query routing
Query orchestration

The project therefore validates not only individual models but also the interaction between major system components.

🛠️ Technology Stack
Layer	Technologies
Language	Python 3.12
Data Processing	Pandas, NumPy
Database	MySQL
Forecasting	Statsmodels, pmdarima, Prophet
Deep Learning	PyTorch, CUDA
Transformers	PyTorch, custom architectures
LLM	Google Gemini
RAG	SentenceTransformers, FAISS
Visualization	Matplotlib, Seaborn
API	FastAPI, Uvicorn, Pydantic
Testing	Pytest
Version Control	Git, GitHub
📂 Project Structure

The repository follows a modular architecture:

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
│   ├── milestone_09_multi_agent/
│   └── milestone_10_fastapi/
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
│   │   ├── tools/
│   │   ├── query/
│   │   ├── knowledge/
│   │   ├── llm/
│   │   ├── prompts/
│   │   └── rag/
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── schema.py
│   │   └── routes/
│   │
│   ├── analytics/
│   ├── database/
│   ├── etl/
│   ├── forecasting/
│   │   ├── classical/
│   │   ├── deep_learning/
│   │   └── transformers/
│   └── utils/
│
├── tests/
│   ├── agents/
│   ├── api/
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

# 💻 Requirements

Before running the project, make sure the following software and services are available.

## Required Software

| Requirement | Version / Recommendation |
|---|---|
| Python | **3.12.x** |
| MySQL | **8.0+** |
| Git | Latest stable version |
| pip | Latest version |
| Virtual Environment | Python `venv` recommended |

## Required Python Packages

All Python dependencies are specified in:

```text
requirements.txt

Required Services
MySQL

A running MySQL server is required for:

Sales data
Product data
Store data
Calendar data
Price data
Forecast experiments
Forecast predictions
SQL Agent queries

The database schema is provided in:

src/database/schema.sql
Google Gemini API

A Gemini API key is required for the LLM-powered components:

Forecast explanations
RAG responses
Agent reasoning
Business report generation

Configure it locally in:

configs/llm.yaml

Example:

provider: gemini
model: YOUR_MODEL
api_key: YOUR_API_KEY

Never commit this file if it contains a real API key.

Dataset Requirement

The project uses the:

M5 Forecasting – Accuracy Dataset

The required raw datasets include:

sales_train_validation.csv
calendar.csv
sell_prices.csv

Place them under:

data/raw/

The ETL pipeline then transforms and loads the data into MySQL.

The M5 dataset is not included in the repository because of its size. It must be obtained separately and placed in data/raw/.


🚀 Getting Started
1. Clone the Repository
git clone <repository-url>
cd AI-demand-intelligence-platform
2. Create a Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🗄️ Database Setup

Install and run MySQL locally.

Create the required database schema using:

src/database/schema.sql

This can be executed through MySQL Workbench or the MySQL CLI.

🔐 Configuration

The project requires configuration for:

MySQL
Gemini API

Use the provided example configuration:

configs/database.example.yaml

Create your local database configuration:

configs/database.yaml

Configure the Gemini credentials in:

configs/llm.yaml

Example:

provider: gemini
model: YOUR_MODEL
api_key: YOUR_API_KEY

Never commit API keys, passwords, or other credentials to GitHub.

Make sure sensitive configuration files are included in .gitignore.

▶️ Running the Application

Start the FastAPI backend:

uvicorn src.api.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Open Swagger:

http://127.0.0.1:8000/docs
💬 Example API Request
Chat
{
    "question": "Which products are selling the fastest?"
}

The system can route this automatically:

Question
   ↓
Task Router
   ↓
Inventory Agent
   ↓
Inventory Tool
   ↓
MySQL
   ↓
LLM Interpretation
   ↓
Business Response
🧪 Running Tests

Run the FastAPI tests:

python -m pytest tests/api -v

Run the complete project test suite:

python -m pytest -v

Individual subsystems can also be tested independently.

🔒 Security

Sensitive information should never be committed to the repository.

Examples include:

MySQL passwords
Gemini API keys
Database credentials
Cloud credentials
Authentication secrets

Use:

configs/database.yaml
configs/llm.yaml

locally and keep them excluded from version control.

📈 Engineering Approach

The project intentionally follows a production-oriented architecture rather than a notebook-only approach.

Key principles include:

Separation of Concerns

Data engineering, forecasting, analytics, AI, agents, and API layers are separated.

Reusability

Common functionality is implemented through reusable abstractions.

Tool Grounding

AI agents retrieve real data through deterministic tools instead of generating unsupported business metrics.

Explainability

Forecasts and analytical results are converted into understandable business explanations.

Reproducibility

Experiments, models, prompts, reports, and benchmark results can be persisted.

Testability

Major components have dedicated test suites.

Extensibility

The architecture allows additional models, agents, tools, APIs, and data sources to be added without redesigning the entire system.

🌟 What Makes This Project Meaningful?

The main contribution of this project is not simply implementing another forecasting model or connecting an LLM to a database.

The project demonstrates how multiple areas of modern data science and AI engineering can be integrated into one coherent decision-support system.

Instead of:

Dataset
   ↓
Notebook
   ↓
Model
   ↓
Prediction

the platform provides:

Large-scale Data
       ↓
Production ETL
       ↓
Data Warehouse
       ↓
Business Analytics
       ↓
Multiple Forecasting Paradigms
       ↓
Explainable AI
       ↓
Domain Knowledge through RAG
       ↓
Specialized AI Agents
       ↓
Tool-Grounded Reasoning
       ↓
Multi-Agent Decision Support
       ↓
FastAPI Backend

This architecture demonstrates practical skills across:

Data Engineering
Machine Learning
Deep Learning
Time-Series Forecasting
Generative AI
RAG
AI Agents
API Development
Database Engineering
Software Engineering
Testing

More importantly, the system attempts to solve the business usability problem: making complex analytical and machine-learning capabilities accessible to non-technical users through natural language.

📌 Current Status
Completed
✅ Business Understanding
✅ ETL & MySQL Data Warehouse
✅ Exploratory Data Analysis
✅ Classical Forecasting
✅ Deep Learning Forecasting
✅ Transformer Forecasting
✅ LLM Forecast Explanations
✅ Retrieval-Augmented Generation
✅ Multi-Agent AI
✅ Agent Query System
✅ Tool-Grounded AI
✅ Executive Report Generation
✅ FastAPI Backend
✅ API Integration Tests
🗺️ Roadmap
Status	Milestone
✅	Business Understanding
✅	ETL & MySQL Data Warehouse
✅	Exploratory Data Analysis
✅	Classical Forecasting
✅	Deep Learning Forecasting
✅	Transformer Forecasting
✅	LLM Forecast Explanations
✅	Retrieval-Augmented Generation
✅	Multi-Agent AI & Query System
✅	FastAPI Backend
🚧	React Dashboard
⬜	Deployment & MLOps
🔮 Future Direction

The next stage is to build a React-based business intelligence dashboard on top of the FastAPI backend.

The planned architecture is:

React Dashboard
       │
       ▼
FastAPI Backend
       │
       ▼
Query Engine
       │
       ▼
Multi-Agent System
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
Forecast Analytics Inventory
       │
       ▼
MySQL / Models / RAG

The dashboard will eventually provide:

Executive Overview
Sales Analytics
Demand Forecasting
Inventory Intelligence
Store Performance
Product Performance
AI Business Assistant
Executive Reports

Long term, the platform can be extended with:

Docker
CI/CD
MLflow
DVC
Monitoring
Cloud Deployment
Authentication
Production MLOps
📊 Project Highlights
Area	Implementation
Data Engineering	Production-oriented ETL + MySQL
Data Warehouse	Star Schema
Forecasting	10 models across 3 paradigms
Deep Learning	LSTM, GRU, Seq2Seq
Transformers	PatchTST, Informer, TFT
Explainable AI	Gemini-powered forecast explanations
RAG	SentenceTransformers + FAISS
AI Agents	Forecast, Analytics, Inventory, SQL
Multi-Agent AI	Task Router + Orchestrator + Executive Agent
Query System	Natural-language business interface
Backend	FastAPI REST API
Testing	Pytest + API integration tests
Dataset	M5 Forecasting – Accuracy
Scale	58M+ sales records
📄 Documentation

Detailed documentation for individual stages of the project is available under:

docs/

including:

docs/milestone_01_etl/
docs/milestone_02_eda/
docs/milestone_03_forecasting/
docs/milestone_04_deep_learning/
docs/milestone_05_transformers/
docs/milestone_06_llm/
docs/milestone_07_rag/
docs/milestone_09_multi_agent/
docs/milestone_10_fastapi/

The documentation explains the implementation decisions, architecture, experiments, testing, and milestone-specific work in greater detail.

📄 License

This project is licensed under the MIT License.

⭐ Final Summary

AI Demand Intelligence Platform is an end-to-end project that demonstrates how raw retail data can be transformed into an intelligent business decision-support system.

The platform combines:

Raw Retail Data
       ↓
Production ETL
       ↓
MySQL Warehouse
       ↓
Analytics
       ↓
Forecasting
       ↓
Deep Learning
       ↓
Transformers
       ↓
Explainable AI
       ↓
RAG
       ↓
Multi-Agent AI
       ↓
Query Engine
       ↓
FastAPI
       ↓
Future Dashboard

The key idea is simple:

A business user should not need to understand SQL, forecasting algorithms, vector databases, or AI architectures to obtain useful insights from business data.

The platform therefore provides a natural-language interface over the underlying data, models, tools, and knowledge systems while maintaining a grounded, modular, and testable architecture.

Current milestone: ✅ FastAPI Backend

Next milestone: 🚧 React Business Intelligence Dashboard