from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database import Base


class PixelWatch(Base):
    __tablename__ = "pixel_watches"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID,
                     ForeignKey('auth.users.id',
                                onupdate='CASCADE',
                                ondelete='CASCADE'),
                     nullable=False)
    user = relationship('User')
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False)
    path = Column(Integer, nullable=False)
    row = Column(Integer, nullable=False)
