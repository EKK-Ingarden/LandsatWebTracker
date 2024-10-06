from typing import List

import structlog
from fastapi import APIRouter, Depends
from gotrue import Session, UserResponse

from backend import models, schemas
from backend.database import get_db
from backend.schemas.structures.wmp_params import WatchPixelParams
from backend.utils.auth import get_current_user

logger = structlog.get_logger()

watch_my_pixel_router = APIRouter()


@watch_my_pixel_router.post("/watch")
async def watch_my_pixel(
    params: WatchPixelParams, user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)
):
    db.add(
        models.PixelWatch(
            latitude=params.coordinates.latitude,
            longitude=params.coordinates.longitude,
            path=params.wrs_coordinates.wrs_path,
            row=params.wrs_coordinates.wrs_row,
            datetime=params.date,
            user_id=user.user.id,
        )
    )
    db.commit()


@watch_my_pixel_router.get("/get_list", response_model=List[schemas.PixelWatch])
def get_my_pixel_watches(user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    user_pixel_watches = (
        db.query(models.PixelWatch).join(models.User).filter(models.PixelWatch.user_id == user.user.id).all()
    )

    return user_pixel_watches
