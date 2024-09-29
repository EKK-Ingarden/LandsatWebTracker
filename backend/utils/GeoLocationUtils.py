from datetime import datetime

from backend.schemas import BorderBox


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
    def get_wrs2_tile(lat, lon):
        """
        Get the WRS-2 tile for a given latitude and longitude.
        """
        raise NotImplementedError

    @staticmethod
    def get_available_scenes(bbox: BorderBox, start_date: datetime, end_date: datetime):
        """
        Get available scenes for a given bounding box and date range.
        """
        raise NotImplementedError
