import torch

from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset

from src.forecasting.deep_learning.lstm import LSTMModel
from src.forecasting.deep_learning.trainer import Trainer


def main():

    train,validation, _, _ = ForecastDataLoader().prepare()

    dataset = TimeSeriesDataset(
        train,
        sequence_length=30
    )

    train_dataset = TimeSeriesDataset(
        train,
        sequence_length=30
    )

    validation_dataset = TimeSeriesDataset(
        validation,
        sequence_length=30
    )

    loader = DataLoader(
        dataset,
        batch_size=64,
        shuffle=True
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=64,
        shuffle=True
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=64,
        shuffle=False
    )

    model = LSTMModel()
    
    print("Model Device:", model.device)
    print("First Parameter Device:", next(model.parameters()).device)

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )

    criterion = torch.nn.MSELoss()

    best_model = Trainer.train(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        optimizer=optimizer,
        criterion=criterion,
        epochs=20,
        patience=5
    )

    print('\nBest model saved at:')
    print(best_model)


if __name__ == "__main__":
    main()