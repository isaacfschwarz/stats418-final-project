# Clinical Trials Machine Learning Project

This repository contains a complete machine learning project that analyzes clinical trial data to predict adverse events using data from the ClinicalTrials.gov API. The project includes data processing, model development, API deployment, and a user-friendly web interface.

## Project Overview

The project focuses on building a predictive model for clinical trial adverse events by combining clinical trial summary information with adverse event data. The final solution includes both a Flask API for model serving and a Streamlit web application for user interaction.

## Repository Structure

### 📁 [`data/`](./data/)
Contains the raw datasets used for model training:
- `adverse_events_10k.csv` - Raw adverse events data for 10,000 clinical trials
- `clinical_trial_summary_10k.csv` - Raw clinical trial summary data for 10,000 trials
- Data obtained from ClinicalTrials.gov API and joined using NCT_ID

### 📁 [`presentations/`](./presentations/)
Project presentation materials:
- `proposal-presentation.pdf` - Initial project proposal slide deck
- `final-presentation.pdf` - Final project presentation with results and demo

### 📁 [`model/`](./model/)
Flask API and model deployment files:
- `model.py` - Main Flask application with model endpoints
- `multi_target_model.joblib` - Serialized XGBoost model
- Docker configuration files for containerized deployment

### 📁 [`app/`](./app/)
Streamlit web application for user interface:
- `streamlit_app_v2.py` - Main Streamlit application file
- Docker configuration files for containerized deployment

### 📄 `writeup.md`
Comprehensive project report containing detailed analysis, methodology, results, and conclusions.

## Quick Start

### Prerequisites
- Docker and Docker Compose installed on your system

### Running the Application

1. **Start the Model API:**
   ```bash
   cd model/
   docker compose up
   ```

2. **Start the Streamlit UI (in a new terminal):**
   ```bash
   cd app/
   docker compose up
   ```

3. **Access the Application:**
   - Open your web browser and navigate to the Streamlit application (typically http://localhost:8501)
   - The web interface will communicate with the model API to provide predictions

## Technology Stack

- **Machine Learning:** XGBoost for multi-target prediction
- **Backend API:** Flask for model serving
- **Frontend UI:** Streamlit for interactive web interface
- **Data Source:** ClinicalTrials.gov API
- **Deployment:** Docker and Docker Compose
- **Data Processing:** Python with pandas and scikit-learn

## Project Workflow

1. **Data Collection:** Retrieved clinical trial and adverse event data from ClinicalTrials.gov API
2. **Data Processing:** Cleaned and joined datasets using NCT_ID as the primary key
3. **Model Development:** Built and trained XGBoost model for adverse event prediction
4. **API Development:** Created Flask API for model serving
5. **UI Development:** Built Streamlit web application for user interaction
6. **Deployment:** Containerized both components using Docker

## Documentation

Each directory contains its own README file with detailed information about the contents and usage instructions.
