from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    latitude: float = Field(alias="lat", ge=-90, le=90)
    longitude: float = Field(alias="lon", ge=-180, le=180)

    def to_list(self):
        return [self.latitude, self.longitude]
