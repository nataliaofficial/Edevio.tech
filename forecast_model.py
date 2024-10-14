import torch
import torch.nn as nn

# Define a simple PyTorch model for solar energy forecasting
class SolarForecastModel(nn.Module):
    def __init__(self):
        super(SolarForecastModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)  # Input layer
        self.fc2 = nn.Linear(50, 1)   # Output layer
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Apply ReLU activation
        x = self.fc2(x)  # Linear output
        return x
