from sqlalchemy import Boolean, Column, DateTime, String, text

from backend.database import Base


class Report(Base):
    __tablename__ = "reports"

    scene_id = Column(String, primary_key=True)
    is_processed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    raw_data = Column(String, nullable=True)
