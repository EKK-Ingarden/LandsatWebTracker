import numpy as np
import requests
from PIL import Image
from pydantic import BaseModel
from pydantic_core import Url


class Matrix(BaseModel):
    url: Url
    add_transformation: float
    multiply_transformation: float
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
        self.matrix = self.matrix * self.multiply_transformation + self.add_transformation

    class Config:
        arbitrary_types_allowed = True
