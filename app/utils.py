import torch
import torch.nn as nn
from torchviz import make_dot
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class NeuralNetwork(nn.Module):
    def __init__(self, input_dim, output_dim, layers, neurons):
        super(NeuralNetwork, self).__init__()

        layer_sizes = [input_dim] + neurons + [output_dim]
        self.layers = nn.ModuleList()

        for i in range(len(layer_sizes) - 1):
            self.layers.append(nn.Linear(layer_sizes[i], layer_sizes[i+1]))

    def forward(self, x):
        for layer in self.layers[:-1]:
            x = torch.relu(layer(x))
        x = self.layers[-1](x)
        return x

def create_neural_network(input_dim, output_dim, layers, neurons):
    model = NeuralNetwork(input_dim, output_dim, layers, neurons)
    return model

def visualize_neural_network(model):
    x = torch.randn(1, model.layers[0].in_features)
    y = model(x)
    dot = make_dot(y, params=dict(list(model.named_parameters())))
    
    # Save the visualization as an image and return its base64 representation
    buf = BytesIO()
    dot.format = 'png'
    dot.render(filename=buf)
    buf.seek(0)
    img_data = base64.b64encode(buf.read()).decode()
    img_src = f"data:image/png;base64, {img_data}"
    
    return {"image_src": img_src}
