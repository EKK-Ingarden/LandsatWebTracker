from datetime import datetime

from pydantic import BaseModel

from .. import WrsCoordinates
from .coordinates import Coordinates


class WatchPixelParams(BaseModel):
    coordinates: Coordinates
    wrs_coordinates: WrsCoordinates
    date: datetime

