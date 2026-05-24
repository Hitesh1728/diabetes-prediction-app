# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the saved model and scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize FastAPI app
app = FastAPI(title="Diabetes Prediction API")

# Define the expected JSON data format using Pydantic
class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API. Use the /predict endpoint."}

@app.post("/predict")
def predict_diabetes(data: DiabetesData):
    # Convert input data to numpy array
    input_features = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])

    # Scale the input data
    scaled_features = scaler.transform(input_features)

    # Make prediction
    prediction = model.predict(scaled_features)
    probability = model.predict_proba(scaled_features)[0][1]

    # Return results
    return {
        "prediction": int(prediction[0]),
        "probability": float(probability),
        "result": "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    }