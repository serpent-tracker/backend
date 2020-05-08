from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


# Shared properties
class ExcretionBase(BaseModel):
    urates: Optional[bool] = None
    feces: Optional[bool] = None
    notes: Optional[str] = None
    excretion_date: Optional[date] = None


# Properties to receive on excretion creation
class ExcretionCreate(ExcretionBase):
    urates: bool
    feces: bool
    notes: str
    excretion_date: date
    snake_id: int


# Properties to receive on excretion update
class ExcretionUpdate(ExcretionBase):
    pass


# Properties shared by models stored in DB
class ExcretionInDBBase(ExcretionBase):
    id: int
    urates: bool
    feces: bool
    excretion_date: date
    snake_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Excretion(ExcretionInDBBase):
    pass


# Properties properties stored in DB
class ExcretionInDB(ExcretionInDBBase):
    pass
