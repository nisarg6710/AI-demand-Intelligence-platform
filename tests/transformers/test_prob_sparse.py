import torch

from src.forecasting.deep_learning.transformers.prob_sparse_attention import (
    ProbSparseAttention
    )


def main():

    attention = ProbSparseAttention()

    x = torch.randn(
        8,
        30,
        64,
    )

    output = attention(x)

    print("Input :", x.shape)
    print("Output:", output.shape)


if __name__ == "__main__":
    main()