import torch

from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset

from src.forecasting.deep_learning.transformers.patchtst import PatchTST
from src.forecasting.deep_learning.trainer import Trainer


def main():

    train, validation, _, _ = ForecastDataLoader().prepare()

    train_dataset = TimeSeriesDataset(
        train,
        sequence_length=30,
    )

    validation_dataset = TimeSeriesDataset(
        validation,
        sequence_length=30,
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=64,
        shuffle=True,
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=64,
        shuffle=False,
    )

    model = PatchTST()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001,
    )

    criterion = torch.nn.MSELoss()

    checkpoint = Trainer.train(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        optimizer=optimizer,
        criterion=criterion,
        epochs=20,
        patience=5,
        checkpoint_name="patchtst_best.pt",
    )

    print("\nBest model:")
    print(checkpoint)


if __name__ == "__main__":
    main()