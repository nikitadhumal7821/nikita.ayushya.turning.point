import streamlit as st
import pandas as pd
import joblib

# Page Title
st.title("AI-Based Horoscope & Personality Prediction System")
st.subheader("Ayushya Turning Point Algorithm")

# User Inputs via Streamlit Interface
st.sidebar.header("Enter Birth Details")
dob = st.sidebar.text_input("Date of Birth (DD/MM/YYYY)", "02/05/2003")
time_birth = st.sidebar.text_input("Time of Birth", "10:30 AM")
place_birth = st.sidebar.text_input("Place of Birth", "Pune")

# Ayushya Turning Point Logic
def ayushya_turning_point(dob_string):
    try:
        day, month, year = map(int, dob_string.split('/'))
        digit_sum = sum(int(digit) for digit in str(year))
        first_tp = year + digit_sum
        second_digit_sum = sum(int(digit) for digit in str(first_tp))
        second_tp = first_tp + second_digit_sum
        return [year, first_tp, second_tp]
    except Exception:
        return [2003, 2008, 2018]

# Prediction Execution Button
if st.sidebar.button("Predict Horoscope & Turning Points"):
    turning_points = ayushya_turning_point(dob)
    
    st.write("### Analysis Results")
    st.write(f"**Birth Year:** {turning_points[0]}")
    st.write(f"**Ayushya Turning Point 1:** {turning_points[1]}")
    st.write(f"**Ayushya Turning Point 2:** {turning_points[2]}")
    
    try:
        # Load the saved Random Forest model
        model = joblib.load('random_forest_model.pkl')
        
        # Prepare processed feature vector matching your training pipeline
        sample_input = pd.DataFrame([[1, 0, 1, turning_points[1]]]) 
        
        prediction = model.predict(sample_input)
        st.success(f"**Predicted Horoscope Category:** {prediction[0]}")
        
    except FileNotFoundError:
        st.warning("Model file ('random_forest_model.pkl') not found. Please upload your trained model to GitHub.")
