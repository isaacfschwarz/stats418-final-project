import streamlit as st
import requests
import json

# Configure page
st.set_page_config(
    page_title="Clinical Trial Predictions",
    page_icon="🔬",
    layout="wide"
)

# App title and description
st.title("🔬 Clinical Trial Adverse Event Prediction")
st.markdown("""
This application predicts adverse events for clinical trials based on study characteristics.
Enter the trial parameters below to get predictions for potential adverse events.
""")

# API endpoint configuration
API_ENDPOINT = "https://model-v2-app-151633565461.europe-west1.run.app/predict"
HEALTH_ENDPOINT = "https://model-v2-app-151633565461.europe-west1.run.app/health"

def call_prediction_api(input_data):
    """
    Call the ML model API with input data
    Returns the three predictions: deaths, serious adverse events, other events
    """
    try:
        response = requests.post(API_ENDPOINT, json=input_data, timeout=30)
        response.raise_for_status()
        predictions = response.json()
        return predictions
    except requests.exceptions.RequestException as e:
        st.error(f"API call failed: {str(e)}")
        return None

# Create input form
st.header("📋 Trial Parameters")

# Collect inputs using the specified widgets
col1, col2 = st.columns(2)

with col1:
    study_type_trials = st.selectbox(
        "Study Type",
        options=["INTERVENTIONAL", "OBSERVATIONAL"],
        help="Type of clinical study design"
    )
    
    allocation_trials = st.selectbox(
        "Allocation Method",
        options=["RANDOMIZED", "NON_RANDOMIZED", "UNKNOWN"],
        help="Method of participant allocation"
    )
    
    intervention_model_trials = st.selectbox(
        "Intervention Model",
        options=["PARALLEL", "SINGLE_GROUP", "SEQUENTIAL", "CROSSOVER", "FACTORIAL", "UNKNOWN"], 
        help="Type of intervention model used"
    )
    
    masking_trials = st.selectbox(
        "Masking/Blinding",
        options=["NONE", "SINGLE", "DOUBLE", "TRIPLE", "QUADRUPLE"], 
        help="Level of masking in the trial"
    )
    
    primary_purpose_trials = st.selectbox(
        "Primary Purpose",
        options=["TREATMENT", "PREVENTION", "HEALTH_SERVICES_RESEARCH", "OTHER", "SUPPORTIVE_CARE", "DIAGNOSTIC", "UNKNOWN", "BASIC_SCIENCE", "SCREENING"],
        help="Main purpose of the clinical trial"
    )

with col2:
    min_age_yr_calc = st.number_input(
        "Minimum Age (years)",
        min_value=0,
        max_value=100,
        value=18,
        step=1,
        help="Minimum age of participants in years"
    )
    
    gender_trials = st.selectbox(
        "Gender",
        options=["ALL", "MALE", "FEMALE"], 
        help="Gender eligibility for the trial"
    )
    
    healthy_volunteers_trials = st.radio(
        "Healthy Volunteers",
        options=[True, False],
        help="Whether healthy volunteers are included"
    )
    
    lead_sponsor_class_trials = st.selectbox(
        "Lead Sponsor Class",
        options=["INDUSTRY", "NIH", "OTHER", "FED", "NETWORK"],
        help="Classification of the lead sponsor"
    )

    intervention_types_trials = st.selectbox(
        "Intervention Types",
        options=["DRUG", "BEHAVIORAL", "DEVICE", "OTHER", "BIOLOGICAL", "RADIATION", "PROCEDURE", "DIAGNOSTIC_TEST", "DIETARY_SUPPLEMENT"],
        help="Types of interventions used (select multiple)"
    )

# Prediction button
if st.button("Generate Predictions", type="primary", use_container_width=True):
    # Prepare input data for API
    input_data = {
        "study_type_trials": study_type_trials,
        "allocation_trials": allocation_trials,
        "intervention_model_trials": intervention_model_trials,
        "masking_trials": masking_trials,
        "primary_purpose_trials": primary_purpose_trials,
        "min_age_yr_calc": min_age_yr_calc,
        "gender_trials": gender_trials,
        "healthy_volunteers_trials": healthy_volunteers_trials,
        "lead_sponsor_class_trials": lead_sponsor_class_trials,
        "intervention_types_trials": intervention_types_trials
    }
    
    # Call API and get predictions
    with st.spinner("Generating predictions..."):
        predictions = call_prediction_api(input_data)
    
    if predictions:
        # Display predictions at the top
        st.header("📊 Prediction Results")
        
        # Create three columns for the predictions
        pred_col1, pred_col2, pred_col3 = st.columns(3)
        
        with pred_col1:
            st.metric(
                label="⚰️ Deaths Rate",
                value=f"{predictions.get('rate_deaths_calc', 0):.3f}",
                help="Predicted rate of deaths in the trial"
            )
        
        with pred_col2:
            st.metric(
                label="⚠️ Serious Adverse Events Rate",
                value=f"{predictions.get('rate_serious_aes_calc', 0):.3f}",
                help="Predicted rate of serious adverse events"
            )
        
        with pred_col3:
            st.metric(
                label="📋 Other Adverse Events Rate",
                value=f"{predictions.get('rate_other_aes_calc', 0):.3f}",
                help="Predicted rate of other adverse events"
            )

# Sidebar with additional information
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This app uses an XGBoost machine learning model to predict the likelihood of adverse events occurring in clinical trials based on trial characteristics.
    The model was built off of publically available data from [ClinicalTrails.gov](https://clinicaltrials.gov/)
    
    **Predictions include:**
    - Rate of Deaths
    - Rate of Serious Adverse Events  
    - Rate of Other Adverse Events
    """)
    
    st.header("📝 Instructions")
    st.write("""
    1. Fill in all trial parameters
    2. Click 'Generate Predictions'
    3. Review the predicted outcomes
    """)
    
    # st.header("⚙️ API Status")
    # # Add API health check - FIXED: Use Cloud Run URL
    # try:
    #     health_response = requests.get(HEALTH_ENDPOINT, timeout=5)
    #     if health_response.status_code == 200:
    #         st.success("✅ API is healthy")
    #     else:
    #         st.warning("⚠️ API health check failed")
    # except:
    #     st.error("❌ Cannot reach API")

# Footer
st.markdown("---")
st.markdown("*Predictions are estimates based on historical data and should be used for planning purposes only.*")