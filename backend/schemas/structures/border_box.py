from pydantic import BaseModel


class BorderBox(BaseModel):
    x_min: float
    y_min: float
    x_max: float
    y_max: float
