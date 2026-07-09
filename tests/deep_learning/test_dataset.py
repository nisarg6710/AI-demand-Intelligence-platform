from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset


def main():

    print("=" * 60)
    print("Testing TimeSeriesDataset")
    print("=" * 60)

    train, val, test, scaler = ForecastDataLoader().prepare()

    dataset = TimeSeriesDataset(
        train,
        sequence_length=30
    )

    print("\nDataset Information")
    print("-" * 30)

    print("Total Samples:", len(dataset))

    X, y = dataset[0]

    print("\nSingle Sample")

    print("Input Shape :", X.shape)
    print("Target Shape:", y.shape)

    print("\nFirst Input Sequence")

    print(X)

    print("\nTarget")

    print(y)

    loader = DataLoader(
        dataset,
        batch_size=64,
        shuffle=True
    )

    X_batch, y_batch = next(iter(loader))

    print("\nMini Batch")

    print("X Batch Shape:", X_batch.shape)
    print("y Batch Shape:", y_batch.shape)


if __name__ == "__main__":
    main()