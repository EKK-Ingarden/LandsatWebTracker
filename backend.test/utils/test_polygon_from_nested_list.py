from backend.schemas import Coordinates, Polygon
from backend.utils.polygon_utils import polygon_from_nested_list


class TestPolygonUtils:
    def test_polygon_from_nested_list(self):
        polygon = polygon_from_nested_list([[[1, 2], [3, 4], [5, 6]]])
        assert polygon == Polygon(
            coordinates=[
                Coordinates(lat=1, lon=2),
                Coordinates(lat=3, lon=4),
                Coordinates(lat=5, lon=6),
            ]
        )
