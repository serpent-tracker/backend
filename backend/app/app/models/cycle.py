from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .snake import Snake  # noqa: F401


class Cycle(Base):
    id = Column(Integer, primary_key=True, index=True)
    cycle_type = Column(String)
    notes = Column(String)
    cycle_date = Column(DateTime)
    snake_id = Column(Integer, ForeignKey("snake.id"))
    snake = relationship("Snake", back_populates="cycles")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)