from fastapi import APIRouter

from app.ml.segmentation import segment_customers

router = APIRouter(
    prefix="/segmentation",
    tags=["AI Segmentation"]
)


@router.get("/")
def segmentation():

    customers = [
        {"age": 20},
        {"age": 22},
        {"age": 45},
        {"age": 47},
        {"age": 30},
        {"age": 60},
    ]

    return segment_customers(customers)