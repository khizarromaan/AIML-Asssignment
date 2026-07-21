import os
import streamlit as st
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Q9
st.title("Heart Disease Prediction")

# Input fields for all features
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=["M", "F"])
cpt = st.selectbox("Chest Pain Type", options=["TA", "ATA", "NAP", "ASY"])
rbp = st.number_input("Resting BP", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", options=[0, 1])
recg = st.selectbox("Resting ECG", options=["Normal", "ST", "LVH"])
maxhr = st.number_input("Max Heart Rate", min_value=50, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina", options=["Y", "N"])
oldpeak = st.number_input("Oldpeak", min_value=-5.0, max_value=10.0, value=0.0)
stslope = st.selectbox("ST Slope", options=["Up", "Flat", "Down"])


# Q10
# Complete Streamlit Web App
try:
    model = joblib.load(os.path.join(BASE_DIR, "heart_model.pkl"))
    scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
    columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))
except FileNotFoundError:
    st.warning("Please run model.py first to train and save the model, scaler, and columns.")
    st.stop()

if st.button("Predict"):
    input_data = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": cpt,
        "RestingBP": rbp,
        "Cholesterol": chol,
        "FastingBS": fbs,
        "RestingECG": recg,
        "MaxHR": maxhr,
        "ExerciseAngina": exang,
        "Oldpeak": oldpeak,
        "ST_Slope": stslope
    }
    
    # Preprocess the input data
    df_input = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df_input)
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)
    
    num_cols = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]
    df_encoded[num_cols] = scaler.transform(df_encoded[num_cols])
    
    # Make a prediction
    prediction = model.predict(df_encoded)[0]
    
    if prediction == 1:
        st.error("Heart Disease: Yes")
    else:
        st.success("Heart Disease: No")
