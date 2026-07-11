import torch
import torch.nn as nn


class BaseTransformer(nn.Module):

    def __init__(self):

        super().__init__()

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.to(self.device)