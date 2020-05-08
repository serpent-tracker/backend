from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .snake import Snake  # noqa: F401


class Excretion(Base):
    id = Column(Integer, primary_key=True, index=True)
    urates = Column(Boolean)
    feces = Column(Boolean)
    notes = Column(String)
    excretion_date = Column(DateTime)
    snake_id = Column(Integer, ForeignKey("snake.id"))
    snake = relationship("Snake", back_populates="excretions")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)