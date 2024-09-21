from datetime import datetime
from typing import List

import structlog
from fastapi import APIRouter

from backend.schemas import CloudCoverageRatio, Coordinates, LandsatAPI, LandsatItem

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
