from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


class ClutchTypeEnum(str, Enum):
    egg = 'egg'
    live_born = 'live born'
    slugs = 'slugs'
    still_born = 'still born'


# Shared properties
class ClutchBase(BaseModel):
    clutch_type: ClutchTypeEnum = None
    laid_date: date
    due_date: Optional[date] = None
    notes: str = ''
    egg_count: int = None
    good_egg_count: int = None
    bad_egg_count: int = None
    custom_id: Optional[int] = None


# Properties to receive on clutch creation
class ClutchCreate(ClutchBase):
    clutch_type: ClutchTypeEnum
    due_date: Optional[date] = None
    laid_date: date
    egg_count: int
    good_egg_count: int
    bad_egg_count: int
    snake_id: int
    father_id: int
    notes: Optional[str] = ''
    custom_id: Optional[int] = None


# Properties to receive on clutch update
class ClutchUpdate(ClutchBase):
    laid_date: Optional[date] = None
    


# Properties shared by models stored in DB
class ClutchInDBBase(ClutchBase):
    id: int
    clutch_type: ClutchTypeEnum
    laid_date: date
    due_date: Optional[date] = None
    egg_count: int
    good_egg_count: int
    bad_egg_count: int
    notes: str
    snake_id: int
    father_id: int
    custom_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Clutch(ClutchInDBBase):
    pass


# Properties properties stored in DB
class ClutchInDB(ClutchInDBBase):
    pass
