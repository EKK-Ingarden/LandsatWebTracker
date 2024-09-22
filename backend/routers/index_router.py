from typing import List

import structlog
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from backend import models, schemas
from backend.database import get_db

logger = structlog.get_logger()

index_router = APIRouter()


@index_router.get("/healthcheck")
async def healthcheck():
    return Response()


@index_router.get("/")
async def read_main():
    logger.info("In root path")
    return {"msg": "Hello World"}


@index_router.get("/get_pixel_watch", response_model=List[schemas.PixelWatch])
def get_pixel_watch(db: Session = Depends(get_db)):
    users = db.query(models.PixelWatch).all()
    return users
