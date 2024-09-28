from pydantic import BaseModel


class LandsatSRAPI(BaseModel):
    scene_id: str
