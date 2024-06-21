import streamlit as st
import pandas as pd
import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Mapping dictionaries
month_mapping = {
    'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
    'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
}

day_of_week_mapping = {
    'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
    'Friday': 4, 'Saturday': 5, 'Sunday': 6
}

day_of_week_claimed_mapping = {
    'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4,
    'Friday': 5, 'Saturday': 6, 'Sunday': 7
}

# Menampilkan judul aplikasi
st.title("🚗 Vehicle Insurance Claim Fraud Detection")
st.markdown("## Welcome to the Fraud Detection App")
st.markdown("This application helps in detecting fraudulent vehicle insurance claims.")

# Sidebar for user input
st.sidebar.header("User Input Parameters")
st.sidebar.markdown("Please provide the following details:")

# Input dari pengguna
month = st.sidebar.selectbox("Month of Incident (Bulan saat kejadian)", list(month_mapping.keys()), help="Bulan saat kejadian atau klaim terjadi. Ini bisa membantu dalam mengidentifikasi pola musiman dalam kasus kecurangan.")
day_of_week = st.sidebar.selectbox("Day of Week of Incident (Hari dalam minggu saat kejadian)", list(day_of_week_mapping.keys()), help="Hari dalam minggu saat kejadian terjadi. Tanggal kejadian bisa mengungkapkan pola kecurangan.")
policy_type_utility_liability = st.sidebar.selectbox("Policy Type Utility - Liability (Jenis polis)", ["Yes", "No"], help="Jenis polis, khususnya polis utilitas dan tanggung jawab. Jenis polis bisa mempengaruhi kecenderungan kecurangan.")
age = st.sidebar.slider("Age (Usia)", 17, 65, help="Usia pemegang polis atau yang terlibat dalam kejadian. Usia bisa memberikan indikasi tentang pola klaim.")
day_of_week_claimed = st.sidebar.selectbox("Day of Week Claimed (Hari dalam minggu saat klaim diajukan)", list(day_of_week_claimed_mapping.keys()), help="Hari dalam minggu saat klaim diajukan. Ini bisa digunakan untuk melihat apakah klaim diajukan pada hari-hari tertentu lebih sering.")
week_of_month = st.sidebar.slider("Week of Month of Incident (Minggu dalam bulan saat kejadian)", 1, 5, help="Minggu dalam bulan saat kejadian terjadi. Ini bisa menunjukkan apakah ada pola tertentu dalam minggu bulan saat kecurangan terjadi.")
week_of_month_claimed = st.sidebar.slider("Week of Month Claimed (Minggu dalam bulan saat klaim diajukan)", 1, 5, help="Minggu dalam bulan saat klaim diajukan. Sama dengan WeekOfMonth, tapi untuk klaim yang diajukan.")

# Preprocess input
input_data = {
    'Month': month_mapping[month],
    'DayOfWeek': day_of_week_mapping[day_of_week],
    'PolicyType_Utility - Liability': 1 if policy_type_utility_liability == "Yes" else 0,
    'Age': age,
    'DayOfWeekClaimed': day_of_week_claimed_mapping[day_of_week_claimed],
    'WeekOfMonth': week_of_month,
    'WeekOfMonthClaimed': week_of_month_claimed
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.markdown("### Prediction Result")
    st.write("Prediction: ", "🚨 Fraud" if prediction[0] == 1 else "✅ Not Fraud")
