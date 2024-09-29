from enum import Enum


class MosaicType(Enum):
    NATURAL_COLOR = "0"
    COLOR_INFRARED = "1"
    SHORTWAVE_INFRARED = "2"
    AGRICULTURE = "3"
    VEGETATION = "4"
    MOISTURE_INDEX = "5"
    ATMOSPHERIC_PENETRATION = "6"
