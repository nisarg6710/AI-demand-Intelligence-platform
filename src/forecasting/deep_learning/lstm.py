import torch
import torch.nn as nn

from src.forecasting.deep_learning.base_model import DeepLearningModel

class LSTMModel(DeepLearningModel):

    def __init__(
            self,
            input_size = 1,
            hidden_size=64,
            num_layers =2
    ):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_size,
            1
        )

        # print("Moving model to:", self.device)
        self.to(self.device)
        # print("After move:", next(self.parameters()).device)
    
    def forward(self, x):
        output, _ = self.lstm(x)
        output = output[:, -1, :]

        output = self.fc(output)

        return output