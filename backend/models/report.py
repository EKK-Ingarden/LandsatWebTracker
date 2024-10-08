from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, String, text
from sqlalchemy.orm import relationship

from backend.database import Base


class Report(Base):
    __tablename__ = "reports"

    scene_id = Column(String, primary_key=True)
    user_id = Column(UUID, ForeignKey("auth.users.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    user = relationship("User")
    is_processed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))
    raw_data = Column(String, nullable=True)
