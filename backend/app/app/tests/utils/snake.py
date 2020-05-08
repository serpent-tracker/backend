from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.snake import SnakeCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_snake(db: Session, *, owner_id: Optional[int] = None) -> models.Snake:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    name = random_lower_string()
    description = random_lower_string()
    hatch_date = '2020-04-20'
    sex = "male"
    produced_by = "Breeder ABC"
    snake_in = SnakeCreate(
        name=name,
        description=description,
        id=id,
        hatch_date=hatch_date,
        sex=sex,
        produced_by=produced_by,
    )
    return crud.snake.create_with_owner(db=db, obj_in=snake_in, owner_id=owner_id)
