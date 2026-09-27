# 📊 AI Demand Intelligence Platform

An end-to-end **AI-powered retail demand intelligence platform** that transforms large-scale retail sales data into forecasting insights, business analytics, and natural-language decision support.

The platform combines:

- Large-scale data engineering
- MySQL data warehousing
- Business analytics
- Classical, deep-learning, and transformer forecasting
- Generative AI
- Retrieval-Augmented Generation (RAG)
- Multi-agent AI
- FastAPI
- React
- Natural-language business intelligence

The goal is to provide a unified interface where users can interact with complex retail data and forecasting systems without needing to directly write SQL queries, understand model implementations, or navigate multiple disconnected analytical tools.

---

# 🎯 Problem

Retail organizations generate large amounts of sales data, but converting that data into useful business decisions typically requires multiple disconnected systems.

A traditional workflow looks like:

```text
Raw Retail Data
      ↓
ETL Pipeline
      ↓
Data Warehouse
      ↓
SQL / Analytics
      ↓
Forecasting Models
      ↓
Reports

A business user may want to ask:

Which stores are performing best?

What is the monthly sales trend?

Which products are performing best?

What does the demand forecast look like?

Which forecasting model performs best?

What are the important business insights?

Give me an executive summary.


Project Goal

Build a unified, data-grounded intelligence platform that allows business users to interact with:

Retail data
Analytics
Forecasting models
Business knowledge
AI agents

through a natural-language interface.

💡 Solution

The platform integrates the complete decision-making pipeline:

Retail Dataset
      ↓
ETL Pipeline
      ↓
MySQL Data Warehouse
      ↓
Analytics + Forecasting
      ↓
AI / RAG
      ↓
Multi-Agent System
      ↓
FastAPI
      ↓
React Dashboard

A key design principle is that the LLM is not treated as the source of numerical truth.

Instead, the system follows:

User Question
      ↓
Query Router
      ↓
Specialized Agent
      ↓
Deterministic Tool
      ↓
Database / Forecasting Model / Knowledge Base
      ↓
Real Results
      ↓
LLM Interpretation
      ↓
Business Answer

This allows the platform to combine the flexibility of natural-language AI with the reliability of structured data and deterministic computation.

🚀 Key Capabilities
📦 1. Data Engineering

The platform processes the M5 Forecasting – Accuracy Dataset, containing more than 58 million historical sales records after transformation.

The ETL pipeline performs:

Raw data ingestion
Data validation
Data cleaning
Wide-to-long transformation
Feature preparation
Chunk-based processing
Relational data loading
MySQL warehouse population

The large sales dataset is processed in chunks rather than attempting to load the complete dataset into memory at once.

🗄️ 2. MySQL Data Warehouse

Processed retail data is stored in a structured MySQL data warehouse.

The warehouse contains:

Dimension Tables
calendar_dim
item_dim
store_dim
Fact Tables
sales_fact
price_fact
Analytical Tables
analytics_monthly_sales
analytics_store_performance
analytics_category_performance
analytics_department_performance
analytics_product_performance
analytics_weekday_sales
analytics_sales_summary
analytics_sales_distribution
analytics_price_summary

The database provides a centralized source for:

Analytics
Forecasting
SQL queries
AI tools
Business intelligence
📊 3. Business Analytics

The analytics layer provides deterministic business insights directly from the MySQL warehouse.

Current analytical capabilities include:

Overall sales summary
Monthly sales trends
Store performance
Product performance
Category performance
Department performance
Weekday sales patterns
Price statistics
Sales distributions

These results are exposed through FastAPI endpoints and visualized through the React frontend.

📈 4. Demand Forecasting

The forecasting framework provides a common workflow for evaluating multiple forecasting approaches.

The project includes:

Classical Forecasting
Statistical time-series approaches
Baseline forecasting
Model evaluation
Deep Learning
Neural-network based forecasting approaches
Transformer Forecasting
Transformer-based time-series models

Models are evaluated using a common forecasting workflow so that their performance can be compared using consistent evaluation procedures.

The forecasting system also supports generating future demand forecasts through the application.

🤖 5. Generative AI

Generative AI is used as an interpretation and reasoning layer rather than as the source of raw numerical data.

LLM functionality supports:

Natural-language business questions
Forecast interpretation
Business explanations
Cross-domain reasoning
Executive summaries
Report generation
Agent orchestration

The current implementation uses Google Gemini.

📚 6. Retrieval-Augmented Generation

The platform includes a RAG subsystem for incorporating business knowledge that may not exist inside the structured sales database.

The pipeline follows:

Business Documents
       ↓
Document Loading
       ↓
Chunking
       ↓
Embeddings
       ↓
FAISS Vector Store
       ↓
Semantic Retrieval
       ↓
Relevant Context
       ↓
LLM
       ↓
Grounded Response

RAG allows the system to combine:

Structured Data
      +
Business Knowledge
      +
LLM Reasoning

rather than relying exclusively on the language model's internal knowledge.

🧠 7. Multi-Agent AI

The platform uses specialized agents for different business responsibilities.

Agent	Responsibility
Forecast Agent	Forecasting models and demand predictions
Analytics Agent	Sales trends, stores, products and KPIs
Inventory Agent	Inventory and replenishment intelligence
SQL Agent	Database and SQL-oriented questions
Executive Agent	Cross-domain business synthesis

A query router determines which agent or agents should handle a question.

For example:

"What is the monthly sales trend?"
                ↓
        Analytics Agent
"What does future demand look like?"
                ↓
         Forecast Agent
"Which products should we prioritize?"
                ↓
         Inventory Agent

For broader questions, multiple agents can contribute and the Executive Agent can synthesize their findings into a single response.

🏗️ System Architecture

The high-level architecture is:

                         ┌──────────────────┐
                         │       User       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ React Frontend   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   FastAPI API    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  Query Engine    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Task Router    │
                         └────────┬─────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
      │  Forecast   │      │  Analytics  │      │  Inventory  │
      │    Agent    │      │    Agent    │      │    Agent    │
      └──────┬──────┘      └──────┬──────┘      └──────┬──────┘
             │                    │                    │
             ▼                    ▼                    ▼
      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
      │ Forecasting │      │   MySQL     │      │    MySQL    │
      │   Models    │      │  Warehouse  │      │  Warehouse  │
      └──────┬──────┘      └──────┬──────┘      └──────┬──────┘
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Real Results   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Executive Agent │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Business Answer  │
                         └──────────────────┘

The architecture separates:

Data ingestion
Data storage
Analytics
Forecasting
Deterministic tools
AI reasoning
Agent orchestration
API services
User interface

This makes individual components easier to test, replace, and extend.

🖥️ React Application

The frontend is built using:

React
Vite
React Router
Axios
Recharts
React Markdown
Lucide React

The application currently provides:

Dashboard

Provides an overview of:

Total sales
Sales records
Average sale
Store performance
Category performance
Monthly sales trends
Forecast overview
Quick actions
Forecasting

Provides:

Forecasting service status
Forecasting queries
Forecast results
AI-generated forecast interpretation
Example forecasting questions
Analytics

Provides interactive visualizations for:

Monthly sales
Store performance
Category performance
Department performance
Weekday sales
Top products
AI Chat

Provides a natural-language interface for interacting with the intelligence platform.

Users can ask business questions without directly writing SQL.

Agents

Provides a visual explanation of the multi-agent architecture, including:

Query Router
Analytics Agent
Forecast Agent
Inventory Agent
SQL Agent
Executive Response
🌐 FastAPI Backend

The backend exposes the intelligence platform through a REST API.

Core Endpoints
Method	Endpoint	Purpose
GET	/health	Service health check
POST	/chat	Natural-language business questions
POST	/forecast	Forecasting intelligence
POST	/analytics	AI-assisted analytics
POST	/report	Executive reporting
Deterministic Analytics Endpoints
Method	Endpoint	Purpose
GET	/analytics/summary	Overall sales summary
GET	/analytics/monthly-sales	Monthly sales
GET	/analytics/top-stores	Store performance
GET	/analytics/category-performance	Category performance
GET	/analytics/department-performance	Department performance
GET	/analytics/top-products	Top product performance
GET	/analytics/weekday-sales	Weekday sales patterns

Interactive API documentation is available through:

http://127.0.0.1:8000/docs
📊 Dataset

The project uses the:

M5 Forecasting – Accuracy Dataset

The dataset contains:

Products
Stores
Departments
Categories
Historical sales
Calendar information
Product prices

The processed warehouse contains more than:

58,000,000+

sales records.

The raw dataset is not included in the repository because of its size.

Required files:

sales_train_validation.csv
calendar.csv
sell_prices.csv

Place them inside:

data/raw/
📂 Project Structure
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
├── artifacts/
│   ├── benchmarks/
│   ├── faiss/
│   ├── metadata/
│   ├── models/
│   ├── prompts/
│   └── reports/
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
│   ├── milestone_10_fastapi/
│   └── milestone_11_react/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
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
│   ├── analytics/
│   ├── api/
│   ├── config/
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
│   ├── forecasting/
│   ├── query/
│   ├── rag/
│   ├── tools/
│   └── transformers/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── ...

Local credentials and API keys are stored outside version control and should never be committed.

📁 Important Directories
Directory	Purpose
src/etl/	Data extraction, transformation and loading
src/database/	MySQL connection and database utilities
src/analytics/	Business analytics services
src/forecasting/	Forecasting models and evaluation
src/ai/agents/	Specialized AI agents
src/ai/tools/	Deterministic tools used by agents
src/ai/query/	Natural-language query orchestration
src/ai/rag/	Retrieval-Augmented Generation
src/api/	FastAPI application and routes
frontend/	React business intelligence interface
tests/	Automated tests
docs/	Milestone documentation
artifacts/	Models, embeddings, reports and experiment outputs
💻 Requirements

Before running the project locally, install:

Requirement	Version
Python	3.12.x
MySQL	8.0+
Node.js	20+
npm	Included with Node.js
Git	Latest stable version

You will also need:

The M5 dataset
A running MySQL server
A Google Gemini API key for AI functionality

Python dependencies are provided through:

requirements.txt

Frontend dependencies are provided through:

frontend/package.json
⚙️ Local Setup
1. Clone the Repository
git clone <repository-url>
cd AI-demand-intelligence-platform
2. Create the Python Environment
Option A — Conda
conda create -p venv python=3.12 -y
conda activate ./venv
Option B — Python Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux / macOS:

python3 -m venv venv
source venv/bin/activate
3. Install Python Dependencies
pip install -r requirements.txt

Verify the environment:

pip check

The project should report:

No broken requirements found.
🗄️ 4. Configure MySQL

Install and start MySQL 8.0+.

Create the database:

CREATE DATABASE demand_intelligence;

The project expects database configuration through:

configs/database.yaml

A safe template is provided at:

configs/database.example.yaml

Example:

database:
  host: localhost
  port: 3306
  user: your_username
  password: your_password
  database: demand_intelligence

Do not commit real database credentials.

📊 5. Add the M5 Dataset

Download the M5 Forecasting – Accuracy dataset.

Place:

sales_train_validation.csv
calendar.csv
sell_prices.csv

inside:

data/raw/

The ETL workflow is documented in:

docs/milestone_01_etl/

The resulting warehouse contains the processed retail data used by the rest of the application.

The complete raw dataset and populated MySQL database are not included in the Git repository because of their size.

🔐 6. Configure Gemini

AI-powered functionality requires a Google Gemini API key.

Configure the local environment according to the project's configuration files.

For example, local environment variables can include:

GEMINI_API_KEY=your_api_key
LLM_PROVIDER=gemini
LLM_MODEL=models/gemini-3.1-flash-lite

Database environment variables can also be configured locally:

DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=demand_intelligence

Keep .env out of Git.

Never commit:

Gemini API keys
Database passwords
Authentication secrets
Cloud credentials
🌐 7. Start the Backend

Activate the Python environment and run:

python -m uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000

The backend will be available at:

http://127.0.0.1:8000

Health check:

http://127.0.0.1:8000/health

Swagger API documentation:

http://127.0.0.1:8000/docs

OpenAPI specification:

http://127.0.0.1:8000/openapi.json
🖥️ 8. Start the React Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Vite will display the local frontend URL in the terminal.

The frontend communicates with the FastAPI backend and provides:

Dashboard
Forecasting
Analytics
AI Chat
Agents
📦 Production Frontend Build

To create a production build:

cd frontend
npm run build

To preview the production build locally:

npm run preview

The production build is generated in:

frontend/dist/
🧪 Testing

The project contains automated tests covering major components of the platform.

Run API tests:

python -m pytest tests/api -v

Run the complete test suite:

python -m pytest -v

For debugging:

python -m pytest -x -vv

The API tests cover the major application interfaces, including:

/health
/chat
/forecast
/analytics
/report

Some forecasting-related tests can take longer because they execute real forecasting workflows.

Third-party library warnings do not necessarily indicate test failures.

🔒 Security

The repository intentionally does not contain production credentials.

Never commit:

Database passwords
Gemini API keys
Cloud credentials
Authentication secrets
Private configuration

Use local configuration files and environment variables instead.

Example configuration files such as:

configs/database.example.yaml

can safely be committed because they contain placeholders rather than real credentials.

🧭 Development Approach

The project was developed incrementally through separate milestones:

Business Understanding
        ↓
ETL + MySQL
        ↓
EDA
        ↓
Classical Forecasting
        ↓
Deep Learning
        ↓
Transformer Forecasting
        ↓
LLM Integration
        ↓
RAG
        ↓
Multi-Agent AI
        ↓
FastAPI
        ↓
React Frontend

Each major stage has its own documentation under:

docs/

The root README intentionally focuses on:

Project overview
Architecture
Capabilities
Setup
Usage
Current status

while the milestone documentation contains detailed implementation decisions and technical explanations.

📚 Milestone Documentation

Detailed documentation is available for the individual development stages:

docs/business_case/

docs/milestone_01_etl/

docs/milestone_02_eda/

docs/milestone_03_forecasting/

docs/milestone_04_deep_learning/

docs/milestone_05_transformers/

docs/milestone_06_llm/

docs/milestone_07_rag/

docs/milestone_09_multi_agent/

docs/milestone_10_fastapi/

docs/milestone_11_react/
📌 Current Status
Component	Status
Business Understanding	✅ Complete
ETL Pipeline	✅ Complete
MySQL Data Warehouse	✅ Complete
Exploratory Data Analysis	✅ Complete
Classical Forecasting	✅ Complete
Deep Learning Forecasting	✅ Complete
Transformer Forecasting	✅ Complete
LLM Integration	✅ Complete
RAG	✅ Complete
Multi-Agent AI	✅ Complete
Query Engine	✅ Complete
FastAPI Backend	✅ Complete
React Frontend	✅ Complete
API Integration	✅ Complete
Frontend Linting	✅ Passing
Frontend Production Build	✅ Passing
Docker	❌ Not Used
Cloud Deployment	⬜ Future Work
Production MLOps	⬜ Future Work
🌟 Why This Project Matters

The primary value of this project is not simply the number of technologies used.

The important part is the integration of the complete decision-making pipeline:

Large-Scale Retail Data
          ↓
      Data Engineering
          ↓
     Data Warehouse
          ↓
 Analytics + Forecasting
          ↓
       AI + RAG
          ↓
    Multi-Agent System
          ↓
      FastAPI API
          ↓
    React Interface
          ↓
 Natural-Language Interaction

A user can interact with the platform at the business level while the underlying system handles:

Data retrieval
SQL
Analytics
Forecasting
Knowledge retrieval
Agent selection
Model interpretation
Business reasoning
Report generation

This turns the project from an isolated forecasting experiment into an integrated AI-enabled retail intelligence system.

🛣️ Future Roadmap

The core application is currently complete through the React frontend.

Future development can focus on productionization and MLOps rather than additional application features.

Completed
✅ Data Engineering
✅ MySQL Data Warehouse
✅ Business Analytics
✅ Classical Forecasting
✅ Deep Learning Forecasting
✅ Transformer Forecasting
✅ Generative AI
✅ RAG
✅ Multi-Agent AI
✅ Query Engine
✅ FastAPI Backend
✅ React Frontend
✅ API Integration
✅ Frontend Build
Future Work
⬜ MLflow Experiment Tracking
⬜ CI/CD Pipeline
⬜ Model Monitoring
⬜ Data Quality Monitoring
⬜ Production MLOps
⬜ Cloud Deployment
⬜ Automated Model Retraining

Dockerized deployment is intentionally not part of the project roadmap. The current application is designed to run natively using Python, MySQL, FastAPI, Node.js, and React.

🏷️ Current Release

The current completed application release is:

v12.0.0

This release represents the completion of the native application integration, including:

Backend
    +
MySQL
    +
AI / RAG / Agents
    +
FastAPI
    +
React Frontend

The project is maintained on the main branch.