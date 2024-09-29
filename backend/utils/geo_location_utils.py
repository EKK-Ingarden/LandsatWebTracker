from datetime import datetime
from typing import Optional

import httpx

from backend.schemas import TileAttributes, WrsCoordinates
from backend.schemas.structures.border_box import BorderBox
from backend.schemas.structures.tile_attributes import Mode
from backend.utils.polygon_utils import polygon_from_nested_list


class WRS2Utils:
    """
    class for WRS2 geolocation utilities.

    The Worldwide Reference System 2 (WRS-2) is a global system used to catalog and organize satellite images,
    It divides the Earth's surface into a grid of path/row coordinates.

    Path: Refers to the satellite's orbit, with each path representing a specific line or track the satellite
    follows as it passes over the Earth.
    Row: Represents divisions along the satellite’s track (north to south), indicating different portions of the Earth's
    surface along that path.

    """

    @staticmethod
    def get_wrs2_path(row, path):
        """
        Get the WRS-2 path number for a given row and path.
        """
        raise NotImplementedError

    @staticmethod
    async def get_wrs2_tiles(lat: float, lng: float, mode: Optional[Mode] = None):
        """
        Get the WRS-2 tile for a given latitude and longitude.
        """
        tiles = []

        url = "https://nimbus.cr.usgs.gov/arcgis/rest/services/LLook_Outlines/MapServer/1/query"

        params = {
            "geometry": f"{lng}, {lat}",
            "geometryType": "esriGeometryPoint",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "*",
            "f": "json",
        }

        if mode is not None:
            params["where"] = f"MODE='{mode}'"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            data = response.json()["features"]

            for tile in data:
                attributes = tile["attributes"]
                tiles.append(TileAttributes(
                    coordinates=WrsCoordinates(
                        path=attributes["PATH"],
                        row=attributes["ROW"]
                    ),
                    mode=attributes["MODE"],
                    polygon=polygon_from_nested_list(tile["geometry"]["rings"]),
                ))
        return tiles

    @staticmethod
    def get_available_scenes(bbox: BorderBox, start_date: datetime, end_date: datetime):
        """
        Get available scenes for a given bounding box and date range.
        """
        raise NotImplementedError
