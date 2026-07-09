import torch.nn as nn

from src.forecasting.deep_learning.base_model import DeepLearningModel


class GRUModel(DeepLearningModel):

    def __init__(
        self,
        input_size=1,
        hidden_size=64,
        num_layers=2,
    ):

        super().__init__()

        self.gru = nn.GRU(
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

        output, _ = self.gru(x)

        output = output[:, -1, :]

        output = self.fc(output)

        return output