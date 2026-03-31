# 🏦 Loan Approval Prediction System (Based on Default Risk)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-red?logo=streamlit&logoColor=white)](https://aymankhan555-loan-approval-app.streamlit.app/)

👉 **Live Demo:**  
🔗 https://aymankhan555-loan-approval-app.streamlit.app/

---

## 📌 Project Overview
Loan approval is a critical decision-making process for financial institutions. Incorrect approvals can lead to significant financial losses due to borrower defaults.

This project presents a **Loan Approval Prediction System** that predicts **default risk** and converts it into an approval decision:

- **Low default risk → Loan Approved ✅**
- **High default risk → Loan Not Approved ❌**

---

## 🎯 Problem Statement
Given borrower demographic and financial data, the goal is to:

- Predict **loan default risk**
- Convert it into a **loan approval decision**
- Help minimize financial loss

---

## 🧠 Project Logic

| Model Prediction | Meaning | Final Decision |
|----------------|--------|---------------|
| 0              | No Default | ✅ Loan Approved |
| 1              | Default    | ❌ Loan Not Approved |

---

## 📊 Dataset Information

### 🔹 Target Variable
- `loan_status`
  - `0` → No Default
  - `1` → Default

### 🔹 Categorical Features
- person_home_ownership  
- loan_intent  
- loan_grade  
- cb_person_default_on_file  

### 🔹 Numerical Features
- person_age  
- person_income  
- person_emp_length  
- loan_amnt  
- loan_int_rate  
- loan_percent_income  
- cb_person_cred_hist_length  

---

## 🧹 Data Preprocessing
- Missing value handling  
- Duplicate removal  
- Range validation  
- Data cleaning  

---

## 📈 Exploratory Data Analysis
- Target distribution  
- Feature distributions  
- Default rates across categories  
- Correlation analysis  

---

## ⚙️ Model Development
- Feature engineering  
- Models used:
  - 🌲 Random Forest  
  - 🚀 XGBoost  

---

## 🔧 Hyperparameter Tuning
- Performed using **Optuna**  
- Optimized XGBoost performance  

---

## 📊 Model Performance
- ✅ Accuracy: ~92%  
- ✅ Strong detection of risky borrowers  
- ✅ Helps reduce financial loss  

---

## 🔍 Feature Importance
Key influencing factors:
- Loan-to-income ratio  
- Interest rate  
- Credit history length  
- Income level  
- Previous default history  

---

## 🌐 Streamlit Web Application

An interactive web app built with Streamlit:

- Input applicant details  
- Get instant loan approval prediction  
- View approval probability  

---

## 🖼️ App Preview

> 📸 Add your screenshot in the repo and update the path below

![App Screenshot](app_screenshot.png)

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run loan_approval_app.py
