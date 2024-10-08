from pydantic import AliasChoices, BaseModel, Field


class WrsCoordinates(BaseModel):
    wrs_path: int = Field(..., validation_alias=AliasChoices("path", "wrs_path"), ge=1, le=233)
    wrs_row: int = Field(..., validation_alias=AliasChoices("row", "wrs_row"), ge=1, le=248)
