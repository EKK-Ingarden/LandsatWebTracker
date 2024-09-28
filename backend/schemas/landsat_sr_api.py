import json

import requests
from fastapi import HTTPException
from pydantic import BaseModel

from backend.settings import settings


class LandsatSRAPI(BaseModel):
    scene_id: str
    base_url: str = "https://m2m.cr.usgs.gov/api/api/json/stable/"
    dataset_name: str = "landsat_ot_c2_l2"

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
