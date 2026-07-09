from torch.utils.data import DataLoader
import pandas as pd

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset
from src.forecasting.deep_learning.evaluate import Evaluator

from src.forecasting.deep_learning.lstm import LSTMModel
from src.forecasting.deep_learning.gru import GRUModel
from src.forecasting.deep_learning.seq2seq import Seq2SeqModel


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
                "MAE": evaluation['metrics']['MAE'],
                'RMSE': evaluation['metrics']['RMSE'],
                'MAPE': evaluation['metrics']['MAPE']
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


if __name__ == "__main__":
    benchmark()