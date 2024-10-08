from typing import List

import structlog
from pystac import Item

from backend.schemas.landsat.landsat_item_advanced import TemperatureChartElement
from backend.schemas.structures.matrix_temperature import TemperatureMatrix


def generate_temperature_chart_from_item(item: Item) -> List[TemperatureChartElement]:
    structlog.get_logger().debug(f"Generating temperature chart from {item}")
    return TemperatureMatrix(
        url=item.assets["lwir11"].href, add_transformation=149.0 - 272.15, multiply_transformation=0.00341802
    ).to_temperature_chart_element()
