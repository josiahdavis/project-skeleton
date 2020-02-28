import numpy as np


class RandomDataset:
    def __init__(self, h=10, w=4):

        self.h = h
        self.w = w

    def get_data(self):
        return np.random.normal(size(self.h, self.w))
