from typing import List

import structlog
from fastapi import APIRouter, Depends, Response
from gotrue.types import UserResponse
from sqlalchemy.orm import Session

from backend import schemas
from backend.database import get_db
from backend.models import PixelWatch
from backend.schemas.structures.wmp_params import WatchPixelParams
from backend.utils.auth import get_current_user

logger = structlog.get_logger()

index_router = APIRouter()


@index_router.get("/healthcheck")
async def healthcheck():
    return Response()


@index_router.get("/")
async def read_main():
    logger.info("In root path")
    return {"msg": "Hello World"}


@index_router.get("/get_my_pixel_watches", response_model=List[schemas.PixelWatch])
def get_my_pixel_watches(user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    user_pixel_watches = db.query(PixelWatch).join(user).filter(PixelWatch.user_id == user.user.id).all()

    return user_pixel_watches


@index_router.post("/watch_my_pixel")
async def watch_my_pixel(
    params: WatchPixelParams, user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)
):
    db.add(
        PixelWatch(
            latitude=params.coordinates.latitude,
            longitude=params.coordinates.longitude,
            path=params.wrs_coordinates.wrs_path,
            row=params.wrs_coordinates.wrs_row,
            datetime=params.date,
            user_id=user.user.id,
        )
    )
    db.commit()
