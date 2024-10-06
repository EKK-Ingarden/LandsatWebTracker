import json

from fastapi import FastAPI

from backend.routers.index_router import index_router
from backend.routers.landsat_api_router import landsat_api_router
from backend.routers.reports_router import reports_router
from backend.routers.watch_my_pixel import watch_my_pixel_router


def create_app():
    new_app = FastAPI(title="Landsat Web Tracker API")
    new_app.include_router(index_router, prefix="")
    new_app.include_router(landsat_api_router, prefix="/landsat")
    new_app.include_router(reports_router, prefix="/reports")
    new_app.include_router(watch_my_pixel_router, prefix="/watch_my_pixel")

    return new_app


def write_openapi():
    with open("frontend/openapi/api/openapi.json", "w") as f:
        json.dump(create_app().openapi(), f)
