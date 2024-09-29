from enum import Enum


class Satellite(str, Enum):
    Landsat9 = "landsat_9"
    Landsat8 = "landsat_8"
    Landsat7 = "landsat_7"
