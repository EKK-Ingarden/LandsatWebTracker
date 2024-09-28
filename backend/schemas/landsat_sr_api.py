import json
from typing import List

import requests
from fastapi import HTTPException
from pydantic import BaseModel

from backend.schemas.structures.download_options import AvailableBandMetadata, DownloadOptions, SecondaryDownload
from backend.schemas.structures.download_request import BandReadyToDownload
from backend.settings import settings


class DownloadOptionsFilter:
    @staticmethod
    def RGB_ONLY(secondary_download: SecondaryDownload):
        return secondary_download.entityId[-6:] in ("B2_TIF", "B3_TIF", "B4_TIF")

    @staticmethod
    def ALL(secondary_download: SecondaryDownload):
        return True

class LandsatSRAPI(BaseModel):
    scene_id: str
    base_url: str = "https://m2m.cr.usgs.gov/api/api/json/stable/"
    dataset_name: str = "landsat_ot_c2_l2"
    _api_key: str = None

    def __init__(self, **data):
        super().__init__(**data)
        self._api_key = self._login_token()

    def _send_request(self, path, data, api_key):
        url = self.base_url + path
        json_data = json.dumps(data)

        if api_key is None:
            response = requests.post(url, json_data)
        else:
            headers = {'X-Auth-Token': api_key}
            response = requests.post(url, json_data, headers=headers)

        try:
            httpStatusCode = response.status_code
            if response is None:
                raise HTTPException(status_code=500, detail="No output from earth explorer service")

            output = json.loads(response.text)
            if output['errorCode'] is not None:
                raise HTTPException(status_code=500, detail=output['errorMessage'])

            if httpStatusCode == 404:
                raise HTTPException(status_code=404, detail="404 Not Found")

            if httpStatusCode == 401:
                raise HTTPException(status_code=401, detail="401 Unauthorized")

            if httpStatusCode == 400:
                raise HTTPException(status_code=400, detail="400 Bad Request")

        except Exception as e:
            response.close()
            raise HTTPException(status_code=500, detail=str(e))

        response.close()
        return output['data']

    def _login_token(self):
        path = "login-token"
        payload = {
            "username": "wikipop",
            "token": settings.usgs_m2m_api_key
        }

        return self._send_request(path, payload, None)

    def _download_options(self, data_filter = DownloadOptionsFilter.ALL) -> List[AvailableBandMetadata]:

        path = "download-options"
        payload = {
            "datasetName": self.dataset_name,
            "entityIds": self.scene_id
        }

        data = DownloadOptions.model_validate(
            # This api returns few versions of one scene not sure why, for our purposes we only need the first one
            self._send_request(path, payload, self._api_key)[0]
        )

        print(data)

        availible_entity_metadata: List[AvailableBandMetadata] = []

        for secondary_download in data.secondaryDownloads:
            if secondary_download.available and data_filter(secondary_download):
                availible_entity_metadata.append(
                    AvailableBandMetadata(productId=secondary_download.id, entityId=secondary_download.entityId)
                )

        return availible_entity_metadata

    def _download_request(self, download_list: List[AvailableBandMetadata]) -> List[BandReadyToDownload]:
        path = "download-request"
        payload = {
            "downloads": [item.to_dict() for item in download_list]
        }

        data = self._send_request(path, payload, self._api_key)
        available_downloads: List[BandReadyToDownload] = []

        for download in data["availableDownloads"]:
            available_downloads.append(BandReadyToDownload.model_validate(download))

        return available_downloads

    @property
    def all_bands(self):
        download_options = self._download_options(data_filter=DownloadOptionsFilter.ALL)
        download_request = self._download_request(download_options)

        for band in download_request:
            yield band

    @property
    def rgb_bands(self):
        download_options = self._download_options(data_filter=DownloadOptionsFilter.RGB_ONLY)
        download_request = self._download_request(download_options)

        for band in download_request:
            yield band
