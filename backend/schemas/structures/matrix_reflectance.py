import numpy as np
from pydantic_core import Url

from backend.schemas.landsat.landsat_item_advanced import ReflectanceChartElement
from backend.schemas.structures.matrix import Matrix


class ReflectanceMatrix(Matrix):
    min_wave_length: float
    max_wave_length: float
    url: Url
    matrix: np.ndarray = None

    def to_reflectance_chart_element(self):
        return ReflectanceChartElement(reflectance=float(self.mean), wave_length=self.median_wave_length)

    @property
    def mean(self):
        return np.mean(self.matrix)

    @property
    def median_wave_length(self):
        return (self.min_wave_length + self.max_wave_length) / 2

    class Config:
        arbitrary_types_allowed = True
