from datetime import datetime
from types import bbox_type

from classes import LandSatData


class LandSatAPI:
    base_url = NotImplementedError

    def __init__(self):
        raise NotImplementedError

    def search(self, bbox: bbox_type,
               start_date: datetime,
               end_date: datetime,
               limit: int,
               cloud_cover,
               sort_by) -> [LandSatData]:

        raise NotImplementedError

    def fetch(self, bbox: bbox_type,
              start_date: datetime,
              end_date: datetime,
              limit: int) -> LandSatData:

        raise NotImplementedError
