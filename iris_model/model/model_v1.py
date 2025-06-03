import torch
import torch.nn as nn

class Iris_classification_v1(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hidden_layer = nn.Linear(4,8) # 4 inputs 
        self.activation = nn.ReLU()
        self.output = nn.Linear(8,3) # 3 classifications
    def forward(self,x):
        x = self.act(self.hidden_layer(x))
        result = self.output(x)
        return x