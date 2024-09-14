import structlog
from fastapi import APIRouter
from fastapi import FastAPI, Request, Response

logger = structlog.get_logger()

coordinates_router = APIRouter()

@coordinates_router.get("/lookup")
async def coordinates_lookup():
    return {"msg": "Coordinates lookup"}


@coordinates_router.get("/scene-detection")
async def scene_detection():
    return {"msg": "Scene detection"}