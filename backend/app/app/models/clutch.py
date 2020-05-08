from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .snake import Snake  # noqa: F401


class Clutch(Base):
    id = Column(Integer, primary_key=True, index=True)
    custom_id = Column(Integer, index=True)
    clutch_type = Column(String)
    laid_date = Column(DateTime)
    due_date = Column(DateTime)
    egg_count = Column(Integer)
    good_egg_count = Column(Integer)
    bad_egg_count = Column(Integer)
    snake_id = Column(Integer, ForeignKey("snake.id"))
    father_id = Column(Integer, ForeignKey("snake.id"))
    snake = relationship("Snake", foreign_keys=[snake_id], back_populates="clutches")
    father = relationship("Snake", foreign_keys=[father_id], back_populates="fathers")
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)