import torch
import torch.nn as nn


class GatedResidualNetwork(nn.Module):

    def __init__(
        self,
        input_size,
        hidden_size,
    ):
        super().__init__()

        self.fc1 = nn.Linear(
            input_size,
            hidden_size,
        )

        self.fc2 = nn.Linear(
            hidden_size,
            input_size,
        )

        self.relu = nn.ReLU()

        self.gate = nn.Sequential(
            nn.Linear(input_size, input_size),
            nn.Sigmoid(),
        )

        self.norm = nn.LayerNorm(
            input_size,
        )

    def forward(self, x):

        residual = x

        x = self.fc1(x)

        x = self.relu(x)

        x = self.fc2(x)

        gate = self.gate(x)

        x = gate * x + (1 - gate) * residual

        return self.norm(x)