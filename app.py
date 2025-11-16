import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------------------
# Load model and scaler
# -------------------------------
model = joblib.load("choco_knn_model.pkl")
scaler = joblib.load("choco_scaler.pkl")

# Page config
st.set_page_config(
    page_title="Chocolate Quality Prediction",
    layout="centered",
    page_icon="🍫"
)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🍫 Chocolate Quality Prediction App")
st.write("Enter chocolate details below to predict its quality.")

# Sidebar
st.sidebar.header("📌 About")
st.sidebar.write("This app predicts chocolate quality using a KNN classifier.")
st.sidebar.write("Model: **KNN (k=5)**")
st.sidebar.write("Preprocessing: **StandardScaler**")

# -------------------------------
# Input Fields
# -------------------------------
st.subheader("🔍 Enter Chocolate Parameters")

# Automatically read column names (except target)
df = pd.read_csv("chocolate_dataset.csv")
feature_columns = df.drop("Quality", axis=1).columns

user_data = []

for col in feature_columns:
    value = st.number_input(f"{col}", step=0.1)
    user_data.append(value)

# Predict Button
if st.button("Predict Quality"):
    # Convert to array
    arr = np.array(user_data).reshape(1, -1)

    # Scale
    arr_scaled = scaler.transform(arr)

    # Prediction
    pred = model.predict(arr_scaled)[0]

    st.success(f"🎉 Predicted Chocolate Quality: **{pred}**")
