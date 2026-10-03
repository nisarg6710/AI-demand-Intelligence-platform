import os
import sys

# Change the notebook's active working directory to the project root
if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir("..")

# Ensure the root path is also in sys.path
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

import pandas as pd
from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset
from src.forecasting.deep_learning.evaluate import Evaluator

from src.forecasting.deep_learning.transformers.patchtst import PatchTST
from src.forecasting.deep_learning.transformers.informer import Informer
from src.forecasting.deep_learning.transformers.tft import TemporalFusionTransformer

from src.mlops.mlflow_tracking import MLflowTracker


def main():

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
            "PatchTST",
            PatchTST(),
            "artifacts/models/patchtst_best.pt",
        ),
        (
            'Informer',
            Informer(),
            'artifacts/models/informer_best.pt'
        ),
        (
            'TFT',
            TemporalFusionTransformer(),
            'artifacts/models/tft_best.pt'

        )
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
                    "model_name": name,
                    "model_family": "transformer",
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
                    "model_family": "transformer",
                    "model_name": name,
                }
            )

        results.append(
            {
                "Model": name,
                "MAE": evaluation["metrics"]["MAE"],
                "RMSE": evaluation["metrics"]["RMSE"],
                "MAPE": evaluation["metrics"]["MAPE"],
            }
        )

    df = pd.DataFrame(results)

    print("\nTransformer Benchmark")
    print("=" * 60)
    print(df.to_string(index=False))
    
    benchmark_dir = "artifacts/benchmarks"

    os.makedirs(
        benchmark_dir,
        exist_ok=True,
    )

    df.to_csv(
        os.path.join(
            benchmark_dir,
            "transformer_benchmark.csv",
        ),
        index=False,
    )




if __name__ == "__main__":
    main()