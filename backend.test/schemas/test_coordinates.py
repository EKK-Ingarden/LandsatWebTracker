import pytest
from backend.schemas.structures.coordinates import Coordinates
from pydantic import ValidationError


class TestCoordinates:
    def test_max_min_values(self):
        with pytest.raises(ValidationError):
            Coordinates(lat=1.0, lon=181.0)

        with pytest.raises(ValidationError):
            Coordinates(lat=-91.0, lon=1.0)
