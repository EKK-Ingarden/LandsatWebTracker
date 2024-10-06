from pydantic import BaseModel, Field


class WrsCoordinates(BaseModel):
    wrs_path: int = Field(..., alias="path", ge=1, le=233)
    wrs_row: int = Field(..., alias="row", ge=1, le=248)
