import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

#device= torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
#print(f"Using {device} device")


data=[[1,2],[3,4]]
x_data=torch.tensor(data)
x_ones=torch.ones_like(x_data)
print(f"Tensor: \n {x_data} \n")
