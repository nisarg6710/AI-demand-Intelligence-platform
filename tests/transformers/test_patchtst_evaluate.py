from torch.utils.data import DataLoader

from src.forecasting.deep_learning.data import ForecastDataLoader
from src.forecasting.deep_learning.dataset import TimeSeriesDataset

from src.forecasting.deep_learning.transformers.patchtst import PatchTST
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

    model = PatchTST()

    evaluator = Evaluator(model)

    results = evaluator.evaluate(
        checkpoint_path="artifacts/models/patchtst_best.pt",
        dataloader=loader,
        scaler=scaler,
    )

    print("\nPatchTST Evaluation")
    print("-" * 30)

    for metric, value in results["metrics"].items():
        print(f"{metric}: {value:.2f}")


if __name__ == "__main__":
    main()