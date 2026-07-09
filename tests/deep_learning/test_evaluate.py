from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset

from src.forecasting.deep_learning.lstm import LSTMModel
from src.forecasting.deep_learning.evaluate import Evaluator


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

    model = LSTMModel()

    evaluator = Evaluator(model)

    results = evaluator.evaluate(
        checkpoint_path="artifacts/models/lstm_best.pt",
        dataloader=loader,
        scaler=scaler,
    )

    print("\nLSTM Evaluation")
    print("-" * 30)

    for metric, value in results.items():

        print(
            f"{metric}: {value:.2f}"
        )


if __name__ == "__main__":
    main()