from enum import Enum

from pydantic import BaseModel

from backend.schemas.structures.polygon import Polygon
from backend.schemas.structures.wrs_coordinates import WrsCoordinates


class Mode(str, Enum):
    Ascending = "A"
    Descending = "D"


class TileAttributes(BaseModel):
    coordinates: WrsCoordinates
    mode: Mode
    polygon: Polygon
