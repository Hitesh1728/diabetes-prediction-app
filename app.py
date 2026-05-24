# app.py
import streamlit as st
import requests

# Configure page
st.set_page_config(page_title="Diabetes Prediction App", page_icon="🩺", layout="centered")

st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient's medical details below to predict the likelihood of diabetes.")

# Create a form for user inputs
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1, step=1)
    glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0, value=120.0)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0.0, max_value=150.0, value=70.0)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0.0, max_value=100.0, value=20.0)

with col2:
    insulin = st.number_input("Insulin Level (IU/mL)", min_value=0.0, max_value=900.0, value=79.0)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
    age = st.number_input("Age", min_value=1, max_value=120, value=33, step=1)

# Prediction button
if st.button("Predict Diabetes", type="primary"):
    # FastAPI endpoint URL (local)
    api_url = "http://127.0.0.1:8000/predict"
    
    # Bundle the data
    patient_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        # Send a POST request to FastAPI
        response = requests.post(api_url, json=patient_data)

        if response.status_code == 200:
            result = response.json()
            prediction_text = result["result"]
            probability = result["probability"]

            st.divider()
            
            # Display results beautifully
            if result["prediction"] == 1:
                st.error(f"### Result: **{prediction_text}**")
                st.write(f"The model predicts a **{probability:.2%}** probability of diabetes.")
                st.warning("Please consult with a healthcare professional for further evaluation.")
            else:
                st.success(f"### Result: **{prediction_text}**")
                st.write(f"The model predicts a **{probability:.2%}** probability of diabetes.")
                st.info("Maintain a healthy lifestyle to keep the risk low!")
        else:
            st.error("Error from the API. Check your backend terminal for details.")

    except requests.exceptions.ConnectionError:
        st.error("Connection Error: Could not reach the API. Please make sure the FastAPI server is running on `http://127.0.0.1:8000`.")