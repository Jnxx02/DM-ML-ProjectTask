import streamlit as st
import pandas as pd
import joblib
from utils import preprocess_data

# Memuat model yang telah dilatih
# model = joblib.load('model/fraud_model.pkl')

# Menampilkan judul aplikasi
st.title("Fraud Detection on Transactions")

# Membuat form untuk input data pengguna
st.header("Input Transaction Data")
with st.form("transaction_form"):
    # Input untuk atribut yang diperlukan
    policy_type_sedan_collision = st.number_input("Policy Type - Sedan Collision", min_value=0.0, step=0.1)
    days_policy_claim = st.number_input("Days Policy Claim", min_value=0, step=1)
    gender = st.selectbox("Gender", options=["Male", "Female"])
    deductible = st.number_input("Deductible", min_value=0, step=1)
    week_of_month_claimed = st.number_input("Week of Month Claimed", min_value=0, step=1)
    week_of_month = st.number_input("Week of Month", min_value=0, step=1)
    day_of_week_claimed = st.number_input("Day of Week Claimed", min_value=0, step=1)
    policy_type_utility_liability = st.number_input("Policy Type - Utility Liability", min_value=0.0, step=0.1)
    age = st.number_input("Age", min_value=0, step=1)
    day_of_week = st.number_input("Day of Week", min_value=0, step=1)
    month = st.number_input("Month", min_value=0, step=1)
    month_claimed = st.number_input("Month Claimed", min_value=0, step=1)
    fraud_found_p = st.number_input("Fraud Found P", min_value=0.0, step=0.1)
    
    # Tombol untuk submit form
    submit_button = st.form_submit_button(label="Check for Fraud")

# Memproses data input dan melakukan prediksi
if submit_button:
    # Mengonversi gender menjadi nilai numerik
    if gender == "Male":
        gender_value = 1.0
    elif gender == "Female":
        gender_value = 0.0
    
    # Membuat DataFrame dari data input
    input_data = pd.DataFrame({
        'PolicyType_Sedan_Collision': [policy_type_sedan_collision],
        'Days_Policy_Claim': [days_policy_claim],
        'Gender': [gender_value],
        'Deductible': [deductible],
        'WeekOfMonthClaimed': [week_of_month_claimed],
        'WeekOfMonth': [week_of_month],
        'DayOfWeekClaimed': [day_of_week_claimed],
        'PolicyType_Utility_Liability': [policy_type_utility_liability],
        'Age': [age],
        'DayOfWeek': [day_of_week],
        'Month': [month],
        'MonthClaimed': [month_claimed],
        'FraudFound_P': [fraud_found_p]
    })
    
    # Memproses data input menggunakan fungsi preprocess_data
    processed_data, _ = preprocess_data(input_data)
    # Melakukan prediksi menggunakan model
    prediction = model.predict(processed_data)
    
    # Menampilkan hasil prediksi
    if prediction[0] == 1:
        st.error("This transaction is likely to be fraudulent.")
    else:
        st.success("This transaction is not fraudulent.")
