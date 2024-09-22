from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: UUID
    email: Optional[EmailStr]

    class Config:
        from_attributes = True


class User(UserBase):
    encrypted_password: str
    role: str
    raw_app_meta_data: Optional[dict]
    raw_user_meta_data: Optional[dict]
    is_anonymous: bool

    class Config:
        from_attributes = True
