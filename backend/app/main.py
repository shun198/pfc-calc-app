from fastapi import FastAPI

from app.presentation.api.routes.health import router as health_router
from app.presentation.api.routes.meals import router as meals_router

app = FastAPI(title="PFC Calc API", version="0.1.0")

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(meals_router, prefix="/api/v1", tags=["meals"])
