import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_dim, output_dim, layers, neurons):
        super(NeuralNetwork, self).__init()

        layer_sizes = [input_dim] + neurons + [output_dim]
        self.layers = nn.ModuleList()

        for i in range(len(layer_sizes) - 1):
            self.layers.append(nn.Linear(layer_sizes[i], layer_sizes[i+1]))

    def forward(self, x):
        for layer in self.layers[:-1]:
            x = torch.relu(layer(x))
        x = self.layers[-1](x)
        return x
