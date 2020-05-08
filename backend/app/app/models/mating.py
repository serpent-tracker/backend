from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .snake import Snake  # noqa: F401


class Mating(Base):
    id = Column(Integer, primary_key=True, index=True)
    event = Column(String)
    event_date = Column(DateTime)
    snake_id = Column(Integer, ForeignKey("snake.id"))
    mate_id = Column(Integer, ForeignKey("snake.id"))
    snake = relationship("Snake", foreign_keys=[snake_id], back_populates="matings")
    mate = relationship("Snake", foreign_keys=[mate_id], back_populates="mates")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)