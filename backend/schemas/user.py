from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True
