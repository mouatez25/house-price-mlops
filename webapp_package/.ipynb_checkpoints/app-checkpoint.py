
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("../models/prod/house_price_model.pkl")

st.title("🏡 House Price Prediction")

st.write("Enter the house features below:")

size_sqft = st.number_input("Size (sqft)", min_value=100, max_value=10000, value=1500)
num_bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
crime_rate = st.slider("Crime Rate", 0.0, 1.0, 0.1)
proximity_to_schools = st.slider("Proximity to Schools", 0.0, 1.0, 0.8)
lot_size = st.number_input("Lot Size (acres)", min_value=0.01, max_value=10.0, value=0.5)
year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2010)

if st.button("Predict Price"):
    features = {
        "size_sqft": size_sqft,
        "num_bedrooms": num_bedrooms,
        "crime_rate": crime_rate,
        "proximity_to_schools": proximity_to_schools,
        "lot_size": lot_size,
        "year_built": year_built
    }
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    st.success(f"🏷️ Estimated House Price: ${prediction:,.2f}")
