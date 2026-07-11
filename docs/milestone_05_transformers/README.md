# 🚀 Milestone 5 — Transformer-based Time Series Forecasting

## Overview

This milestone introduces **modern Transformer architectures** for demand forecasting. Unlike recurrent neural networks (LSTMs and GRUs), Transformer models capture long-range temporal dependencies using attention mechanisms, enabling more efficient learning and improved forecasting performance.

The objective of this milestone is to evaluate whether modern Transformer-based models can outperform both classical statistical approaches and deep learning sequence models on the M5 Forecasting dataset.

---

# Objectives

- Implement modern Transformer architectures for time series forecasting
- Build reusable Transformer components
- Benchmark multiple Transformer models
- Compare against Deep Learning models
- Compare against Classical Forecasting models
- Evaluate forecasting performance using common metrics

---

# Implemented Models

## 1. PatchTST

PatchTST divides the input time series into patches before feeding them into a Transformer encoder.

### Features

- Patch-based representation
- Positional Encoding
- Multi-head Self Attention
- Shared Transformer framework
- GPU compatible

---

## 2. Informer

Informer is designed specifically for long sequence forecasting by reducing the computational cost of self-attention.

### Features

- Custom ProbSparse Attention
- Positional Encoding
- Feed Forward Network
- Early Stopping
- Model Checkpointing
- Efficient attention mechanism

---

## 3. Temporal Fusion Transformer (TFT)

Temporal Fusion Transformer combines attention with gating mechanisms to improve forecasting performance while providing a more structured architecture.

Implemented components include:

- Variable Selection Network (VSN)
- Gated Residual Network (GRN)
- Multi-head Attention
- Prediction Head

---

# Architecture

```text
Input Time Series
        │
        ▼
 Linear Embedding
        │
        ▼
 Positional Encoding
        │
        ▼
 Transformer Block
        │
        ├──────────────┐
        │              │
        ▼              ▼
  Informer      Temporal Fusion Transformer
 ProbSparse      Variable Selection
 Attention       Gated Residual Network
        │              │
        └──────┬───────┘
               ▼
         Prediction Head
               │
               ▼
        Forecasted Demand
```

---

# Reusable Components

The milestone introduces reusable Transformer modules:

- Base Transformer
- Positional Encoding
- ProbSparse Attention
- Variable Selection Network
- Gated Residual Network
- Shared Trainer
- Shared Evaluator
- Early Stopping
- Model Checkpointing

---

# Training Features

Every Transformer model supports:

- GPU Training
- Mini-batch Training
- Validation Split
- Early Stopping
- Best Model Checkpointing
- Automatic Evaluation

---

# Evaluation Metrics

Each model is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

---

# Benchmark Results

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| PatchTST | 5576.15 | 7746.80 | 1027.00 |
| Informer | 3015.61 | 4222.57 | **940.88** |
| **Temporal Fusion Transformer** | **2442.95** | **3731.74** | 941.51 |

---

# Key Observations

## PatchTST

- Strong baseline Transformer
- Demonstrated patch-based sequence learning
- Did not outperform recurrent architectures on this dataset

---

## Informer

- Significant improvement over PatchTST
- ProbSparse Attention reduced attention complexity
- Achieved substantially lower MAE and RMSE

---

## Temporal Fusion Transformer

- Best overall forecasting performance
- Lowest MAE
- Lowest RMSE
- Demonstrated the benefit of combining gating mechanisms with attention

---

# Folder Structure

```text
src/
└── forecasting/
    └── deep_learning/
        └── transformers/
            ├── base_transformer.py
            ├── positional_encoding.py
            ├── prob_sparse_attention.py
            ├── variable_selection.py
            ├── gated_residual_network.py
            ├── patchtst.py
            ├── informer.py
            └── tft.py
```

---

# Skills Demonstrated

This milestone demonstrates experience with:

- PyTorch
- Transformer Architectures
- Attention Mechanisms
- Sequence Modeling
- GPU Training
- Deep Learning
- Model Benchmarking
- Time Series Forecasting
- Modular Software Engineering

---

# Milestone Outcome

By the end of this milestone, the project supports forecasting using:

- Classical Statistical Models
- Deep Learning Sequence Models
- Modern Transformer Architectures

The benchmarking framework now enables direct comparison across all implemented Transformer models, laying the foundation for explainable AI, retrieval-augmented generation, and production deployment in future milestones.

---

## Status

**Milestone 5 — Completed ✅**