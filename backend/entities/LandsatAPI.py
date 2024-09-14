from datetime import datetime

from backend.entities import LandsatData
from backend.entities.BorderBox import BorderBox


class LandsatAPI:
    base_url = NotImplementedError

    def __init__(self):
        raise NotImplementedError

    def search(self, bbox: BorderBox,
               start_date: datetime,
               end_date: datetime,
               limit: int,
               cloud_cover: float,
               sort_by) -> [LandsatData]:

        raise NotImplementedError

    def fetch(self, bbox: BorderBox,
              start_date: datetime,
              end_date: datetime,
              limit: int) -> LandsatData:

        raise NotImplementedError
