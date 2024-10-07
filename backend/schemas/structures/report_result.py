from datetime import datetime

from pydantic import BaseModel

from backend.schemas.landsat.landsat_item_advanced import LandsatAdvancedItem


class ReportResult(BaseModel):
    scene_id: str

    def __init__(self, **data):
        super().__init__(**data)

        print(f"executing {self.__class__.__name__} with data: {data}")


class ReportResultError(ReportResult):
    error: str


class ReportResultProcess(ReportResult):
    is_processed: bool
    created_at: datetime


class ReportResultSuccess(ReportResultProcess):
    data: LandsatAdvancedItem
