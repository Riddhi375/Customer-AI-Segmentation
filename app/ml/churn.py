import joblib
import os

MODEL_PATH = os.path.join("trained_models", "churn_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_churn(age: int, income: int, orders: int):
    prediction = model.predict([[age, income, orders]])

    if prediction[0] == 1:
        return "High Risk"

    return "Low Risk"