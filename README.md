#  Loan Approval Prediction System (Based on Default Risk)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-green)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


 **Live Demo:**  
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-red?logo=streamlit&logoColor=white)](https://aymankhan555-loan-approval-app.streamlit.app/)

---

##  Project Overview
Loan approval is a critical decision-making process for financial institutions. Incorrect approvals can lead to significant financial losses due to borrower defaults.

This project presents a **Loan Approval Prediction System** that predicts **default risk** and converts it into an approval decision:

- **Low default risk → Loan Approved ✅**
- **High default risk → Loan Not Approved ❌**

---

##  Problem Statement
Given borrower demographic and financial data, the goal is to:

- Predict **loan default risk**
- Convert it into a **loan approval decision**
- Help minimize financial loss

---

##  Project Logic

| Model Prediction | Meaning | Final Decision |
|----------------|--------|---------------|
| 0              | No Default | ✅ Loan Approved |
| 1              | Default    | ❌ Loan Not Approved |

---

##  Dataset Information

### 🔹 Target Variable
- **loan_status**: Indicates whether the borrower defaulted  
  - `1` = Default  
  - `0` = No Default  

---

### 🔹 Categorical Features
- **person_home_ownership**: Type of home ownership (e.g., RENT, OWN, MORTGAGE)  
- **loan_intent**: Purpose of the loan (e.g., EDUCATION, MEDICAL, PERSONAL, HOMEIMPROVEMENT)  
- **loan_grade**: Risk grade assigned to the loan by the lender (A to G)  
- **cb_person_default_on_file**: Indicates whether the borrower has any prior default (Y/N)  

---

### 🔹 Numerical Features
- **person_age**: Age of the borrower (in years)  
- **person_income**: Annual income of the borrower (USD)  
- **person_emp_length**: Employment length (in years)  
- **loan_amnt**: Loan amount requested (USD)  
- **loan_int_rate**: Interest rate of the loan (%)  
- **loan_percent_income**: Loan amount as a percentage of income  
- **cb_person_cred_hist_length**: Length of credit history (in years)   

---

## 🔹 Data Preprocessing
- Missing value handling  
- Duplicate removal  
- Range validation  
- Data cleaning  

---

## 🔹 Exploratory Data Analysis
- Target distribution  
- Feature distributions  
- Default rates across categories  
- Correlation analysis  

---

## 🔹 Model Development
- Feature engineering  
- Models used:
  -  Random Forest  
  -  XGBoost  

---

## 🔹 Hyperparameter Tuning
- Performed using **Optuna**  
- Optimized XGBoost performance  

---

##  Model Performance
### 🔹 Model Comparison

| Model              | ROC AUC |
|--------------------|--------|
| Random Forest      | 0.938 |
| XGBoost (Baseline) | 0.953 |
| ⭐ XGBoost (Tuned) | **0.956** |

---

### 🏆 Best Model: Tuned XGBoost

The **tuned XGBoost model** achieved the best performance among all models and was selected as the final model for deployment.

---

### 🔹 Performance Metrics

- ✅ **Accuracy:** ~92%  
- ✅ **ROC-AUC:** ~0.96  
- ✅ **Recall (Default Detection):** ~84%  
- ✅ **Precision:** ~75%  

---

###  Model Insights

The tuned XGBoost model performs effectively in identifying risky borrowers:

- It correctly detects **84% of actual defaults**, which is crucial for minimizing financial losses.  
- It maintains a **precision of 75%**, reducing unnecessary rejection of safe applicants.  
- Most non-default borrowers are classified correctly, contributing to an overall **accuracy of 92%**.  
- A **ROC-AUC score of 0.96** indicates strong overall classification performance.  

---



##  Feature Importance
Key influencing factors:
- Loan-to-income ratio  
- Interest rate  
- Credit history length  
- Income level  
- Previous default history  

---

## 🌐 Streamlit Web Application

An interactive web app built with Streamlit:
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-red?logo=streamlit&logoColor=white)](https://aymankhan555-loan-approval-app.streamlit.app/)
- Input applicant details  
- Get instant loan approval prediction  
- View approval probability  

---

##  App Preview



![App Screenshot](app_screenshot.png)

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run loan_approval_app.py
```

##  Conclusion
...conclusion...

---

## 🤝 Let's Connect

If you found this project interesting or useful:

⭐ Star the repo  
🍴 Fork it  
💬 Give feedback  

---



##  Future Improvements

- **Explore additional ML models:** LightGBM, CatBoost, and Neural Networks to improve prediction performance  
- **Advanced hyperparameter tuning:** Optimize models for better accuracy and generalization  
- **Deep learning integration:** Capture complex patterns in borrower data  
- **Enhanced UI/UX:** Improve Streamlit interface with advanced components for better user experience   
- **Automated notifications:** Integrate AI agent to send decision updates via email  
- **Model monitoring:** Track model performance in production for reliability and risk management    
