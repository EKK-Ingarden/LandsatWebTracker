from backend.schemas import Coordinates, Polygon
from backend.utils.polygon_utils import polygon_from_nested_list


class TestPolygonUtils:
    def test_polygon_from_nested_list(self):
        polygon = polygon_from_nested_list([[[1, 2], [3, 4], [5, 6]]])
        assert polygon == Polygon(
            coordinates=[
                Coordinates(lat=2, lon=1),
                Coordinates(lat=4, lon=3),
                Coordinates(lat=6, lon=5),
            ]
        )
