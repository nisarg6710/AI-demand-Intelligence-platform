# 🧠 Milestone 4 — Deep Learning Forecasting

This milestone extends the AI Demand Intelligence Platform with deep learning-based forecasting models implemented using **PyTorch**. The objective is to compare recurrent neural network architectures against the classical forecasting models developed in Milestone 3.

---

# 🎯 Objectives

The goals of this milestone were to:

- Build a reusable deep learning forecasting framework
- Implement multiple recurrent neural network architectures
- Train models using GPU acceleration when available
- Prevent overfitting with Early Stopping
- Save the best-performing model using Model Checkpointing
- Evaluate models on unseen test data
- Benchmark multiple deep learning models

---

# 🏗 Architecture

```text
Sales Data
      │
      ▼
ForecastDataLoader
      │
      ▼
TimeSeriesDataset
      │
      ▼
DeepLearningModel
      │
 ┌────┼───────────────┐
 │    │               │
 ▼    ▼               ▼
LSTM GRU         Seq2Seq
 │    │               │
 └────┼───────────────┘
      ▼
Trainer
      │
 ┌────┴───────────┐
 │                │
 ▼                ▼
Early Stopping  Model Checkpoint
      │
      ▼
Evaluator
      │
      ▼
Benchmark
```

---

# 📂 Directory Structure

```text
src/
└── forecasting/
    └── deep_learning/
        ├── base_model.py
        ├── data.py
        ├── dataset.py
        ├── evaluate.py
        ├── gru.py
        ├── lstm.py
        ├── seq2seq.py
        └── trainer.py

tests/
└── deep_learning/
    ├── test_data.py
    ├── test_dataset.py
    ├── test_evaluate.py
    ├── test_gru.py
    ├── test_lstm.py
    └── test_seq2seq.py

tests/
└── benchmark_deep_learning.py

artifacts/
├── models/
│   ├── lstm_best.pt
│   ├── gru_best.pt
│   └── seq2seq_best.pt
└── deep_learning_benchmark.csv
```

---

# 🧠 Implemented Models

## LSTM

- Two-layer LSTM network
- Fully connected output layer
- Next-day demand prediction

---

## GRU

- Two-layer GRU network
- Reduced parameter count
- Faster convergence than LSTM

---

## Seq2Seq

- Encoder–Decoder LSTM architecture
- Hidden state transfer
- Sequence-to-sequence forecasting framework

---

# ⚙ Training Pipeline

Each model follows the same workflow:

```text
Load Data
     │
     ▼
Create Sliding Windows
     │
     ▼
Move Model to GPU
     │
     ▼
Training Loop
     │
     ▼
Validation
     │
     ▼
Early Stopping
     │
     ▼
Checkpoint Saving
     │
     ▼
Evaluation
```

---

# 🚀 Framework Features

Implemented features include:

- PyTorch training pipeline
- GPU acceleration (CUDA support)
- Sliding window dataset generation
- Batch training using DataLoader
- Generic trainer
- Validation loop
- Early stopping
- Model checkpointing
- Generic evaluator
- Deep learning benchmark

---

# 📊 Evaluation Metrics

Models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

---

# 🏆 Benchmark Results

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| LSTM | 5387.24 | 7125.91 | 1067.01 |
| GRU | 5550.31 | 7757.56 | 1011.50 |
| Seq2Seq | **5331.46** | **7111.10** | 1064.29 |

---

# 📈 Observations

- Seq2Seq achieved the lowest MAE and RMSE.
- GRU converged quickly while using fewer parameters.
- LSTM provided stable baseline performance.
- MAPE values are inflated because of very small demand values in the dataset; MAE and RMSE are more reliable indicators for this task.

---

# 📦 Generated Artifacts

```
artifacts/
├── models/
│   ├── lstm_best.pt
│   ├── gru_best.pt
│   └── seq2seq_best.pt
└── deep_learning_benchmark.csv
```

---

# 📚 Key Learnings

During this milestone, the project evolved from individual model implementations into a reusable deep learning forecasting framework.

Major engineering concepts covered include:

- PyTorch model development
- GPU-based training
- Sliding window time series forecasting
- Early stopping
- Model checkpointing
- Modular trainer design
- Model evaluation
- Benchmarking multiple architectures

---

# ✅ Milestone Completion

Completed deliverables:

- Reusable deep learning forecasting framework
- LSTM implementation
- GRU implementation
- Seq2Seq implementation
- Generic training pipeline
- Generic evaluation pipeline
- Model checkpointing
- Early stopping
- Benchmark generation

---

# ➡ Next Milestone

**Milestone 5 — Transformer-based Forecasting**

Upcoming models include:

- PatchTST
- Informer
- Temporal Fusion Transformer (TFT)

The objective will be to compare modern transformer architectures against both classical statistical models and recurrent neural networks.