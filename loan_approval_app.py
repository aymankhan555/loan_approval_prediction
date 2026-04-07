from datetime import date
import streamlit as st
import pandas as pd
import numpy as np
import joblib 

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("💰 Loan Approval Predictor")
st.caption("Predicting the likelihood of loan approval using machine learning.")
st.divider()

# categorical options

# person_has_owenership = ["RENT", "MORTGAGE", "OWN", "OTHER"]
# loan_intent = ["EDUCATION", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "MEDICAL","VENTURE"]
# loan_grade = ["A", "B", "C", "D", "E", "F", "G"]
# cb_person_default_on_file = ["Y", "N"]

st.sidebar.header("Input Applicant Details")

# Demographic Information and Financial Details
# categorical

person_home_ownership = st.sidebar.selectbox(
    "Ownership Status",
    ["RENT", "OWN", "MORTGAGE", "OTHER"]
)

loan_intent = st.sidebar.selectbox(
    "Loan Intent",
    ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
)

loan_grade = st.sidebar.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)

cb_person_default_on_file = st.sidebar.selectbox(
    "Default on File",
    ["Y", "N"]
)

#Numerical
person_age = st.sidebar.number_input(
    "Age", min_value=18,max_value=80,value=30
)

person_income = st.sidebar.number_input(
    "Annual Income",min_value=0,max_value=1000000,value=50000,step=1000
)

person_emp_length = st.sidebar.slider(
    "Employment Length (years)", 0, 60, 1
)

loan_amnt = st.sidebar.number_input(
    "Loan Amount",min_value=500,max_value=50000,value=10000,step=500
)

loan_int_rate = st.sidebar.slider(
    "Loan Interest Rate (%)",5, 25, 10)

loan_percent_income = st.sidebar.slider(
    "Loan-to-Income Ratio",0.0, 1.0, 0.3, step=0.01
)

cb_person_cred_hist_length = st.sidebar.slider(
    "Credit History Length (years)",0, 40, 5
)

def new_features(data_df):      
    data_df['income_to_loan'] = data_df['person_income'] / (data_df['loan_amnt'] + 1)
    data_df['age_to_emp_length'] = data_df['person_age'] / (data_df['person_emp_length'] + 1)
    data_df['log_income'] = np.log1p(data_df['person_income'])
    data_df['age_to_credit_history'] = data_df['person_age'] / (data_df['cb_person_cred_hist_length'] )
    data_df['stability_score'] = (data_df['person_emp_length'] * data_df['person_income']) / (data_df['loan_amnt'] * (data_df['cb_person_cred_hist_length'] + 1))
    data_df['rate_to_age'] = data_df['loan_int_rate'] / data_df['person_age']
    return data_df

def model_load():
    try:
        model = joblib.load("models/best_model.pkl")
        model_columns = joblib.load("models/feature_columns.pkl")
        st.sidebar.success("Model and feature columns loaded successfully!")
        return model, model_columns
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

input_df = pd.DataFrame({
    'person_age': [person_age],
    'person_income': [person_income],
    'person_emp_length': [person_emp_length],
    'loan_amnt': [loan_amnt],
    'loan_int_rate': [loan_int_rate],
    'loan_percent_income': [loan_percent_income],
    'cb_person_cred_hist_length': [cb_person_cred_hist_length],
    'person_home_ownership': [person_home_ownership],
    'loan_intent': [loan_intent],
    'loan_grade': [loan_grade],
    'cb_person_default_on_file': [cb_person_default_on_file]
})

input  = new_features(input_df)
model,model_columns = model_load()


input_encoded = pd.get_dummies(input)
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

if st.sidebar.button("Predict Loan Approval", type='primary'):
    if model is not None:
        prediction = model.predict(input_encoded) 
        probability_default = model.predict_proba(input_encoded)[0][1]  
        probability_approval = 1 - probability_default  

        st.subheader("Loan Prediction Result")

        if prediction[0] == 0:  # predicted no default
            st.success(f"✅ Loan Approved!")
        else:  # predicted default
            st.error(f"❌ Loan Denied!")

        st.info(f"Approval Probability: {probability_approval*100:.2f}%")
else:
    st.info(
        """👋 **Welcome to the Loan Approval Portal**

We're here to help you understand loan eligibility. Please provide the requested financial information on the left.
We'll analyze the data and provide a prediction based on historical trends."""
    )