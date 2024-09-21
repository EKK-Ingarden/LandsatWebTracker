from typing import List

from pydantic import BaseModel

from backend.schemas.structures.coordinates import Coordinates


class Polygon(BaseModel):
    coordinates: List[Coordinates]

    def to_list(self):
        return [coord.to_list() for coord in self.coordinates]
