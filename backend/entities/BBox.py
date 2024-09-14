from dataclasses import dataclass


@dataclass
class BBox:
    x_min: int
    y_min: int
    x_max: int
    y_max: int
