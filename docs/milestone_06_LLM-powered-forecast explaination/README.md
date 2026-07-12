# 🧠 Milestone 6 — LLM-powered Forecast Explanation

## Overview

Traditional forecasting systems generate numerical predictions but leave business users with an important question:

> **Why is demand expected to increase or decrease?**

This milestone transforms numerical forecasts into **natural language business explanations** using a Large Language Model (LLM).

Instead of presenting only charts and evaluation metrics, the system analyzes forecast trends, seasonality, and statistical properties, then generates executive-ready business reports.

---

# 🎯 Objectives

The goals of this milestone are:

- Make forecasting results explainable
- Generate business-friendly insights
- Produce executive-ready reports
- Automate report generation
- Build a reusable LLM pipeline
- Prepare the project for Retrieval-Augmented Generation (RAG)

---

# 🏗 Architecture

```text
Forecast
    │
    ▼
Metadata Builder
    │
    ▼
Prompt Builder
    │
    ▼
Gemini Client
    │
    ▼
Forecast Explainer
    │
    ▼
Markdown Report
    │
    ▼
HTML Report
```

---

# 📂 Module Structure

```text
src/
└── ai/
    ├── metadata.py
    ├── trend.py
    ├── seasonality.py
    ├── statistics.py
    ├── explainer.py
    ├── pipeline.py
    │
    ├── llm/
    │   └── gemini_client.py
    │
    ├── prompts/
    │   ├── prompt_builder.py
    │   └── templates.py
    │
    ├── report.py
    ├── html_report.py
    ├── metadata_writer.py
    └── prompt_writer.py
```

---

# 🧩 Components

## 1. Forecast Metadata Builder

The metadata layer extracts structured information from forecasts before sending anything to the LLM.

Generated metadata includes:

- Trend direction
- Growth percentage
- Average forecast
- Weekly seasonality detection
- Seasonality strength
- Forecast statistics
- Demand volatility

Example:

```json
{
    "trend": {
        "direction": "Increasing",
        "growth_percent": 9.12
    },
    "seasonality": {
        "weekly_seasonality": false
    },
    "statistics": {
        "mean": 136.4,
        "std_dev": 5.46
    }
}
```

---

## 2. Prompt Builder

Instead of sending raw JSON to the LLM, the project constructs structured prompts using:

- System Prompt
- User Prompt

This ensures:

- Consistent responses
- Better reasoning
- Stable report formatting

---

## 3. Gemini Client

The project integrates Google's latest Gemini models through the official `google-genai` SDK.

Configuration is externalized through:

```text
configs/llm.yaml
```

making it easy to switch models without changing application code.

---

## 4. Forecast Explainer

The Forecast Explainer orchestrates the complete explanation workflow.

Pipeline:

```text
Forecast
    │
    ▼
Metadata
    │
    ▼
Prompt Generation
    │
    ▼
Gemini
    │
    ▼
Business Explanation
```

The output contains:

- Metadata
- Generated prompts
- Business explanation
- Markdown report
- HTML report

---

## 5. Report Generation

Every explanation is automatically saved as:

### Markdown

```text
artifacts/reports/
```

### HTML

```text
artifacts/reports/
```

The reports are timestamped to preserve historical runs.

Example:

```text
forecast_report_20260712_194530.md

forecast_report_20260712_194530.html
```

---

## 6. Prompt Persistence

The exact prompts sent to the LLM are preserved for reproducibility.

Stored under:

```text
artifacts/prompts/
```

Example:

```text
system_prompt_20260712_194530.txt

user_prompt_20260712_194530.txt
```

---

## 7. Metadata Persistence

Structured forecast metadata is automatically stored as JSON.

Example:

```text
artifacts/metadata/

metadata_20260712_194530.json
```

This enables:

- Debugging
- Prompt tuning
- Experiment reproducibility

---

## 8. Logging

Pipeline execution is logged using Python's logging module.

Logs include:

- Metadata creation
- Prompt generation
- LLM execution
- Report generation

Stored in:

```text
logs/project.log
```

---

# 📋 Example Output

The generated report includes:

- Executive Summary
- Trend Analysis
- Seasonality Analysis
- Forecast Statistics
- Business Interpretation
- Inventory Recommendations

Example:

```text
Executive Summary

Demand is expected to increase steadily over the forecast horizon.

Trend Analysis

Demand is projected to grow by approximately 9%.

Seasonality Analysis

No significant weekly seasonality was detected.

Inventory Recommendations

Increase inventory gradually while maintaining lean safety stock.
```

---

# 🚀 Running the Pipeline

Execute:

```bash
python -m tests.llm.test_pipeline
```

Generated artifacts:

```text
artifacts/
│
├── metadata/
│
├── prompts/
│
├── reports/
│
└── logs/
```

---

# ✨ Key Features

- AI-powered business explanations
- Explainable forecasting
- Prompt engineering
- Automatic report generation
- Markdown export
- HTML export
- Metadata persistence
- Prompt persistence
- Timestamped artifacts
- Modular pipeline architecture

---

# 📈 Business Value

Instead of presenting only numerical forecasts, the platform answers questions such as:

- Why is demand increasing?
- Is seasonality affecting sales?
- How stable is demand?
- What inventory strategy should be adopted?
- What are the operational risks?

This bridges the gap between technical forecasting models and actionable business insights.

---

# ✅ Deliverables

- Forecast Metadata Builder
- Trend Analyzer
- Seasonality Analyzer
- Statistics Analyzer
- Prompt Builder
- Gemini Integration
- Forecast Explainer
- Markdown Report Generator
- HTML Report Generator
- Metadata Writer
- Prompt Writer
- Forecast Explanation Pipeline
- Timestamped Artifact Management

---

# 🎯 Next Milestone

**Milestone 7 — Retrieval-Augmented Generation (RAG)**

The next milestone enriches explanations using external business knowledge retrieved from a vector database.

Future architecture:

```text
Forecast
      │
      ▼
Metadata
      │
      ▼
Retriever
      │
      ▼
Business Knowledge
      │
      ▼
Prompt Builder
      │
      ▼
LLM
      │
      ▼
Context-Aware Business Explanation
```