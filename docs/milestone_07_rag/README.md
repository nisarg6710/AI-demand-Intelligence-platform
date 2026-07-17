# 📚 Milestone 7 — Retrieval-Augmented Generation (RAG)

> **Production-grade Retrieval-Augmented Generation (RAG) pipeline for AI-powered demand intelligence.**

---

# 🎯 Objective

The previous milestone introduced Large Language Models (LLMs) to explain forecasting results in natural language.

However, LLMs alone cannot answer questions about historical reports, inventory policies, or previous business knowledge because they have no access to project-specific documents.

This milestone solves that problem by implementing a **Retrieval-Augmented Generation (RAG)** system.

Instead of relying solely on the LLM's pre-trained knowledge, the system retrieves relevant business documents from a local knowledge base and provides them as context before generating an answer.

---

# ❓ Business Problem

Business managers frequently ask questions such as:

- Have we seen this demand pattern before?
- Which inventory policy applies to this product?
- What recommendations were made in previous forecast reports?
- How should increasing demand be handled?
- What does our retail market report recommend?

Without document retrieval, an LLM would either:

- hallucinate information,
- rely on general knowledge,
- or be unable to answer accurately.

RAG enables the system to answer using **company-specific knowledge**.

---

# 💡 Solution

A complete Retrieval-Augmented Generation pipeline was implemented using:

- Document Loader
- Text Chunking
- Sentence Embeddings
- FAISS Vector Database
- Semantic Retrieval
- Context Builder
- Prompt Engineering
- Gemini LLM Integration

The LLM now answers questions **grounded in retrieved business documents**.

---

# 🏗 Architecture

```text
Business Documents
        │
        ▼
Document Loader
        │
        ▼
Text Chunking
        │
        ▼
Sentence Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Semantic Retriever
        │
        ▼
Context Builder
        │
        ▼
Prompt Builder
        │
        ▼
Gemini LLM
        │
        ▼
Business Answer
```

---

# 📂 Knowledge Base

The RAG system currently indexes three document categories.

## Forecast Reports

Generated automatically from previous forecasting experiments.

Contains:

- Demand trends
- Business summaries
- Forecast explanations
- Inventory recommendations

---

## Inventory Policies

Business policy documents including:

- Replenishment strategies
- Safety stock rules
- Seasonal inventory guidelines
- Procurement recommendations

---

## Retail Market Reports

Business reports describing:

- Historical demand patterns
- Promotional effects
- Seasonal demand
- Market recommendations

---

# 📦 Project Structure

```text
knowledge_base/
│
├── forecast_reports/
│
├── inventory_policies/
│
└── retail_reports/

src/
└── ai/
    └── rag/
        ├── document_loader.py
        ├── text_chunker.py
        ├── embedding_generator.py
        ├── vector_store.py
        ├── retriever.py
        ├── context_builder.py
        └── pipeline.py

artifacts/
└── faiss/
    ├── index.faiss
    └── metadata.pkl
```

---

# ⚙ Pipeline Components

## 1. Document Loader

Loads Markdown documents from the knowledge base.

Supported categories:

- Forecast Reports
- Inventory Policies
- Retail Reports

---

## 2. Text Chunker

Splits long documents into overlapping chunks.

Benefits:

- Better retrieval accuracy
- Improved semantic search
- Reduced context loss

---

## 3. Embedding Generator

Each chunk is converted into a dense vector using:

**SentenceTransformer**

```
all-MiniLM-L6-v2
```

Embedding size:

```
384 dimensions
```

---

## 4. FAISS Vector Database

Embeddings are indexed using:

```
IndexFlatL2
```

The vector database enables efficient semantic similarity search.

Stored artifacts:

```
artifacts/faiss/
    index.faiss
    metadata.pkl
```

---

## 5. Retriever

Given a user question:

1. Generate embedding
2. Search FAISS
3. Retrieve Top-K similar chunks

The retriever returns:

- document
- category
- similarity score
- retrieved text

---

## 6. Context Builder

Retrieved chunks are merged into a structured context before being passed to the LLM.

Each section includes:

- Source document
- Category
- Retrieved content

---

## 7. Prompt Builder

A dedicated RAG prompt template instructs the LLM to:

- Answer only using retrieved knowledge
- Avoid hallucinations
- Reference retrieved documents
- Produce business-friendly explanations

---

## 8. RAG Pipeline

The complete orchestration layer performs:

Question

↓

Retrieve Documents

↓

Build Context

↓

Construct Prompt

↓

Gemini Response

↓

Business Answer

---

# 🤖 Interactive AI Assistant

An interactive command-line assistant was implemented.

Example:

```text
Retail Demand Intelligence Assistant

> Have we seen this demand pattern before?

Answer:
...

Sources:
forecast_report.md
inventory_policy.md
```

Users can ask arbitrary business questions.

---

# 📊 Example Questions

Examples include:

- Have we seen this pattern before?
- Which inventory policy applies?
- What recommendations were made previously?
- What does the retail report recommend?
- Should safety stock be increased?
- How should increasing demand be handled?

---

# 🧪 Testing

Implemented tests include:

```text
test_document_loader.py

test_chunker.py

test_embeddings.py

test_vector_store.py

test_retriever.py

test_context_builder.py

test_rag_prompt.py

test_rag_pipeline.py

rag_assistant.py
```

---

# 🚀 Key Features

- Production-ready RAG architecture
- Modular design
- Semantic document search
- FAISS vector indexing
- SentenceTransformer embeddings
- Context-aware prompting
- Explainable AI responses
- Source-aware answers
- Interactive business assistant

---

# 📈 Milestone Outcome

After completing this milestone, the platform can:

✅ Search historical forecast reports

✅ Retrieve inventory policies

✅ Query retail business knowledge

✅ Generate grounded AI answers

✅ Cite retrieved document sources

Instead of relying only on model memory, responses are now generated using **retrieved business knowledge**, making the system significantly more reliable and explainable.

---

# 🎯 Next Milestone

**Milestone 8 — Multi-Agent AI System**

The next milestone extends the platform from a single RAG assistant into a collaborative AI system.

Planned agents include:

- Forecast Analyst Agent
- Inventory Advisor Agent
- Business Intelligence Agent
- Report Generation Agent
- Agent Orchestrator

Multiple AI agents will work together to answer complex business questions and automate decision-making workflows.