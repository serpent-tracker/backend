from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


# Shared properties
class ShedBase(BaseModel):
    complete: Optional[bool] = None
    pre_lay: Optional[bool] = None
    shed_date: Optional[date] = None


# Properties to receive on shed creation
class ShedCreate(ShedBase):
    complete: bool
    pre_lay: bool
    shed_date: date
    snake_id: int


# Properties to receive on shed update
class ShedUpdate(ShedBase):
    pass


# Properties shared by models stored in DB
class ShedInDBBase(ShedBase):
    id: int
    complete: bool
    pre_lay: bool
    shed_date: date
    snake_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Shed(ShedInDBBase):
    pass


# Properties properties stored in DB
class ShedInDB(ShedInDBBase):
    pass
