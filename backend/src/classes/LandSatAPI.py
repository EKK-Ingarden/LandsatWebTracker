import datetime
from typing import List

bbox_type = List[int, int, int, int]

class LandSatAPI:
    base_url = NotImplementedError

    def __init__(self):
        raise NotImplementedError

    def search(self, bbox: bbox_type,
               start_date: datetime.datetime,
               end_date: datetime.datetime,
               limit: int,
               cloud_cover,
               sort_by):

        raise NotImplementedError

    def fetch(self, bbox: bbox_type,
              start_date: datetime.datetime,
              end_date: datetime.datetime,
              limit: int):

        raise NotImplementedError