import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self, in_features, out_features, dropout):
        super(Net, self).__init__()
        self.fc = nn.Linear(in_features, out_features)
        self.do = nn.Dropout(p=dropout)

    def forward(self, x):
        return self.do(self.fc(x))
