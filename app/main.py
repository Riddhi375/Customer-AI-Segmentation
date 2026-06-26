from fastapi import FastAPI

from app.database import Base, engine
import app.models

from app.routes.customers import router as customer_router
from app.routes.segmentation import router as segment_router
from app.routes.dashboard import router as dashboard_router
from app.routes.churn import router as churn_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="AI Customer Intelligence Platform"
)

# Register all routers
app.include_router(customer_router)
app.include_router(segment_router)
app.include_router(dashboard_router)
app.include_router(churn_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Customer Intelligence Platform"
    }