from pydantic import BaseModel
from typing import List

class NeuralNetworkCreateRequest(BaseModel):
    input_dim: int
    output_dim: int
    layers: int
    neurons: List[int]

class NeuralNetworkResponse(BaseModel):
    layers: List[int]
    weights: List[List[List[float]]]
