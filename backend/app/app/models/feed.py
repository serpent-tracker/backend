from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .snake import Snake  # noqa: F401


class Feed(Base):
    id = Column(Integer, primary_key=True, index=True)
    prey = Column(String)
    prey_type = Column(String)
    prey_size = Column(String)
    feed_date = Column(DateTime)
    count = Column(Integer)
    snake_id = Column(Integer, ForeignKey("snake.id"))
    snake = relationship("Snake", back_populates="feeds")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)