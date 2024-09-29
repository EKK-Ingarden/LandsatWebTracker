import planetary_computer
from pystac_client import Client

from backend.schemas.landsat.landsat_api import LandsatAPI


class LandsatAPIById(LandsatAPI):
    scene_id: str

    def __init__(self, **data):
        super().__init__(**data)
        self._catalog = Client.open(self.base_url, modifier=planetary_computer.sign_inplace)
        self._result = self._catalog.search(
            collections=["landsat-c2-l2"],
            ids=[self.scene_id],
        )
