from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.cycle import CycleCreate, CycleUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.tests.utils.snake import create_random_snake


def test_create_cycle(db: Session) -> None:
    snake = create_random_snake(db)

    cycle_type = 'follicles'
    notes = ""
    cycle_date = "2020-04-20"

    cycle_in = CycleCreate(
        cycle_type=cycle_type,
        notes=notes,
        snake_id=snake.id,
        cycle_date=cycle_date,
    )
    cycle = crud.cycle.create_with_snake(db=db, obj_in=cycle_in)
    assert cycle.cycle_type == cycle_type
    assert cycle.notes == notes
    assert cycle.cycle_date == datetime.strptime(cycle_date, '%Y-%m-%d')
    assert cycle.snake_id == snake.id


def test_get_cycle(db: Session) -> None:
    snake = create_random_snake(db)

    cycle_type = 'follicles'
    notes = ""
    cycle_date = "2020-04-20"

    cycle_in = CycleCreate(
        cycle_type=cycle_type,
        notes=notes,
        snake_id=snake.id,
        cycle_date=cycle_date,
    )
    cycle = crud.cycle.create_with_snake(db=db, obj_in=cycle_in)
    stored_cycle = crud.cycle.get(db=db, id=cycle.id)
    assert cycle
    assert cycle.id == stored_cycle.id
    assert cycle.cycle_type == stored_cycle.cycle_type
    assert cycle.notes == stored_cycle.notes
    assert cycle.cycle_date == stored_cycle.cycle_date
    assert cycle.snake.id == stored_cycle.snake.id


def test_update_cycle(db: Session) -> None:
    snake = create_random_snake(db)

    cycle_type = 'follicles'
    notes = ""
    cycle_date = "2020-04-20"

    cycle_in = CycleCreate(
        cycle_type=cycle_type,
        notes=notes,
        snake_id=snake.id,
        cycle_date=cycle_date,
    )
    cycle = crud.cycle.create_with_snake(db=db, obj_in=cycle_in)
    
    cycle_type2 = 'ovulation'
    cycle_update = CycleUpdate(cycle_type=cycle_type2)
    cycle2 = crud.cycle.update(db=db, db_obj=cycle, obj_in=cycle_update)
    assert cycle.id == cycle2.id
    assert cycle.cycle_date == cycle2.cycle_date
    assert cycle2.cycle_type == cycle_type2
    assert cycle2.notes == notes
    assert snake.id == cycle2.snake.id


def test_delete_cycle(db: Session) -> None:
    snake = create_random_snake(db)

    cycle_type = 'follicles'
    notes = ""
    cycle_date = "2020-04-20"

    cycle_in = CycleCreate(
        cycle_type=cycle_type,
        notes=notes,
        snake_id=snake.id,
        cycle_date=cycle_date,
    )

    cycle = crud.cycle.create_with_snake(db=db, obj_in=cycle_in)
    cycle2 = crud.cycle.remove(db=db, id=cycle.id)
    cycle3 = crud.cycle.get(db=db, id=cycle.id)
    assert cycle3 is None
    assert cycle2.id == cycle.id
    assert cycle2.cycle_date == datetime.strptime(cycle_date, '%Y-%m-%d')
    assert cycle2.cycle_type == cycle_type
    assert cycle2.notes == notes
    assert cycle2.snake.id == snake.id
