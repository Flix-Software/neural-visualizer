# Neural Network Visualizer

The Neural Network Visualizer is a FastAPI project that allows you to create and visualize neural networks. Users can input the number of layers, input layer size, output layer size, and the number of neurons in each layer. The application will create the neural network and display a visual representation of the network in the UI.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/neural-visualizer.git
   cd neural-visualizer

```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

pip install -r requirements.txt
```

### Usage

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Directory Structure

```
app/: Contains the FastAPI application and related files.
templates/: HTML templates for the user interface.
requirements.txt: Lists the project dependencies.
README.md: Project documentation.
```
