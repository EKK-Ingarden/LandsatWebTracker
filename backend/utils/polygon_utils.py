from backend.schemas.structures.coordinates import Coordinates
from backend.schemas.structures.polygon import Polygon


def polygon_from_nested_list(nested_data: list[list[list[float]]]) -> Polygon:
    data = nested_data[0]
    return Polygon(coordinates=[Coordinates(lat=coord[1], lon=coord[0]) for coord in data])
