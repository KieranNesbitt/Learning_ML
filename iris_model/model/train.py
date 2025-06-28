import torch
from torch import nn
from torch import optim
from model_v1 import Iris_classification_v1 as MultiClass
from ready_data import get_data
device = "cuda" if torch.cuda.is_available() else "cpu"
model = MultiClass().to(device)

Iris_db = get_data()
N_epoch = 1000
data = Iris_db.iloc[:, 0:4]
labels = Iris_db.iloc[:, 5:]
loss_fn = nn.MultiMarginLoss()
optm = optim.Adam(model.parameters(), lr=0.1)
data = torch.tensor(data, dtype=torch.float32)
labels = torch.tensor(labels, dtype=torch.float32)


for epoch in range(N_epoch):
    pass