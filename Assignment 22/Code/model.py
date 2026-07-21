import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import joblib

# Setup absolute paths so the script works regardless of where it is run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Q1
df = pd.read_csv(os.path.join(BASE_DIR, "heart.csv"))
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

categorical_cols = X.select_dtypes(include=["object", "str"]).columns
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Scaling numerical features
num_cols = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])

# Q2
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Q3
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("Logistic Regression model trained successfully.")

# Q4
y_pred = model.predict(X_test)
print("Actual values (first 10):")
print(y_test.head(10).values)
print("\nPredicted values (first 10):")
print(y_pred[:10])

# Q5
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
TN, FP, FN, TP = cm.ravel()
print(f"TN: {TN}, FP: {FP}, FN: {FN}, TP: {TP}")

# Q6
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Q7
joblib.dump(model, os.path.join(BASE_DIR, "heart_model.pkl"))
joblib.dump(scaler, os.path.join(BASE_DIR, "scaler.pkl"))
joblib.dump(X.columns.tolist(), os.path.join(BASE_DIR, "columns.pkl"))
print("Model, scaler, and columns saved successfully.")

# Q8
loaded_model = joblib.load(os.path.join(BASE_DIR, "heart_model.pkl"))
loaded_scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
loaded_cols = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

sample_data = pd.DataFrame([{
    "Age": 50,
    "Sex": "M",
    "ChestPainType": "ASY",
    "RestingBP": 140,
    "Cholesterol": 288,
    "FastingBS": 0,
    "RestingECG": "Normal",
    "MaxHR": 140,
    "ExerciseAngina": "Y",
    "Oldpeak": 2.0,
    "ST_Slope": "Flat"
}])

sample_encoded = pd.get_dummies(sample_data)

sample_encoded = sample_encoded.reindex(columns=loaded_cols, fill_value=0)

sample_encoded[num_cols] = loaded_scaler.transform(sample_encoded[num_cols])

sample_pred = loaded_model.predict(sample_encoded)
print("Sample Prediction (1=Heart Disease, 0=Normal):", sample_pred[0])
