from datetime import datetime

from pydantic import BaseModel

from backend.schemas.structures.user import UserBase


class PixelWatch(BaseModel):
    user: UserBase
    latitude: float
    longitude: float
    path: int
    row: int
    datetime: datetime

    class Config:
        from_attributes = True
