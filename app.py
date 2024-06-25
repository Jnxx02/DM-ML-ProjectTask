import streamlit as st
import pandas as pd
import pickle

# Set page configuration
st.set_page_config(page_title="Vehicle Insurance Fraud Detection", page_icon="🚗")

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
st.markdown("This web application can detect fraud in accident insurance claims by allowing users to input transaction data through a form. The data is then sent to the server to be processed using a machine learning model to determine whether the transaction is fake or not. The classification results are immediately returned and displayed to the user on the same page.")

# Menampilkan informasi mengenai Vehicle Insurance Claim Fraud
st.markdown("## About Vehicle Insurance Claim Fraud")
st.markdown("""
Vehicle insurance claim fraud is a significant issue that affects insurance companies and policyholders alike. Here are some key points about vehicle insurance claim fraud:

- **Definition**: Vehicle insurance claim fraud involves providing false information or exaggerating details in an insurance claim to receive compensation that is not deserved.
- **Common Types**:
  - **Staged Accidents**: Deliberately causing an accident to file a claim.
  - **Exaggerated Claims**: Inflating the extent of damages or injuries.
  - **False Claims**: Filing claims for accidents or damages that never occurred.
- **Statistics**:
  - According to a study published in ScienceDirect, fraud accounts for a significant portion of the property-casualty insurance industry's incurred losses and loss adjustment expenses each year.
  - The FBI estimates that the total cost of insurance fraud (non-health insurance) is more than $40 billion per year.
- **Impact**:
  - Increases insurance premiums for all policyholders.
  - Leads to higher operational costs for insurance companies.
  - Can result in legal consequences for those caught committing fraud.
- **Detection Methods**:
  - **Data Analysis**: Using machine learning models to identify patterns and anomalies in claims data.
  - **Investigation**: Conducting thorough investigations of suspicious claims.
  - **Collaboration**: Sharing information between insurance companies and law enforcement agencies.

By understanding the nature and impact of vehicle insurance claim fraud, we can better appreciate the importance of detection and prevention efforts.
""")

st.markdown("## References")
st.markdown("""
- [ScienceDirect Study on Insurance Fraud](https://www.sciencedirect.com/science/article/abs/pii/S0275531922001556)
- [FBI Insurance Fraud](https://www.fbi.gov/stats-services/publications/insurance-fraud)
""")

# Sidebar for user input
st.sidebar.header("Input Parameters for Fraud Detection")
st.sidebar.markdown("Please provide the following details to help us detect potential fraud in vehicle insurance claims:")

# User input
month = st.sidebar.selectbox("Month of Incident", list(month_mapping.keys()), help="Month when the incident or claim occurred. This can help identify seasonal patterns in fraud cases.")
day_of_week = st.sidebar.selectbox("Day of Week of Incident", list(day_of_week_mapping.keys()), help="Day of the week when the incident occurred. The date of the incident can reveal fraud patterns.")
policy_type_utility_liability = st.sidebar.selectbox("Policy Type Utility - Liability", ["Yes", "No"], help="Type of policy, specifically utility and liability policies. The type of policy can influence fraud tendencies.")
age = st.sidebar.slider("Age", 18, 59, help="Age of the policyholder or those involved in the incident. Age can provide indications about claim patterns.")
day_of_week_claimed = st.sidebar.selectbox("Day of Week Claimed", list(day_of_week_claimed_mapping.keys()), help="Day of the week when the claim was filed. This can be used to see if claims are filed more frequently on certain days.")
week_of_month = st.sidebar.slider("Week of Month of Incident", 1, 5, help="Week of the month when the incident occurred. This can show if there are specific patterns in the week of the month when fraud occurs.")
week_of_month_claimed = st.sidebar.slider("Week of Month Claimed", 1, 5, help="Week of the month when the claim was filed. Similar to WeekOfMonth, but for filed claims.")

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

# Sidebar for prediction result
if st.sidebar.button("Predict"):
    prediction = model.predict(input_df)
    st.sidebar.markdown("### Prediction Result")
    st.sidebar.write("Prediction: ", "🚨 Fraud" if prediction[0] == 1 else "✅ Not Fraud")
