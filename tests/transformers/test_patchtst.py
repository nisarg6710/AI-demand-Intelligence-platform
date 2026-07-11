import torch

from src.forecasting.deep_learning.transformers.patchtst import PatchTST


def main():

    model = PatchTST()

    x = torch.randn(
        16,
        30,
        1,
    ).to(model.device)

    y = model(x)

    print("Input Shape :", x.shape)
    print("Output Shape:", y.shape)


if __name__ == "__main__":
    main()