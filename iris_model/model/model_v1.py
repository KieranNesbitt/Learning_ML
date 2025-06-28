import torch
import torch.nn as nn

class Iris_classification_v1(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hidden_layer1 = nn.Linear(4,8) # 4 inputs 
        self.hidden_layer2 = nn.Linear(8,8)
        self.activation = nn.ReLU()
        self.output = nn.Linear(8,3) # 3 classifications
    def forward(self,x):
        return self.output(
                    self.activation(
                        self.hidden_layer2(
                            self.activation(
                                self.hidden_layer1(x)
                                ))))
