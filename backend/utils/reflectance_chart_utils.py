from typing import List

import structlog

from backend.schemas.landsat.landsat_item import Bands
from backend.schemas.landsat.landsat_item_advanced import ReflectanceChartElement
from backend.schemas.structures.matrix_reflectance import ReflectanceMatrix

"""
Source of the constans: https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites

Band 1 - Coastal aerosol	            0.43-0.45
Band 2 - Blue	                        0.45-0.51
Band 3 - Green	                        0.53-0.59
Band 4 - Red	                        0.64-0.67
Band 5 - Near Infrared (NIR)	        0.85-0.88
Band 6 - Shortwave Infrared (SWIR) 1	1.57-1.65
Band 7 - Shortwave Infrared (SWIR) 2	2.11-2.29
Band 8 - Panchromatic	                0.50-0.68
Band 9 - Cirrus	                        1.36-1.38
Band 10 - Thermal Infrared (TIRS) 1	    10.6-11.19
Band 11 - Thermal Infrared (TIRS) 2	    11.50-12.51
"""

BANDS_WAVE_LENGTHS = {
    "costal": (0.43, 0.45),
    "blue": (0.45, 0.51),
    "green": (0.53, 0.59),
    "red": (0.64, 0.67),
    "nir08": (0.85, 0.88),
    "swir16": (1.57, 1.65),
    "swir22": (2.11, 2.29),
    # TODO: Data is incomplete some1 must fill it, for now we will use only those bands
}


def generate_reflectance_chart_from_tiff(bands: Bands) -> List[ReflectanceChartElement]:
    structlog.get_logger().debug(f"Generating reflectance chart from {bands}")
    """
    Generate the reflectance chart from the bands
    """
    return [
        ReflectanceMatrix(
            min_wave_length=BANDS_WAVE_LENGTHS[name][0],
            max_wave_length=BANDS_WAVE_LENGTHS[name][1],
            url=url,
            add_transformation=-0.2,
            multiply_transformation=2.75e-05,
        ).to_reflectance_chart_element()
        for name, url in bands.model_dump().items()
        if name in BANDS_WAVE_LENGTHS
    ]
