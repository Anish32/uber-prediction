import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from the pickle file
with open('uber_fare_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("Uber Fare Prediction")

# Input fields
pickup_longitude = st.number_input("Pickup Longitude", value=-73.9735)  # Example default value
pickup_latitude = st.number_input("Pickup Latitude", value=40.7830)  # Example default value
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.9735)  # Example default value
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.7830)  # Example default value



# Prediction
if st.button("Predict Fare"):
    # Create input data
    # Indented this block of code to be executed when the button is clicked
    input_data = pd.DataFrame([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude]])  
    input_data.columns = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']  

    # Make prediction
    # Indented this line as well
    prediction = model.predict(input_data)[0]

    # Indented this line as well
    st.write(f"Predicted Fare: ${prediction:.2f}")
