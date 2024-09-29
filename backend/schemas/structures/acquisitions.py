from datetime import date, datetime
from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, RootModel, field_validator, model_validator


class Satellite(str, Enum):
    Landsat9 = "landsat_9"
    Landsat8 = "landsat_8"
    Landsat7 = "landsat_7"


class AcquisitionDetails(BaseModel):
    path: List[int]
    cycle: int

    @field_validator('path', mode='before')
    def parse_path(cls, value):
        if isinstance(value, str):
            return [int(x) for x in value.split(',')]
        return value


class SatelliteAcquisitions(RootModel):
    root: Dict[date, AcquisitionDetails]

    @model_validator(mode='before')
    def parse_dates(cls, values):
        parsed_values = {}
        for key, value in values.items():
            if isinstance(key, str):
                try:
                    parsed_key = datetime.strptime(key, '%m/%d/%Y').date()
                except ValueError:
                    raise ValueError(f"Invalid date format for key: {key}")
                parsed_values[parsed_key] = value
            else:
                parsed_values[key] = value
        return parsed_values


class AcquisitionsData(RootModel):
    root: Dict[Satellite, SatelliteAcquisitions]
