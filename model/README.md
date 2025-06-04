# Model

This directory contains the Flask API application and Docker containerization files for model deployment.

## Files

### Core Application Files

#### `model.py`
The main Python script that contains:
- The machine learning model implementation
- Flask API endpoints for model predictions
- Request handling and response formatting logic

#### `multi_target_model.joblib`
The serialized XGBoost model file containing the trained model ready for inference. This file is loaded by the Flask application to make predictions.

### Docker Configuration Files

#### `Dockerfile`
Docker configuration file that defines the container environment, dependencies, and runtime settings for the Flask application.

#### `compose.yaml`
Docker Compose configuration file that orchestrates the container deployment, including service definitions, port mappings, and environment variables.

#### `requirements.txt`
Python dependencies file listing all required packages and their versions needed to run the Flask application.

## Usage

### Running with Docker Compose

To deploy the model API using Docker:

1. Download all files from this directory
2. Navigate to the directory containing the files
3. Run the following command:

```bash
docker compose up
```

This will build and start the Docker container with the Flask API, making the model available for predictions through HTTP requests.

### API Access

Once the container is running, the Flask API will be accessible at the configured port. Refer to the `model.py` file for specific endpoint documentation and request/response formats.
