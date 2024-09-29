from datetime import datetime

import planetary_computer
from pystac_client import Client

from backend.schemas import CloudCoverageRatio, Coordinates
from backend.schemas.landsat.landsat_api import LandsatAPI


class LandsatAPIBySearch(LandsatAPI):
    max_items: int = 5
    limit: int = 5
    coordinates: Coordinates
    start_date: datetime
    end_date: datetime
    max_cloud_cover: CloudCoverageRatio

    def __init__(self, **data):
        super().__init__(**data)
        self._catalog = Client.open(self.base_url, modifier=planetary_computer.sign_inplace)
        self._result = self._catalog.search(
            collections=["landsat-c2-l2"],
            limit=self.limit,
            max_items=self.max_items,
            intersects={
                "type": "Point",
                "coordinates": [self.coordinates.latitude, self.coordinates.longitude]
            },
            query={
                "eo:cloud_cover": {
                    "lt": self.max_cloud_cover * 100
                },
            },
            datetime=f"{self.start_date.isoformat()}/{self.end_date.isoformat()}",
        )
