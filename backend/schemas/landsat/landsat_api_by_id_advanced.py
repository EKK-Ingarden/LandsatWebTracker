from pystac import Item

from backend.schemas import WrsCoordinates
from backend.schemas.landsat.landsat_api_by_id import LandsatAPIById
from backend.schemas.landsat.landsat_item import LandsatItem
from backend.schemas.landsat.landsat_item_advanced import LandsatAdvancedItem
from backend.utils.polygon_utils import polygon_from_nested_list
from backend.utils.reflectance_chart_utils import generate_reflectance_chart_from_tiff
from backend.utils.temperature_chart_utils import generate_temperature_chart_from_item


class LandsatAdvancedAPIById(LandsatAPIById):
    def __init__(self, **data):
        super().__init__(**data)

    def landsat_item_builder(self, item: Item) -> LandsatItem:
        return LandsatAdvancedItem(
            platform=item.properties["platform"],
            mosaic_endpoints=self.mosaic_endpoint_builder(item),
            bands=(bands := self.bands_builder(item)),
            id=item.id,
            datetime=item.datetime,
            eo_cloud_cover=item.properties["eo:cloud_cover"] / 100,
            wrs_coordinates=WrsCoordinates(
                path=item.properties["landsat:wrs_path"],
                row=item.properties["landsat:wrs_row"],
            ),
            rendered_preview=item.assets["rendered_preview"].href,
            polygon=polygon_from_nested_list(item.geometry["coordinates"]),
            temperature_chart=generate_temperature_chart_from_item(item),
            reflectance_chart=generate_reflectance_chart_from_tiff(bands),
        )
