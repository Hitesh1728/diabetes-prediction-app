<img width="1914" height="971" alt="Screenshot 2026-05-24 125013" src="https://github.com/user-attachments/assets/81dcaca3-81bf-4d3d-849d-b19036db14ac" />
🩺 Diabetes Prediction App

A modern Machine Learning web application built with Python, Streamlit, and Scikit-learn to predict the likelihood of diabetes based on patient health parameters.

📸 Application Preview

🚀 Features
Predicts diabetes using trained Machine Learning model
Clean and modern Streamlit UI
Real-time prediction probability
User-friendly input form
Responsive dark theme interface
Displays medical recommendation message
🛠️ Tech Stack
Frontend: Streamlit
Backend: Python
Machine Learning: Scikit-learn
Data Processing: Pandas, NumPy
Model Serialization: Pickle / Joblib
📂 Project Structure
Diabetes-Prediction-App/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── diabetes.csv
└── assets/
    └── screenshot.png
📊 Input Parameters

The model predicts diabetes based on:

Pregnancies
Glucose Level
Blood Pressure
Skin Thickness
Insulin Level
BMI
Diabetes Pedigree Function
Age
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py

Application will run on:

http://localhost:8501
🤖 Machine Learning Model

The diabetes prediction model is trained using:

Logistic Regression / Random Forest / XGBoost
PIMA Indians Diabetes Dataset
Feature Scaling using StandardScaler
📈 Prediction Output

The application displays:

Diabetes Prediction Result
Probability Score
Health Recommendation

Example:

Result: Diabetic
Probability: 90%
📦 Requirements

Example dependencies:

streamlit
scikit-learn
pandas
numpy
joblib
🌐 Deployment

 deploy the app on:

Streamlit Cloud
Render

👨‍💻 Author

Developed by Hitesh Raisharma

📜 License

This project is licensed under the MIT License.
