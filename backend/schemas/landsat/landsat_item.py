from datetime import datetime

from pydantic import BaseModel
from pydantic_core import Url

from backend.schemas.structures.cloud_coverage_ratio import CloudCoverageRatio
from backend.schemas.structures.polygon import Polygon
from backend.schemas.structures.wrs_coordinates import WrsCoordinates


class Bands(BaseModel):
    qa: Url
    ang: Url
    red: Url
    blue: Url
    drad: Url
    emis: Url
    emsd: Url
    trad: Url
    urad: Url
    atran: Url
    cdist: Url
    green: Url
    nir08: Url
    lwir11: Url
    swir16: Url
    swir22: Url
    coastal: Url
    mtl_txt: Url
    mtl_xml: Url
    mtl_json: Url
    qa_pixel: Url
    qa_radsat: Url
    qa_aerosol: Url
    tilejson: Url
    rendered_preview: Url


class Mosaics(BaseModel):
    natural_color: str
    color_infrared: str
    shortwave_infrared: str
    agriculture: str
    vegetation: str
    moisture_index: str
    atmospheric_penetration: str


class LandsatItem(BaseModel):
    platform: str
    id: str
    datetime: datetime
    eo_cloud_cover: CloudCoverageRatio
    wrs_coordinates: WrsCoordinates
    rendered_preview: str
    mosaic_endpoints: Mosaics
    polygon: Polygon
    bands: Bands
