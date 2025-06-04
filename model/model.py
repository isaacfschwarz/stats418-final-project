# Import modules 
from flask import Flask, request, jsonify
import joblib
import os
import pandas as pd
from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor

# Create Flask app first
app = Flask(__name__)

# Load model with error handling
try:
    model = joblib.load('multi_target_model.joblib')
    print("Model loaded successfully")
except FileNotFoundError:
    print("ERROR: multi_target_model.joblib not found!")
    model = None
except Exception as e:
    print(f"ERROR loading model: {e}")
    model = None

# Define expected features 
EXPECTED_FEATURES = ['study_type_trials',
                     'allocation_trials',
                     'intervention_model_trials',
                     'masking_trials',
                     'primary_purpose_trials',
                     'min_age_yr_calc',
                     'gender_trials',
                     'healthy_volunteers_trials',
                     'lead_sponsor_class_trials',
                     'intervention_types_trials']

# Define categorical and numerical features (same as during training)
FEATURES_CAT = ['study_type_trials',
                'allocation_trials',
                'intervention_model_trials',
                'masking_trials',
                'primary_purpose_trials',
                'gender_trials',
                'healthy_volunteers_trials',
                'lead_sponsor_class_trials',
                'intervention_types_trials']

FEATURES_NUM = ['min_age_yr_calc']

def preprocess_input_data(input_data):
    """
    Convert input data to the same format as training data:
    - Categorical columns to category dtype
    - Numerical columns to float32
    """
    # Create DataFrame
    input_df = pd.DataFrame([input_data], columns=EXPECTED_FEATURES)
    
    # Convert categorical columns to category dtype (same as training)
    for col in FEATURES_CAT:
        input_df[col] = input_df[col].astype('category')
    
    # Convert numerical columns to float32 (same as training)
    for col in FEATURES_NUM:
        input_df[col] = input_df[col].astype('float32')
    
    return input_df

@app.route('/', methods=['GET'])
def server_is_up():
    return 'server is up - nice job! \n \n'

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Cloud Run"""
    if model is None:
        return jsonify({'status': 'unhealthy', 'error': 'Model not loaded'}), 500
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        # Parse JSON input
        input_data = request.get_json()

        # Ensure all required features are present
        missing = [feature for feature in EXPECTED_FEATURES if feature not in input_data]
        if missing:
            return jsonify({'error': f'Missing features: {missing}'}), 400

        # Preprocess the input data (convert to same dtypes as training)
        input_df = preprocess_input_data(input_data)
        
        # Debug: Print the processed data types
        print("Processed input data types:")
        print(input_df.dtypes)
        print("Input values:")
        print(input_df.iloc[0])

        # Make prediction - XGBoost handles categorical data automatically since model was trained with enable_categorical=True
        predictions = model.predict(input_df)[0]

        # Create response with the three outputs
        response = {
            'rate_deaths_calc': round(float(predictions[0]), 3),
            'rate_serious_aes_calc': round(float(predictions[1]), 3),
            'rate_other_aes_calc': round(float(predictions[2]), 3)
        }

        return jsonify(response)

    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/debug', methods=['POST'])
def debug_input():
    """
    Endpoint to debug input data processing without making predictions
    """
    try:
        input_data = request.get_json()
        input_df = preprocess_input_data(input_data)
        
        debug_info = {
            'dtypes': input_df.dtypes.to_dict(),
            'values': input_df.iloc[0].to_dict(),
            'shape': input_df.shape
        }
        
        return jsonify(debug_info)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)