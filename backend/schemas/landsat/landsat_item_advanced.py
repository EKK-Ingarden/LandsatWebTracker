from typing import List

from pydantic import BaseModel

from backend.schemas.landsat.landsat_item import LandsatItem


class ReflectanceChartElement(BaseModel):
    wave_length: float
    reflectance: float


class LandsatAdvancedItem(LandsatItem):
    temp_chart: List[ReflectanceChartElement]
