import os
import sys

# Change the notebook's active working directory to the project root
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir("..")

# Ensure the root path is also in sys.path
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from torch.utils.data import DataLoader
import pandas as pd

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset
from src.forecasting.deep_learning.evaluate import Evaluator

from src.forecasting.deep_learning.lstm import LSTMModel
from src.forecasting.deep_learning.gru import GRUModel
from src.forecasting.deep_learning.seq2seq import Seq2SeqModel

from src.mlops.mlflow_tracking import MLflowTracker


def benchmark():

    _, _, test, scaler = ForecastDataLoader().prepare()

    dataset = TimeSeriesDataset(
        test,
        sequence_length=30,
    )

    loader = DataLoader(
        dataset,
        batch_size=64,
        shuffle=False,
    )

    models = [
        (
            "LSTM",
            LSTMModel(),
            "artifacts/models/lstm_best.pt",
        ),
        (
            "GRU",
            GRUModel(),
            "artifacts/models/gru_best.pt",
        ),
        (
            "Seq2Seq",
            Seq2SeqModel(),
            "artifacts/models/seq2seq_best.pt",
        ),
    ]

    results = []

    tracker = MLflowTracker(
        experiment_name="AI-Demand-Intelligence-Forecasting"
    )



    for name, model, checkpoint in models:

        evaluator = Evaluator(model)

        evaluation = evaluator.evaluate(
            checkpoint,
            loader,
            scaler,
        )

        metrics = evaluation["metrics"]

        with tracker.start_run(
            run_name=name
        ):

            tracker.log_params(
                {
                    "model_family": "deep_learning",
                    "model_name": name,
                    "checkpoint": checkpoint,
                    "sequence_length": 30,
                    "batch_size": 64,
                }
            )

            tracker.log_metrics(
                {
                    "MAE": metrics["MAE"],
                    "RMSE": metrics["RMSE"],
                    "MAPE": metrics["MAPE"],
                }
            )

            tracker.log_tags(
                {
                    "project": "AI Demand Intelligence Platform",
                    "stage": "milestone_12",
                    "model_family": "deep_learning",
                }
            )


        results.append(
            {
                "Model": name,
                "MAE": metrics["MAE"],
                "RMSE": metrics["RMSE"],
                "MAPE": metrics["MAPE"]
            }
        )

    df = pd.DataFrame(results)

    print("\nDeep Learning Benchmark")
    print("=" * 60)
    print(df.to_string(index=False))

    df.to_csv(
        "artifacts/deep_learning_benchmark.csv",
        index=False,
    )

    benchmark_path = "artifacts/deep_learning_benchmark.csv"

    with tracker.start_run(run_name="Deep-Learning-Benchmark"):

        tracker.log_params({
            "model_family": "deep_learning",
            "sequence_length": 30,
            "batch_size": 64,
            "models_evaluated": len(models),
        })

        tracker.log_metrics({
            "best_mae": float(df["MAE"].min()),
            "best_rmse": float(df["RMSE"].min()),
            "best_mape": float(df["MAPE"].min()),
        })

        tracker.log_tags({
            "project": "AI Demand Intelligence Platform",
            "stage": "milestone_12",
            "artifact_type": "benchmark",
        })

        tracker.log_artifact(
            benchmark_path,
            artifact_path="benchmarks",
        )


if __name__ == "__main__":
    benchmark()