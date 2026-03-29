from datetime import date
import streamlit as st
import pandas as pd
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

person_has_owenership = ["RENT", "MORTGAGE", "OWN", "OTHER"]
loan_intent = ["EDUCATION", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "MEDICAL","VENTURE"]
loan_grade = ["A", "B", "C", "D", "E", "F", "G"]
cb_person_default_on_file = ["Y", "N"]

st.sidebar.header("Input Applicant Details")
# Demographic Information and Financial Details


person_age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)

person_income = st.sidebar.number_input("Annual Income", min_value=0, max_value=1000000, value=50000, step=1000)



person_emp_length = st.sidebar.slider('Employment Length (years)', 0, 60, 1)

loan_amnt  = st.sidebar.number_input("Loan Amount", min_value=500, max_value=1000000, value=10000, step=1000)
loan_int_rate = st.sidebar.slider('Loan Interest Rate (%)', 0, 30, 5.0, step=1)
loan_percent_income = st.sidebar.slider('Loan-to-Income Ratio (%)', 0, 1, 0.5, step=0.1) 
cb_person_cred_hist_length = st.sidebar.slider('Credit History Length (years)', 0, 60, 5)