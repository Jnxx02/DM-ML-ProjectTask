import streamlit as st
import pandas as pd
import joblib
from utils import preprocess_data

# Memuat model yang telah dilatih
model = joblib.load('model/fraud_model.pkl')

# Menampilkan judul aplikasi
st.title("Fraud Detection on Transactions")

# Membuat form untuk input data pengguna
st.header("Input Transaction Data")
with st.form("transaction_form"):
    # Input untuk nomor polis
    policy_number = st.number_input("Policy Number", min_value=0, step=1)
    # Input untuk nomor perwakilan
    rep_number = st.number_input("Representative Number", min_value=0, step=1)
    # Input untuk rating pengemudi
    driver_rating = st.number_input("Driver Rating", min_value=0, step=1)
    
    # Tombol untuk submit form
    submit_button = st.form_submit_button(label="Check for Fraud")

# Memproses data input dan melakukan prediksi
if submit_button:
    # Membuat DataFrame dari data input
    input_data = pd.DataFrame({
        'PolicyNumber': [policy_number],
        'RepNumber': [rep_number],
        'DriverRating': [driver_rating]
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
