from dataclasses import dataclass


@dataclass
class BorderBox:
    x_min: int
    y_min: int
    x_max: int
    y_max: int
