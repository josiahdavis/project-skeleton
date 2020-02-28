import numpy as np
import torch


class RandomDataset:
    def __init__(self, h=10, w=4):

        self.h = h
        self.w = w

    def get_data(self):
        x = np.random.normal(size=(self.h, self.w))
        return torch.tensor(x, dtype=torch.float)


def make_random_data(h=10, w=4):
    rd = RandomDataset(h, w)
    return rd.get_data()
