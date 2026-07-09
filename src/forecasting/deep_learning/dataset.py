import numpy as np
import torch
from torch.utils.data import Dataset


class TimeSeriesDataset(Dataset):
    """
    Converts a univariate time series into
    sliding-window supervised learning samples.

    Example
    -------
    Sequence Length = 5

    Input:
    [1,2,3,4,5] -> Target = 6
    [2,3,4,5,6] -> Target = 7
    """

    def __init__(self, data, sequence_length=30):

        self.sequence_length = sequence_length

        X = []
        y = []

        for i in range(len(data) - sequence_length):

            X.append(data[i:i + sequence_length])

            y.append(data[i + sequence_length])

        self.X = torch.FloatTensor(np.array(X))
        self.y = torch.FloatTensor(np.array(y))

    def __len__(self):

        return len(self.X)

    def __getitem__(self, index):

        return self.X[index], self.y[index]