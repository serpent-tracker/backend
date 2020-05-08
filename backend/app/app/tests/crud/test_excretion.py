from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.excretion import ExcretionCreate, ExcretionUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.tests.utils.snake import create_random_snake


def test_create_excretion(db: Session) -> None:
    urates = False
    feces = False
    notes = "test note"
    excretion_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    excretion_in = ExcretionCreate(
        urates=urates,
        feces=feces,
        notes=notes,
        excretion_date=excretion_date,
        snake_id=snake.id
    )
    excretion = crud.excretion.create_with_snake(db=db, obj_in=excretion_in)
    assert excretion.urates == urates
    assert excretion.feces == feces
    assert excretion.excretion_date == datetime.strptime(excretion_date, '%Y-%m-%d')
    assert excretion.snake_id == snake.id


def test_get_excretion(db: Session) -> None:
    urates = False
    feces = False
    notes = "test note"
    excretion_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    excretion_in = ExcretionCreate(
        urates=urates,
        feces=feces,
        notes=notes,
        excretion_date=excretion_date,
        snake_id=snake.id
    )
    excretion = crud.excretion.create_with_snake(db=db, obj_in=excretion_in)
    stored_excretion = crud.excretion.get(db=db, id=excretion.id)
    assert excretion
    assert excretion.id == stored_excretion.id
    assert excretion.urates == stored_excretion.urates
    assert excretion.feces == stored_excretion.feces
    assert excretion.notes == stored_excretion.notes
    assert excretion.excretion_date == stored_excretion.excretion_date
    assert excretion.snake.id == stored_excretion.snake.id


def test_update_shed(db: Session) -> None:
    urates = False
    feces = False
    notes = "test note"
    excretion_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    excretion_in = ExcretionCreate(
        urates=urates,
        feces=feces,
        notes=notes,
        excretion_date=excretion_date,
        snake_id=snake.id
    )
    excretion = crud.excretion.create_with_snake(db=db, obj_in=excretion_in)
    
    urates2 = True
    excretion_update = ExcretionUpdate(urates=urates2)
    excretion2 = crud.excretion.update(db=db, db_obj=excretion, obj_in=excretion_update)
    assert excretion.id == excretion2.id
    assert excretion.excretion_date == excretion2.excretion_date
    assert excretion2.urates == urates2
    assert excretion.snake.id == excretion2.snake.id


def test_delete_shed(db: Session) -> None:
    urates = False
    feces = False
    notes = "test note"
    excretion_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    excretion_in = ExcretionCreate(
        urates=urates,
        feces=feces,
        notes=notes,
        excretion_date=excretion_date,
        snake_id=snake.id
    )
    excretion = crud.excretion.create_with_snake(db=db, obj_in=excretion_in)
    excretion2 = crud.excretion.remove(db=db, id=excretion.id)
    excretion3 = crud.excretion.get(db=db, id=excretion.id)
    assert excretion3 is None
    assert excretion2.id == excretion.id
    assert excretion2.excretion_date == datetime.strptime(excretion_date, '%Y-%m-%d')
    assert excretion2.urates == urates
    assert excretion2.feces == feces
    assert excretion2.notes == notes
    assert excretion2.snake.id == snake.id
