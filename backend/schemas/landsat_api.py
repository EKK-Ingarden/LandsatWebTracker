from datetime import datetime

import planetary_computer
from pydantic import BaseModel
from pystac import Item
from pystac_client import Client

from backend.schemas.structures.cloud_coverage_ratio import CloudCoverageRatio
from backend.schemas.structures.coordinates import Coordinates
from backend.schemas.structures.landsat_item import LandsatItem
from backend.schemas.structures.wrs_coordinates import WrsCoordinates
from backend.settings import settings
from backend.utils.polygon_utils import polygon_from_nested_list


class LandsatAPI(BaseModel):
    coordinates: Coordinates
    start_date: datetime
    end_date: datetime
    max_cloud_cover: CloudCoverageRatio
    max_items: int = 5
    limit: int = 5

    base_url: str = settings.landsat_provider_url

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

    @staticmethod
    def _landsat_item_builder(item: Item):
        return LandsatItem(
            id=item.id,
            datetime=item.datetime,
            eo_cloud_cover=item.properties["eo:cloud_cover"] / 100,
            wrs_coordinates=WrsCoordinates(
                path=item.properties["landsat:wrs_path"],
                row=item.properties["landsat:wrs_row"],
            ),
            rendered_preview=item.assets["rendered_preview"].href,
            polygon=polygon_from_nested_list(item.geometry["coordinates"]),
            green=item.assets["green"].href,
            red=item.assets["red"].href,
            blue=item.assets["blue"].href,
        )

    @property
    def pages(self):
        """
        Get the page from the ItemSearch object
        """
        return self._result.pages()

    @property
    def all_results(self):
        """
        returns results in LandsatItem class format
        """
        for item in self._result.items():
            yield self._landsat_item_builder(item)
