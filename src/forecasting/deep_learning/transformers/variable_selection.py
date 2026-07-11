import torch
import torch.nn as nn


class VariableSelectionNetwork(nn.Module):

    def __init__(
        self,
        input_size,
        hidden_size,
    ):
        super().__init__()

        self.weight_network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, input_size),
            nn.Softmax(dim=-1),
        )

    def forward(self, x):

        weights = self.weight_network(x)

        return x * weights