from typing import List

from pydantic import AliasChoices, BaseModel, Field

from backend.schemas.landsat.landsat_item import LandsatItem


class ReflectanceChartElement(BaseModel):
    wave_length: float
    reflectance: float


class TemperatureChartElement(BaseModel):
    temperature: float
    distribution: float


class Metadata(BaseModel):
    created: str
    instruments: list[str]
    sun_azimuth: float = Field(validation_alias=AliasChoices("sun_azimuth", "view:sun_azimuth"))
    sun_elevation: float = Field(validation_alias=AliasChoices("sun_elevation", "view:sun_elevation"))
    cloud_cover: float = Field(validation_alias=AliasChoices("cloud_cover", "landsat:cloud_cover_land"))
    collection_number: str = Field(validation_alias=AliasChoices("collection_number", "landsat:collection_number"))
    collection_category: str = Field(
        validation_alias=AliasChoices("collection_category", "landsat:collection_category")
    )


class LandsatAdvancedItem(LandsatItem):
    reflectance_chart: List[ReflectanceChartElement]
    temperature_chart: List[TemperatureChartElement]
    metadata: Metadata
