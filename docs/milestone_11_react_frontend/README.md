# Milestone 11 — React Frontend

## Overview

Milestone 11 introduces the React-based frontend for the AI Demand Intelligence Platform.

The frontend provides a unified interface for interacting with the platform's analytics, forecasting, conversational AI, and multi-agent capabilities.

The frontend communicates with the FastAPI backend through a centralized API service layer.

---

## Objectives

- Build a production-ready React frontend.
- Provide dedicated pages for major platform capabilities.
- Connect the frontend to the FastAPI backend.
- Visualize historical sales and forecasting information.
- Provide natural-language interfaces for analytics and forecasting.
- Expose the multi-agent architecture through a dedicated interface.
- Validate the frontend using both development and production builds.

---

## Frontend Architecture

```text
React Frontend
│
├── Dashboard
│   ├── KPI metrics
│   ├── Monthly sales visualization
│   ├── Forecast intelligence
│   └── Quick actions
│
├── Analytics
│   ├── Natural-language analytics
│   ├── Monthly sales trend
│   └── AI-generated insights
│
├── Forecasting
│   ├── Forecasting questions
│   ├── Model selection
│   ├── Future predictions
│   └── Forecast analysis
│
├── Chat
│   └── Natural-language interaction with AI services
│
└── Agents
    └── Multi-agent architecture visualization


Pages
Dashboard

Provides a high-level overview of the platform.

Includes:

Total revenue
Total sales
Active products
Store count
Monthly sales trend
Forecast intelligence
Quick navigation actions
Analytics

Provides natural-language access to historical business analytics.

Supported capabilities include:

Sales summaries
Monthly sales trends
Store performance
AI-generated business insights

Example questions:

Give me a sales summary.


Show me the monthly sales trend.


Which stores are performing best?
Forecasting

Provides access to the demand forecasting services.

The page supports:

Forecasting questions
Best-model identification
Future demand predictions
Forecast interpretation
Business recommendations

Example:

Forecast demand for the next 12 months.
Chat

Provides a conversational interface for interacting with the platform's AI capabilities.

The backend router determines which specialist agent or service should handle the user's question.

Agents

Provides a visual representation of the multi-agent architecture.

The architecture consists of:

User Question
      ↓
Task Router
      ↓
Specialist Agents
      ↓
Executive Synthesis
      ↓
Business Insight

Specialized components include:

Analytics Agent
Forecast Agent
Inventory Agent
SQL Agent
Executive Agent
API Communication

Frontend-backend communication is centralized in:

frontend/src/services/api.js

The service layer communicates with the FastAPI backend using Axios.

Primary endpoints include:

POST /analytics
POST /forecast
POST /chat
POST /report


GET /health


GET /analytics/monthly-sales
GET /analytics/summary
GET /analytics/top-stores
GET /analytics/category-performance

Centralizing API communication keeps backend integration separate from page-level UI logic.

Visualization

The frontend uses Recharts for data visualization.

The primary visualization implemented in this milestone is the historical monthly sales trend.

The chart is populated directly from the backend analytics service:

MySQL
   ↓
Analytics Service
   ↓
FastAPI
   ↓
Axios
   ↓
React
   ↓
Recharts
AI Integration

The frontend does not directly execute machine-learning or LLM logic.

Instead:

React
  ↓
FastAPI
  ↓
AI Agents / Services
  ↓
Tools / Database / Forecasting Models
  ↓
AI Response
  ↓
React

This separation keeps business logic and model execution on the backend while the frontend focuses on presentation and user interaction.

Validation
Backend Tests

The complete backend test suite was executed using:

python -m pytest -x -vv

Result:

5 passed

Tested endpoints:

Analytics
Chat
Forecast
Health
Report
Frontend Production Build

The production build was validated using:

npm run build

Result:

✓ built

The Vite build completed successfully.

A chunk-size warning was reported by Vite, but it does not prevent production builds and was not treated as a functional issue for this milestone.

Production Preview

The production frontend was also tested using:

npm run preview

The frontend successfully communicated with the FastAPI backend after resolving the development/preview CORS configuration.

Technologies
React
Vite
Axios
Recharts
React Markdown
Lucide React
Tailwind/CSS-based application styling
FastAPI backend
Outcome

Milestone 11 establishes the user-facing application layer of the AI Demand Intelligence Platform.

The platform now provides a unified interface through which users can:

Explore historical business data.
Analyze sales trends.
Interact with forecasting models.
Ask natural-language business questions.
Access AI-generated insights.
Understand the underlying multi-agent architecture.

The frontend is integrated with the existing data, analytics, forecasting, and AI backend services.



---


## 11.13 — Don't Commit Yet


After creating that README, run:


```bash
git status

Then:

git diff --stat

We should see the new documentation in addition to the existing changes.