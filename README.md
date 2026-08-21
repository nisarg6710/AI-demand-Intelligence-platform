📊 AI Demand Intelligence Platform

An end-to-end AI-powered retail demand intelligence platform that transforms large-scale sales data into forecasting insights, business analytics, and natural-language decision support.

The AI Demand Intelligence Platform combines data engineering, time-series forecasting, machine learning, generative AI, RAG, multi-agent systems, and a React dashboard into a single application.

Instead of requiring a business user to work directly with SQL queries, forecasting models, notebooks, or analytical dashboards, the platform provides a natural-language interface for interacting with business data and AI capabilities.

🎯 What Problem Does This Solve?

Retail organizations generate large amounts of sales and operational data, but turning that data into useful decisions requires multiple disconnected systems.

A typical workflow might involve:

Raw Data
   ↓
ETL Pipeline
   ↓
Database
   ↓
SQL / Analytics
   ↓
Forecasting Models
   ↓
Reports

This creates a usability gap.

A business user may want to ask:

Which stores are performing best?
What is the monthly sales trend?
Which products are selling fastest?
What is the best forecasting model?
What are the biggest business risks?
Give me an executive summary of the current situation.

The user should not need to know SQL, machine-learning implementation details, or database structure to obtain these answers.

The goal of this project is therefore:

Build a unified, data-grounded intelligence platform that allows business users to interact with retail data, forecasting models, analytics, and domain knowledge through natural language.

💡 What Is the Solution?

The platform creates a complete pipeline:

Retail Data
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

The important design principle is that LLMs are not treated as the source of numerical truth.

Instead:

User Question
     ↓
Task Router
     ↓
Specialized Agent
     ↓
Deterministic Tool
     ↓
Database / Model / Knowledge Base
     ↓
Real Results
     ↓
LLM Interpretation
     ↓
Business Answer

This allows the system to combine the flexibility of natural-language AI with the reliability of structured data and deterministic tools.

🚀 What Can the Platform Do?
📦 Data Engineering
Process the M5 retail dataset containing 58M+ sales records
Validate and transform raw data
Perform chunk-based ETL
Load structured data into MySQL
Maintain a centralized data warehouse
📊 Business Analytics

The analytics layer provides insights into:

Sales trends
Monthly sales
Store performance
Product performance
Categories and departments
Business KPIs
Historical demand
📈 Demand Forecasting

The forecasting framework supports multiple approaches, including:

Classical time-series models
Deep-learning models
Transformer-based forecasting models

Models can be evaluated and compared through a common forecasting workflow.

🤖 Generative AI

LLMs are used for:

Forecast interpretation
Business explanations
Natural-language interaction
Report generation
Agent reasoning
📚 Retrieval-Augmented Generation

The RAG subsystem combines:

Business Documents
       ↓
Chunking
       ↓
Embeddings
       ↓
FAISS
       ↓
Semantic Retrieval
       ↓
Relevant Context
       ↓
LLM
       ↓
Grounded Response

This allows the system to incorporate information that is not contained in the structured sales database.

🧠 Multi-Agent Intelligence

The platform contains specialized agents for different business responsibilities:

Agent	Responsibility
Forecast Agent	Forecasting models and demand predictions
Analytics Agent	Sales trends, stores, products and KPIs
Inventory Agent	Inventory and replenishment intelligence
SQL Agent	Database and SQL-oriented questions
Executive Agent	Cross-domain business synthesis

A Task Router determines which agent should handle a user's question.

For example:

"What is the best forecasting model?"
              ↓
       Forecast Agent
"Which stores are performing best?"
              ↓
       Analytics Agent
"Which products should we prioritize?"
              ↓
       Inventory Agent

For broader questions, multiple agents can contribute and the Executive Agent synthesizes their findings.

🏗️ System Architecture

At a high level:

                    User
                     │
                     ▼
             React Dashboard
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
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Forecast   Analytics   Inventory
       Agent       Agent       Agent
          │          │          │
          ▼          ▼          ▼
       Models      MySQL      MySQL
          │          │          │
          └──────────┼──────────┘
                     ▼
               Real Results
                     │
                     ▼
             Executive Agent
                     │
                     ▼
              Business Answer

The system separates:

Data access
Analytics
Forecasting
AI reasoning
Agent orchestration
API services
User interface

This makes individual components easier to test, replace, and extend.

🗄️ Data & Database

The project uses the M5 Forecasting – Accuracy Dataset as its primary retail dataset.

The dataset contains information about:

Products
Stores
Departments
Categories
Historical sales
Calendar information
Prices

The processed data is stored in a MySQL data warehouse.

The database contains structured dimensions and fact tables used by:

Analytics
Forecasting
SQL queries
Inventory intelligence
AI agents

The raw M5 dataset is not included in the repository because of its size.

Required files:

sales_train_validation.csv
calendar.csv
sell_prices.csv

Place them in:

data/raw/
📂 Project Structure

