import json

from backend.routers.coordinates_router import coordinates_router
from backend.routers.index_router import index_router
from fastapi import FastAPI


def create_app():
    new_app = FastAPI(title="Landsat Web Tracker API")
    new_app.include_router(index_router, prefix="")
    new_app.include_router(coordinates_router, prefix="/coordinates")

    return new_app


def write_openapi():
    with open('frontend/openapi/api/openapi.json', 'w') as f:
        json.dump(create_app().openapi(), f)
