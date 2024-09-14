from datetime import datetime
from types import bbox_type


class WRS2Tools:
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
    def get_available_scenes(bbox: bbox_type, start_date: datetime, end_date: datetime):
        """
        Get available scenes for a given bounding box and date range.
        """
        raise NotImplementedError
