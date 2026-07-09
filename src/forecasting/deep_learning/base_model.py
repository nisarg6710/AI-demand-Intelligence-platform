from abc import ABC, abstractmethod

import torch
import torch.nn as nn

class DeepLearningModel(nn.Module, ABC):
    def __init__(self):
        super().__init__()

        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu'
        )

    
    @abstractmethod
    def forward(self, x):
        pass