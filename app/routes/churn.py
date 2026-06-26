from fastapi import APIRouter

from app.ml.churn import predict_churn

router = APIRouter(
    prefix="/churn",
    tags=["Churn Prediction"]
)

@router.get("/")
def predict(age: int, income: int, orders: int):

    risk = predict_churn(age, income, orders)

    return {
        "age": age,
        "income": income,
        "orders": orders,
        "risk": risk
    }