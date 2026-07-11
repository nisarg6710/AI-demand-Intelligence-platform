import torch
import torch.nn as nn

from src.forecasting.deep_learning.transformers.base_transformer import BaseTransformer
from src.forecasting.deep_learning.transformers.positional_encoding import PositionalEncoding
from src.forecasting.deep_learning.transformers.prob_sparse_attention import ProbSparseAttention


class Informer(BaseTransformer):

    def __init__(
        self,
        input_size=1,
        d_model=64,
        hidden_size=128,
        n_heads=4,
    ):

        super().__init__()

        self.embedding = nn.Linear(
            input_size,
            d_model,
        )

        self.position = PositionalEncoding(
            d_model=d_model,
        )

        self.attetion = ProbSparseAttention(
            d_model=d_model,
            n_heads=n_heads
        )

        self.feed_forward= nn.Sequential(
            nn.Linear(d_model, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, d_model)
        )

        self.output_layer = nn.Linear(
            d_model,
            1,
        )

        self.to(self.device)

    def forward(self, x):

        x = self.embedding(x)

        x = self.position(x)

        x = self.attetion(x)

        x = self.feed_forward(x)

        x = x[:, -1]

        prediction = self.output_layer(x)

        return prediction