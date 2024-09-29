from datetime import date
from typing import List, Optional

import httpx

from backend.schemas import AcquisitionDetails, AcquisitionsData, Satellite


class AcquisitionsUtils:
    def __init__(self):
        self.acquisitions_data = None

    async def load_acquisitions(self):
        url = "https://landsat.usgs.gov/sites/default/files/landsat_acq/assets/json/cycles_full.json"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            acquisitions = response.json()

        self.acquisitions_data = AcquisitionsData.parse_obj(acquisitions)

    def get_next_acquisition(self, path: int) -> Optional[tuple[str, date, AcquisitionDetails]]:
        acquisitions = self.get_acquisitions(path, date.today())
        return acquisitions[0] if acquisitions else None

    def get_acquisitions(self,
                         path: int,
                         from_date: date,
                         to_date: Optional[date] = None,
                         satellites: Optional[List[Satellite]] = None) -> List[tuple[str, date, AcquisitionDetails]]:
        if not self.acquisitions_data:
            raise ValueError("Acquisitions data is not loaded")

        acquisitions = []

        for satellite, satellite_acquisitions in self.acquisitions_data.root.items():
            for acquisition_date, details in satellite_acquisitions.root.items():
                if acquisition_date <= from_date:
                    continue
                if to_date is not None and acquisition_date > to_date:
                    continue
                if satellites is not None and satellite not in satellites:
                    continue
                if path not in details.path:
                    continue

                acquisitions.append((satellite, acquisition_date, details))

        acquisitions.sort(key=lambda x: x[1])

        return acquisitions

