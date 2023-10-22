from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Depends
from .utils import create_neural_network, visualize_neural_network

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/visualize/")
async def visualize_network(request_data: NeuralNetworkCreateRequest):
    # Create the neural network model
    model = create_neural_network(request_data.input_dim, request_data.output_dim, request_data.layers, request_data.neurons)
    
    # Visualize the neural network and get the visualization data
    visualization_data = visualize_neural_network(model)
    
    return visualization_data
