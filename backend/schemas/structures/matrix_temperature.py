import collections

import numpy as np

from backend.schemas.landsat.landsat_item_advanced import TemperatureChartElement
from backend.schemas.structures.matrix import Matrix


class TemperatureMatrix(Matrix):
    def to_temperature_chart_element(self):
        count_collection = collections.Counter(self.matrix)

        keys = np.array(list(count_collection.keys()), dtype=float)
        values = np.array(list(count_collection.values()))

        rounded_keys = np.round(keys)

        unique_keys = np.unique(rounded_keys)
        sums = {key: values[rounded_keys == key].sum() for key in unique_keys}

        return [
            TemperatureChartElement(temperature=temperature, distribution=distribution)
            for temperature, distribution in sums.items()
        ]
