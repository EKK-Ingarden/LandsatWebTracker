import structlog
from fastapi import APIRouter
from fastapi import FastAPI, Request, Response

logger = structlog.get_logger()

coordinates_router = APIRouter()

@coordinates_router.get("/lookup")
async def healthcheck():
    return {"msg": "Coordinates lookup"}


@coordinates_router.get("/scene-detection")
async def read_main():
    return {"msg": "Scene detection"}