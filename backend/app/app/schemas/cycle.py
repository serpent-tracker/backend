from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


class CycleEnum(str, Enum):
    follicles = 'follicles'
    ovulation = 'ovulation'


# Shared properties
class CycleBase(BaseModel):
    cycle_type: Optional[CycleEnum] = None
    cycle_date: Optional[date] = None
    notes: Optional[str] = None


# Properties to receive on cycle creation
class CycleCreate(CycleBase):
    cycle_type: CycleEnum
    cycle_date: Optional[date] = None
    notes: Optional[str] = None
    snake_id: int


# Properties to receive on cycle update
class CycleUpdate(CycleBase):
    pass


# Properties shared by models stored in DB
class CycleInDBBase(CycleBase):
    id: int
    cycle_type: CycleEnum
    cycle_date: date
    notes: str
    snake_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Cycle(CycleInDBBase):
    pass


# Properties properties stored in DB
class CycleInDB(CycleInDBBase):
    pass
