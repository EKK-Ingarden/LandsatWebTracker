from datetime import datetime

import pytest
from backend.schemas.landsat.landsat_api_by_search import LandsatAPIBySearch
from backend.schemas.structures.coordinates import Coordinates
from pydantic import ValidationError


class TestLandsatAPI:
    def test_cloud_coverage_validation_error(self):
        # Arrange
        coordinates = Coordinates(lat=1.0, lon=1.0)
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 1)
        max_cloud_cover = 1.5

        # Act / Assert
        with pytest.raises(ValidationError):
            LandsatAPIBySearch(
                coordinates=coordinates, start_date=start_date, end_date=end_date, max_cloud_cover=max_cloud_cover
            )
