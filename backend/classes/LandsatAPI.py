from datetime import datetime

from backend.classes import LandsatData
from backend.types import BBoxType


class LandsatAPI:
    base_url = NotImplementedError

    def __init__(self):
        raise NotImplementedError

    def search(self, bbox: BBoxType,
               start_date: datetime,
               end_date: datetime,
               limit: int,
               cloud_cover,
               sort_by) -> [LandsatData]:

        raise NotImplementedError

    def fetch(self, bbox: BBoxType,
              start_date: datetime,
              end_date: datetime,
              limit: int) -> LandsatData:

        raise NotImplementedError
