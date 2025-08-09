import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

st.title("💳 Credit Card Fraud Detection")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    # Load the file
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:", data.head())

    if st.button("Detect Fraud"):
        # Copy the data to transform it
        df = data.copy()

        # Encode categorical (string) columns into numbers
        for col in df.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

        # Train Isolation Forest model
        model = IsolationForest(contamination=0.001, random_state=42)
        model.fit(df)

        # Predictions (-1 means anomaly/fraud)
        predictions = model.predict(df)
        data['Fraudulent'] = ["Yes" if p == -1 else "No" for p in predictions]

        st.write("Fraud Detection Results:", data)
        st.download_button(
            label="Download Results as CSV",
            data=data.to_csv(index=False),
            file_name="fraud_results.csv",
            mime="text/csv"
        )
