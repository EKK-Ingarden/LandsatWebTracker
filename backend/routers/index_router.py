from typing import List

import structlog
from backend import models, schemas
from backend.database import get_db
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

logger = structlog.get_logger()

index_router = APIRouter()


@index_router.get("/healthcheck")
async def healthcheck():
    return Response()


@index_router.get("/")
async def read_main():
    logger.info("In root path")
    return {"msg": "Hello World"}


@index_router.get("/get_users", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
