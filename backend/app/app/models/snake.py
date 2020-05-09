from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Snake(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    common_name = Column(String)
    scientific_name = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="snakes")
    cycles = relationship("Cycle", back_populates="snake")
    weights = relationship("Weight", back_populates="snake")
    sheds = relationship("Shed", back_populates="snake")
    clutches = relationship("Clutch", back_populates="snake", foreign_keys="Clutch.snake_id")
    fathers = relationship("Clutch", back_populates="snake", foreign_keys="Clutch.father_id")
    matings = relationship("Mating", back_populates="snake", foreign_keys="Mating.snake_id")
    mates = relationship("Mating", back_populates="snake", foreign_keys="Mating.mate_id")
    feeds = relationship("Feed", back_populates="snake")
    excretions = relationship("Excretion", back_populates="snake")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    hatch_date = Column(DateTime)
    sex = Column(String)
    produced_by = Column(String)
    visual_genes = Column(ARRAY(String))
    het_genes = Column(ARRAY(String))
    imageurl = Column(String)