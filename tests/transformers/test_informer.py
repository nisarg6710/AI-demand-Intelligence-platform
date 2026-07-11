import torch

from src.forecasting.deep_learning.transformers.informer import Informer


def main():

    model = Informer()

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