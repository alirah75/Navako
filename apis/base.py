from apis.routes import route_health, route_prediction

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(route_prediction.router, prefix="/predict", tags=["Predict"])
api_router.include_router(route_health.router, prefix="/health", tags=["Health"])
