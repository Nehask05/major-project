import streamlit as st
import pandas as pd
import joblib

# Load trained models
rf_model = joblib.load("rf_model.pkl")
log_model = joblib.load("log_model.pkl")

st.title("💳 UPI Fraud Detection App")
st.write("Enter transaction details to check if it is **Fraudulent or Legitimate**.")

# User input fields
amount = st.number_input("Transaction Amount (INR)", min_value=1.0, max_value=1000000.0, step=100.0)
transaction_type = st.selectbox("Transaction Type", ["P2P", "Merchant", "Bill"])
device_type = st.selectbox("Device Type", ["Mobile", "Web", "POS"])
transaction_hour = st.slider("Transaction Hour (0-23)", 0, 23, 12)

# YES/NO fields
is_new_device = st.radio("Is New Device?", ["Yes", "No"])
is_international = st.radio("Is International Transaction?", ["Yes", "No"])
daily_count = st.slider("Transactions Today", 1, 10, 1)
previous_fraud = st.radio("User Previous Fraud History?", ["Yes", "No"])

# Convert Yes/No → 1/0
is_new_device = 1 if is_new_device == "Yes" else 0
is_international = 1 if is_international == "Yes" else 0
previous_fraud = 1 if previous_fraud == "Yes" else 0

# Convert inputs into DataFrame
input_data = pd.DataFrame([[
    amount,
    {"P2P": 0, "Merchant": 1, "Bill": 2}[transaction_type],
    {"Mobile": 0, "Web": 1, "POS": 2}[device_type],
    transaction_hour,
    is_new_device,
    is_international,
    daily_count,
    previous_fraud
]], columns=['Amount','TransactionType','DeviceType','TransactionHour',
             'IsNewDevice','IsInternational','DailyTransactionCount','PreviousFraudFlag'])

# Predict button
if st.button("Check Fraud"):
    rf_pred = rf_model.predict(input_data)[0]
    log_pred = log_model.predict(input_data)[0]

    st.subheader("🔍 Prediction Results")
    st.write(f"**Random Forest Model:** {'Fraud 🚨' if rf_pred==1 else 'Legitimate ✅'}")
    st.write(f"**Logistic Regression Model:** {'Fraud 🚨' if log_pred==1 else 'Legitimate ✅'}")

    # ---- ACTION BUTTON IF FRAUD DETECTED ----
    if rf_pred == 1 or log_pred == 1:
        st.warning("⚠️ Suspicious Activity Detected!")

        st.markdown("""
        ### 🔗 Take Immediate Action  
        Click the button below to report this as a fraud transaction.
        """)
        
        fraud_url = "https://www.cybercrime.gov.in/"  # Official portal

        st.link_button("🚨 Report Fraud Now", fraud_url)