The repository is organized around the different stages of the platform:

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
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .gitignore
Important directories
Directory	Purpose
src/etl/	Data extraction, validation and loading
src/database/	MySQL connection and schema
src/analytics/	Business analytics services
src/forecasting/	Forecasting models and evaluation
src/ai/agents/	Specialized AI agents
src/ai/tools/	Deterministic tools used by agents
src/ai/query/	Natural-language query orchestration
src/ai/rag/	Retrieval-Augmented Generation
src/api/	FastAPI application and routes
frontend/	React business intelligence interface
tests/	Automated tests
docs/	Detailed milestone documentation
artifacts/	Models, reports, embeddings and experiment outputs
💻 Requirements

Before running the project locally, install:

Requirement	Recommended
Python	3.12.x
MySQL	8.0+
Node.js	20+
npm	Included with Node.js
Git	Latest stable version

You will also need:

The M5 dataset
A running MySQL server
A Google Gemini API key for LLM-powered functionality

Python dependencies are provided in:

requirements.txt

Frontend dependencies are provided in:

frontend/package.json
⚙️ Local Setup
1. Clone the repository
git clone <repository-url>
cd AI-demand-intelligence-platform
2. Create the Python environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python -m venv venv
source venv/bin/activate
3. Install Python dependencies
pip install -r requirements.txt
🗄️ 4. Configure MySQL

Create the MySQL database using:

src/database/schema.sql

The project expects a database configuration at:

configs/database.yaml

A safe template is provided as:

configs/database.example.yaml

Example:

database:
  host: localhost
  user: your_username
  password: your_password
  database: demand_intelligence

Do not commit real database credentials.

📊 5. Add the M5 Dataset

Download the M5 Forecasting – Accuracy dataset and place:

sales_train_validation.csv
calendar.csv
sell_prices.csv

inside:

data/raw/

Then run the ETL pipeline described in:

docs/milestone_01_etl/
🔐 6. Configure Gemini

LLM-powered functionality requires a Gemini API key.

Configure the local LLM settings in:

configs/llm.yaml

Keep credentials out of Git.

🌐 7. Start the Backend

Activate the virtual environment and run:

uvicorn src.api.main:app --reload

The backend will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
🖥️ 8. Start the React Frontend

Open another terminal:

cd frontend
npm install
npm run dev

The Vite development server will provide the frontend URL shown in the terminal.

The frontend communicates with the FastAPI backend to provide:

Dashboard
Forecasting
Analytics
AI Chat
Agent architecture
📦 Production Frontend Build

To create a production build:

cd frontend
npm run build

To locally preview the production build:

npm run preview
🧪 Testing

The project includes automated tests across the major system components.

For the API integration tests:

python -m pytest tests/api -v

The API suite validates:

/health
/chat
/forecast
/analytics
/report

The complete test suite can be executed with:

python -m pytest -v

Use:

python -m pytest -x -vv

when debugging failures.

Note: Some forecasting/report tests can take significantly longer because they execute real forecasting workflows. Warnings from third-party libraries do not necessarily indicate test failures.

🔌 API

The FastAPI backend currently exposes:

Endpoint	Purpose
GET /health	Service health check
POST /chat	General natural-language business questions
POST /forecast	Forecasting intelligence
POST /analytics	Business analytics
POST /report	Executive reporting

Interactive API documentation is available through:

/ docs

when the backend is running.

🔒 Security

The repository intentionally does not store production credentials.

Never commit:

Database passwords
Gemini API keys
Cloud credentials
Authentication secrets
Other sensitive configuration

Local configuration files should remain excluded through .gitignore.

Template configuration files such as:

configs/database.example.yaml

can safely be committed.

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

The root README intentionally provides the high-level picture and setup instructions, while the milestone documentation contains the implementation details.

📚 Milestone Documentation

Detailed technical documentation is available for each stage:

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
ETL & MySQL Warehouse	✅ Complete
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
API Integration Tests	✅ Passing
Deployment / MLOps	🚧 Next Stage
🌟 Why This Project Matters

The main value of this project is not simply combining many technologies.

The important part is the integration of the entire decision-making pipeline:

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
 Natural-Language Decisions

This transforms the project from a standalone forecasting experiment into a complete AI-enabled business intelligence system.

The user interacts with the platform at the business level, while the underlying system handles:

Data retrieval
SQL
Analytics
Forecasting
Knowledge retrieval
Agent selection
Model interpretation
Report generation

The result is a system designed to make complex data-science capabilities more accessible, explainable, and actionable for business users.

🗺️ Roadmap

The core application is now complete through the React frontend.

Completed
✅ Data Engineering
✅ MySQL Data Warehouse
✅ Analytics
✅ Forecasting
✅ Deep Learning
✅ Transformers
✅ LLM
✅ RAG
✅ Multi-Agent AI
✅ FastAPI
✅ React Frontend
Next
⬜ Dockerized Deployment
⬜ CI/CD
⬜ MLflow / Experiment Tracking
⬜ Monitoring
⬜ Cloud Deployment
⬜ Production MLOps