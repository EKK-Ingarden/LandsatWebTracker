import numpy as np
import requests
from PIL import Image
from pydantic import BaseModel
from pydantic_core import Url

from backend.schemas.landsat.landsat_item_advanced import ReflectanceChartElement


class ReflectanceMatrix(BaseModel):
    min_wave_length: float
    max_wave_length: float
    url: Url
    matrix: np.ndarray = None

    def __init__(self, /, **data):
        super().__init__(**data)
        self.matrix = np.array(Image.open(self.data_downloader())).flatten()
        self.clean_zeros()
        self.apply_transformations()

    def data_downloader(self):
        response = requests.get(self.url.unicode_string(), stream=True)
        response.raise_for_status()
        return response.raw

    def clean_zeros(self):
        """
        No data is represented by 0, so we remove it
        """
        self.matrix = self.matrix[self.matrix > 0]

    def apply_transformations(self):
        """
        Apply the transformation to the matrix.
        Constans are based on the reflectance matrix documentation and mtl files of the bands
        """
        self.matrix = self.matrix * 0.0000275 - 0.2

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
