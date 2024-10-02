from sqlalchemy import JSON, UUID, Boolean, Column, String, text

from backend.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id = Column(UUID, server_default=text("auth.gen_random_uuid()"), primary_key=True)
    email = Column(String, unique=True)
    encrypted_password = Column(String)
    role = Column(String, nullable=False)
    raw_app_meta_data = Column(JSON)
    raw_user_meta_data = Column(JSON)
    is_anonymous = Column(Boolean, nullable=False, default=True)
