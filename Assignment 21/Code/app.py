#Q1
import joblib
import pandas as pd
import streamlit as st
# streamlit: used to build interactive web applications
# pandas: used for data handling, dataframes, and one-hot encoding
# joblib: used to load pre-trained model, scaler, and column objects

# Q2
# Load saved files
model = joblib.load("LR_model.pkl")
scaler = joblib.load("scaler.pkl")
encoded_columns = joblib.load("columns.pkl")

# Q3
# Page configuration
st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)
# layout="centered" centers the content on screen for a clean interface

# Q4
# Title and description
st.title("Ford Car Price Predictor")
st.write("Enter the car details below to predict its selling price.")

# Q5
# Input fields
model_input = st.text_input("Car Model", value="Fiesta")
year = st.number_input(
    "Manufacturing Year (year)",
    min_value=1990,
    max_value=2030,
    value=2018,
    step=1,
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=500000,
    value=15000,
    step=1000
)

tax = st.number_input(
    "Road Tax (tax)",
    min_value=0,
    max_value=1000,
    value=145,
    step=5
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    max_value=200.0,
    value=55.0,
    step=0.5
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    max_value=10.0,
    value=1.5,
    step=0.1
)

# Q6
# Advantage of selectbox: Restricts user input to valid pre-defined options, preventing typos
transmission = st.selectbox(
    "Transmission",
    options=["Automatic", "Manual", "Semi-Auto"]
)
fuelType = st.selectbox(
    "Fuel Type",
    options=["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

# Q7
# Predict button
if st.button("Predict Price"):
    input_data = {
        "model": " " + model_input.strip(),
        "year": year,
        "transmission": transmission,
        "mileage": mileage,
        "fuelType": fuelType,
        "tax": tax,
        "mpg": mpg,
        "engineSize": engineSize,
    }

    # Q8
    df = pd.DataFrame([input_data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=encoded_columns, fill_value=0)

    # Q9
    num_cols = ["year", "mileage", "tax", "mpg", "engineSize"]
    df[num_cols] = scaler.transform(df[num_cols])

    prediction = model.predict(df)[0]
    st.success(f"Predicted Price: £{prediction:.2f}")


