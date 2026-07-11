import torch

from src.forecasting.deep_learning.transformers.positional_encoding import (
    PositionalEncoding,
)


def main():

    x = torch.randn(
        8,
        30,
        64,
    )

    pe = PositionalEncoding(
        d_model=64
    )

    output = pe(x)

    print("Input Shape :", x.shape)
    print("Output Shape:", output.shape)


if __name__ == "__main__":
    main()