import torch
import torch.nn as nn

from src.forecasting.deep_learning.transformers.base_transformer import BaseTransformer
from src.forecasting.deep_learning.transformers.positional_encoding import PositionalEncoding
from src.forecasting.deep_learning.transformers.variable_selection import VariableSelectionNetwork
from src.forecasting.deep_learning.transformers.gated_residual_network import GatedResidualNetwork


class TemporalFusionTransformer(BaseTransformer):

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
            d_model,
        )

        self.variable_selection = VariableSelectionNetwork(
            d_model,
            hidden_size,
        )

        self.grn = GatedResidualNetwork(
            d_model,
            hidden_size,
        )

        self.attention = nn.MultiheadAttention(
            embed_dim=d_model,
            num_heads=n_heads,
            batch_first=True,
        )

        self.output_layer = nn.Linear(
            d_model,
            1,
        )

        self.to(self.device)

    def forward(self, x):

        x = self.embedding(x)

        x = self.position(x)

        x = self.variable_selection(x)

        x = self.grn(x)

        x, _ = self.attention(
            x,
            x,
            x,
        )

        x = x[:, -1]

        return self.output_layer(x)