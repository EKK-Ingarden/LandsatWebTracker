import datetime
from typing import Optional

from pydantic import BaseModel


class Report(BaseModel):
    scene_id: str
    is_processed: bool
    created_at: datetime.datetime
    raw_data: Optional[str]

    class Config:
        from_attributes = True

