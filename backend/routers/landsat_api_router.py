from datetime import date, datetime
from typing import List, Optional

import structlog
from fastapi import APIRouter

from backend.schemas import CloudCoverageRatio, Coordinates, LandsatAPI, LandsatItem
from backend.schemas.structures.tile_attributes import Mode
from backend.utils.acquisitions_utils import AcquisitionsUtils
from backend.utils.geo_location_utils import WRS2Utils

logger = structlog.get_logger()

landsat_api_router = APIRouter()


@landsat_api_router.get("/search")
async def search(latitude: float,
                 longitude: float,
                 start_date: datetime,
                 end_date: datetime,
                 max_cloud_cover: CloudCoverageRatio = 0.2,
                 max_items: int = 5,
                 limit: int = 5) -> List[LandsatItem]:
    landsat_api = LandsatAPI(
        coordinates=Coordinates(lat=latitude, lon=longitude),
        start_date=start_date,
        end_date=end_date,
        max_cloud_cover=max_cloud_cover,
        max_items=max_items,
        limit=limit
    )

    results = list(landsat_api.all_results)

    return results


@landsat_api_router.get("/get_acquisitions")
async def get_acquisitions(path: int, from_date: date, to_date: Optional[date] = None):
    utils = AcquisitionsUtils()
    await utils.load_acquisitions()
    return utils.get_acquisitions(path, from_date, to_date=to_date)


@landsat_api_router.get("/get_scene")
async def get_scene(lat: int, lng: int, mode: Optional[Mode] = None):
    tiles = await WRS2Utils.get_wrs2_tiles(lat, lng, mode)
    return tiles
