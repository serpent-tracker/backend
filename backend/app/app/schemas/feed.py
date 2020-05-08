from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


class PreyEnum(str, Enum):
    asf = 'african soft fur'
    mouse = 'mouse'
    rat = 'rat'
    rabbit = 'rabbit'
    chick = 'chick'


class PreyTypeEnum(str, Enum):
    frozen = 'ft'
    live = 'live'
    prekill = 'prekill'


class PreySizeEnum(str, Enum):
    pinky = 'pinky'
    crawler = 'crawler'
    pup = 'pup'
    fuzzy = 'fuzzy'
    weaned = 'weaned'
    hopper = 'hopper'
    small = 'small'
    medium = 'medium'
    large = 'large'
    xl = 'xl'
    jumbo = 'jumbo'

# Shared properties
class FeedBase(BaseModel):
    prey: Optional[PreyEnum] = None
    prey_type: Optional[PreyTypeEnum] = None
    prey_size: Optional[PreySizeEnum] = None
    feed_date: Optional[date] = None
    count: Optional[int] = None


# Properties to receive on feed creation
class FeedCreate(FeedBase):
    prey: PreyEnum
    prey_type: PreyTypeEnum
    prey_size: PreySizeEnum
    feed_date: Optional[date] = None
    count: Optional[int] = None
    snake_id: int


# Properties to receive on feed update
class FeedUpdate(FeedBase):
    pass


# Properties shared by models stored in DB
class FeedInDBBase(FeedBase):
    id: int
    prey: PreyEnum
    prey_type: PreyTypeEnum
    prey_size: PreySizeEnum
    count: int
    feed_date: date
    snake_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Feed(FeedInDBBase):
    pass


# Properties properties stored in DB
class FeedInDB(FeedInDBBase):
    pass
