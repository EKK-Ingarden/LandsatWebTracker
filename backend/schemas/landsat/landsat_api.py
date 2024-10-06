import base64
import itertools
import json

import requests
from pydantic import BaseModel
from pystac import Item

from backend.schemas.enums.mosaic_type import MosaicType
from backend.schemas.landsat.landsat_item import Bands, LandsatItem, Mosaics
from backend.schemas.structures.wrs_coordinates import WrsCoordinates
from backend.settings import settings
from backend.utils.polygon_utils import polygon_from_nested_list


class LandsatAPI(BaseModel):
    base_url: str = settings.landsat_provider_url

    @staticmethod
    def landsat_mosaic_builder(scene_id: str, collection_id: str, mosaic_type: MosaicType):
        r_register = requests.post(
            "https://planetarycomputer.microsoft.com/api/data/v1/mosaic/register",
            json={"collections": ["landsat-c2-l2"], "ids": [scene_id]},
        )
        registered = r_register.json()
        tilejson_url = registered["links"][0]["href"]

        mosaic_info = requests.get(
            "https://planetarycomputer.microsoft.com/api/data/v1/mosaic/info",
            params=dict(collection=collection_id),
        ).json()

        render_config = mosaic_info["renderOptions"][int(mosaic_type.value)]

        def key(s):
            return s.split("=")[0]

        params = {
            k: [x.split("=")[1] for x in v] for k, v in itertools.groupby(render_config["options"].split("&"), key=key)
        }
        params["collection"] = collection_id

        return requests.get(tilejson_url, params=params).json()["tiles"][0]

    @staticmethod
    def bands_builder(item: Item) -> Bands:
        return Bands(**{key.replace(".", "_"): value.href for key, value in item.assets.items()})

    def mosaic_endpoint_builder(self, item: Item) -> Mosaics:
        decoded_results = base64.urlsafe_b64encode(json.dumps(self._result.get_parameters()).encode()).decode()
        return Mosaics(
            **{
                data.name.lower(): f"?collection_id={item.collection_id}"
                f"&results_param={decoded_results}"
                f"&mosaic_type={data.value}"
                for data in MosaicType
            }
        )

    def landsat_item_builder(self, item: Item) -> LandsatItem:
        return LandsatItem(
            platform=item.properties["platform"],
            mosaic_endpoints=self.mosaic_endpoint_builder(item),
            bands=self.bands_builder(item),
            id=item.id,
            datetime=item.datetime,
            eo_cloud_cover=item.properties["eo:cloud_cover"] / 100,
            wrs_coordinates=WrsCoordinates(
                path=item.properties["landsat:wrs_path"],
                row=item.properties["landsat:wrs_row"],
            ),
            rendered_preview=item.assets["rendered_preview"].href,
            polygon=polygon_from_nested_list(item.geometry["coordinates"]),
        )

    @property
    def pages(self):
        """
        Get the page from the ItemSearch object
        """
        return self._result.pages()

    @property
    def all_results(self):
        """
        returns results in LandsatItem class format
        """
        for item in self._result.items():
            yield self.landsat_item_builder(item)

    @property
    def first_result(self):
        """
        returns first result in LandsatItem class format
        """
        return self.landsat_item_builder(next(self._result.items()))
