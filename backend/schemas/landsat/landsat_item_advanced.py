from typing import List

from pydantic import BaseModel

from backend.schemas.landsat.landsat_item import LandsatItem


class ReflectanceChartElement(BaseModel):
    wave_length: float
    reflectance: float


class TemperatureChartElement(BaseModel):
    temperature: float
    distribution: float


class LandsatAdvancedItem(LandsatItem):
    reflectance_chart: List[ReflectanceChartElement]
    temperature_chart: List[TemperatureChartElement]
