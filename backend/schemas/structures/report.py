import datetime
from typing import Optional

from pydantic import BaseModel

from backend.schemas.structures.user import UserBase


class Report(BaseModel):
    scene_id: str
    user: UserBase
    is_processed: bool
    created_at: datetime.datetime
    raw_data: Optional[str]

    class Config:
        from_attributes = True
