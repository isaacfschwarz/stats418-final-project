# App

This directory contains the user interface component of the application built using Streamlit, along with Docker containerization files for deployment.

## Files

### Core Application Files

#### `streamlit_app_v2.py`
The main Python file containing the Streamlit application UI. This file includes:
- User interface components and layout
- Interactive elements for user input
- Data visualization and display logic
- Integration with the backend model API

### Docker Configuration Files

#### `Dockerfile`
Docker configuration file that defines the container environment, dependencies, and runtime settings for the Streamlit application.

#### `compose.yaml`
Docker Compose configuration file that orchestrates the container deployment, including service definitions, port mappings, and environment variables for the Streamlit app.

#### `requirements.txt`
Python dependencies file listing all required packages and their versions needed to run the Streamlit application.

## Usage

### Running with Docker Compose

To deploy the Streamlit UI using Docker:

1. Download all files from this directory
2. Navigate to the directory containing the files
3. Run the following command:

```bash
docker compose up
```

This will build and start the Docker container with the Streamlit application, making the user interface accessible through your web browser.

### Application Access

Once the container is running, the Streamlit application will be available at the configured port (typically http://localhost:8501). The web interface provides a way to interact with the model and visualize results.

## Framework

The application is built using [Streamlit](https://streamlit.io/), a Python framework for creating interactive web applications for data science and machine learning projects.
