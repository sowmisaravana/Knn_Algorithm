import streamlit as st
import pandas as pd
import joblib

st.title("🍫 Chocolate Quality Prediction App")

model = joblib.load("choco_knn_model.pkl")
scaler = joblib.load("choco_scaler.pkl")

cocoa = st.number_input("Cocoa Percentage (40-90)")
sugar = st.number_input("Sugar Level (5-40)")
milk = st.number_input("Milk Content (0-30)")
brand = st.number_input("Brand Rating (1-5)")

if st.button("Predict"):
    data = pd.DataFrame([[cocoa, sugar, milk, brand]],
                        columns=["Cocoa_Percentage", "Sugar_Level", "Milk_Content", "Brand_Rating"])

    scaled = scaler.transform(data)
    pred = model.predict(scaled)[0]

    if pred == 1:
        st.success("🍫 High Quality Chocolate!")
    else:
        st.error("⚠ Low Quality Chocolate")
