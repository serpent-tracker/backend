from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


# Shared properties
class WeightBase(BaseModel):
    weight: Optional[int] = None
    weight_date: Optional[date] = None


# Properties to receive on weight creation
class WeightCreate(WeightBase):
    weight: int
    weight_date: date
    snake_id: int


# Properties to receive on weight update
class WeightUpdate(WeightBase):
    pass


# Properties shared by models stored in DB
class WeightInDBBase(WeightBase):
    id: int
    weight: int
    weight_date: date
    snake_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Weight(WeightInDBBase):
    pass


# Properties properties stored in DB
class WeightInDB(WeightInDBBase):
    pass
