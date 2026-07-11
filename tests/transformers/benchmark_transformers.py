
import os
import pandas as pd
from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset
from src.forecasting.deep_learning.evaluate import Evaluator

from src.forecasting.deep_learning.transformers.patchtst import PatchTST
from src.forecasting.deep_learning.transformers.informer import Informer
from src.forecasting.deep_learning.transformers.tft import TemporalFusionTransformer



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

    for name, model, checkpoint in models:

        evaluator = Evaluator(model)

        evaluation = evaluator.evaluate(
            checkpoint,
            loader,
            scaler,
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