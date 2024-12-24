from fastapi import FastAPI
from app.controllers import product_controller

app = FastAPI()

# Include routers
app.include_router(product_controller.router, prefix="/api/v1")
