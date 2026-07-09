import torch
import torch.nn as nn

from src.forecasting.deep_learning.base_model import DeepLearningModel


class Seq2SeqModel(DeepLearningModel):

    def __init__(
        self,
        input_size=1,
        hidden_size=64,
        num_layers=2,
    ):

        super().__init__()

        self.encoder = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )

        self.decoder = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )

        self.fc = nn.Linear(
            hidden_size,
            1,
        )

        self.to(self.device)

    def forward(self, x):

        _, (hidden, cell) = self.encoder(x)

        decoder_input = x[:, -1:, :]

        output, _ = self.decoder(
            decoder_input,
            (hidden, cell),
        )

        prediction = self.fc(
            output[:, -1, :]
        )

        return prediction