import json

from fastapi import FastAPI

from backend.routers.auth_router import auth_router
from backend.routers.coordinates_router import coordinates_router
from backend.routers.index_router import index_router
from backend.routers.landsat_api_router import landsat_api_router


def create_app():
    new_app = FastAPI(title="Landsat Web Tracker API")
    new_app.include_router(index_router, prefix="")
    new_app.include_router(coordinates_router, prefix="/coordinates")
    new_app.include_router(landsat_api_router, prefix="/landsat")
    new_app.include_router(auth_router, prefix="/auth")

    return new_app


def write_openapi():
    with open('frontend/openapi/api/openapi.json', 'w') as f:
        json.dump(create_app().openapi(), f)
