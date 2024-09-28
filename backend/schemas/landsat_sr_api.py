import json

import requests
from fastapi import HTTPException
from pydantic import BaseModel

from backend.schemas.structures.download_options import DownloadOptions
from backend.settings import settings


class LandsatSRAPI(BaseModel):
    scene_id: str
    base_url: str = "https://m2m.cr.usgs.gov/api/api/json/stable/"
    dataset_name: str = "landsat_ot_c2_l2"
    api_key: str = None

    def __init__(self, **data):
        super().__init__(**data)
        self.api_key = self._login_token()

        print(self._get_download_options())

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

    def _get_download_options(self):
        path = "download-options"
        payload = {
            "datasetName": self.dataset_name,
            "entityIds": self.scene_id
        }

        data = self._send_request(path, payload, self.api_key)

        json.dump(data, open("dwnld-options-2.json", "w"))

        data = DownloadOptions.model_validate(data[0])

        return data
