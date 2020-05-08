from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


class EventEnum(str, Enum):
    intro = 'introduction'
    courting = 'courting'
    breeding = 'breeding'
    seperated = 'seperated'


# Shared properties
class MatingBase(BaseModel):
    event: Optional[EventEnum] = None
    event_date: Optional[date] = None


# Properties to receive on mating creation
class MatingCreate(MatingBase):
    event: EventEnum
    event_date: Optional[date] = None
    snake_id: int
    mate_id: int


# Properties to receive on mating update
class MatingUpdate(MatingBase):
    pass


# Properties shared by models stored in DB
class MatingInDBBase(MatingBase):
    id: int
    event: EventEnum
    event_date: date
    snake_id: int
    mate_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Mating(MatingInDBBase):
    pass


# Properties properties stored in DB
class MatingInDB(MatingInDBBase):
    pass
