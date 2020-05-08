from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.mating import MatingCreate, MatingUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.tests.utils.snake import create_random_snake


def test_create_mating(db: Session) -> None:
    snake = create_random_snake(db)
    mate = create_random_snake(db)

    event = 'introduction'
    mate_id = mate.id
    event_date = "2020-04-20"

    mate_in = MatingCreate(
        event=event,
        snake_id=snake.id,
        mate_id=mate_id,
        event_date=event_date,
    )
    mating = crud.mating.create_with_snake(db=db, obj_in=mate_in)
    assert mating.event == event
    assert mating.mate_id == mate_id
    assert mating.event_date == datetime.strptime(event_date, '%Y-%m-%d')
    assert mating.snake_id == snake.id


def test_get_mating(db: Session) -> None:
    snake = create_random_snake(db)
    mate = create_random_snake(db)

    event = 'introduction'
    mate_id = mate.id
    event_date = "2020-04-20"

    mate_in = MatingCreate(
        event=event,
        snake_id=snake.id,
        mate_id=mate_id,
        event_date=event_date,
    )

    mating = crud.mating.create_with_snake(db=db, obj_in=mate_in)
    stored_mating = crud.mating.get(db=db, id=mating.id)
    assert mating
    assert mating.id == stored_mating.id
    assert mating.mate_id == stored_mating.mate_id
    assert mating.event_date == stored_mating.event_date
    assert mating.snake.id == stored_mating.snake.id


def test_update_mating(db: Session) -> None:
    snake = create_random_snake(db)
    mate = create_random_snake(db)

    event = 'introduction'
    mate_id = mate.id
    event_date = "2020-04-20"

    mate_in = MatingCreate(
        event=event,
        snake_id=snake.id,
        mate_id=mate_id,
        event_date=event_date,
    )
    mating = crud.mating.create_with_snake(db=db, obj_in=mate_in)
    
    event2 = 'breeding'
    mating_update = MatingUpdate(event=event2)
    mating2 = crud.mating.update(db=db, db_obj=mating, obj_in=mating_update)
    assert mating.id == mating2.id
    assert mating.event_date == mating2.event_date
    assert mating2.event == event2
    assert snake.id == mating2.snake.id
    assert mating.mate_id == mating2.mate_id


def test_delete_mating(db: Session) -> None:
    snake = create_random_snake(db)
    mate = create_random_snake(db)

    event = 'introduction'
    mate_id = mate.id
    event_date = "2020-04-20"

    mate_in = MatingCreate(
        event=event,
        snake_id=snake.id,
        mate_id=mate_id,
        event_date=event_date,
    )

    mating = crud.mating.create_with_snake(db=db, obj_in=mate_in)
    mating2 = crud.mating.remove(db=db, id=mating.id)
    mating3 = crud.mating.get(db=db, id=mating.id)
    assert mating3 is None
    assert mating2.id == mating.id
    assert mating2.event_date == datetime.strptime(event_date, '%Y-%m-%d')
    assert mating2.event == event
    assert mating2.snake.id == snake.id
    assert mating2.mate_id == mate.id
