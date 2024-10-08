from pydantic import AliasChoices, BaseModel, Field


class Coordinates(BaseModel):
    latitude: float = Field(..., validation_alias=AliasChoices("lat", "latitude"), ge=-90, le=90)
    longitude: float = Field(..., validation_alias=AliasChoices("lon", "longitude"), ge=-180, le=180)

    def to_list(self):
        return [self.latitude, self.longitude]
