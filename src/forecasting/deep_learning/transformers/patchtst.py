import torch
import torch.nn as nn

from src.forecasting.deep_learning.transformers.base_transformer import BaseTransformer
from src.forecasting.deep_learning.transformers.positional_encoding import PositionalEncoding


class PatchTST(BaseTransformer):

    def __init__(
        self,
        input_size=1,
        patch_length=5,
        d_model=64,
        nhead=4,
        num_layers=2,
    ):

        super().__init__()

        self.patch_length = patch_length

        self.patch_embedding = nn.Linear(
            patch_length * input_size,
            d_model,
        )

        self.position = PositionalEncoding(
            d_model=d_model
        )

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            batch_first=True,
        )

        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers,
        )

        self.fc = nn.Linear(
            d_model,
            1,
        )

        self.to(self.device)
    def forward(self, x):

        batch_size = x.size(0)

        sequence_length = x.size(1)

        num_patches = sequence_length // self.patch_length

        x = x[:, : num_patches * self.patch_length, :]

        x = x.reshape(
            batch_size,
            num_patches,
            self.patch_length,
        )

        x = self.patch_embedding(x)

        x = self.position(x)

        x = self.transformer(x)

        x = x[:, -1]

        prediction = self.fc(x)

        return prediction