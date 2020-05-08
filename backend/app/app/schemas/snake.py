from typing import Optional
from datetime import date
from datetime import datetime

from enum import Enum

from pydantic import BaseModel


class SexEnum(str, Enum):
    male = 'male'
    female = 'female'
    unknown = 'unknown'

# Shared properties
class SnakeBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    common_name: Optional[str] = None
    scientific_name: Optional[str] = None
    hatch_date: Optional[date] = None
    sex: Optional[SexEnum] = SexEnum.unknown
    produced_by: Optional[str] = None
    visual_genes: Optional[list] = None
    het_genes: Optional[list] = None


# Properties to receive on snake creation
class SnakeCreate(SnakeBase):
    name: str


# Properties to receive on snake update
class SnakeUpdate(SnakeBase):
    pass


# Properties shared by models stored in DB
class SnakeInDBBase(SnakeBase):
    id: int
    name: str
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Snake(SnakeInDBBase):
    pass


# Properties properties stored in DB
class SnakeInDB(SnakeInDBBase):
    pass
