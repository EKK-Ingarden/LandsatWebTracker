from datetime import datetime

from pydantic import BaseModel

from backend.schemas.structures.user import UserBase


class PixelWatch(BaseModel):
    id: int
    user: UserBase
    latitude: float
    longitude: float
    datetime: datetime

    class Config:
        from_attributes = True
