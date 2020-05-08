from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.weight import WeightCreate, WeightUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_weight_int, random_lower_string
from app.tests.utils.snake import create_random_snake


def test_create_weight(db: Session) -> None:
    weight = random_weight_int()
    weight_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    weight_in = WeightCreate(weight=weight, weight_date=weight_date, snake_id=snake.id)
    weight_record = crud.weight.create_with_snake(db=db, obj_in=weight_in)
    assert weight_record.weight == weight
    assert weight_record.weight_date == datetime.strptime(weight_date, "%Y-%m-%d")
    assert weight_record.snake_id == snake.id


def test_get_weight(db: Session) -> None:
    weight = random_weight_int()
    weight_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    weight_in = WeightCreate(weight=weight, weight_date=weight_date, snake_id=snake.id)
    weight_record = crud.weight.create_with_snake(db=db, obj_in=weight_in)
    stored_weight = crud.weight.get(db=db, id=weight_record.id)
    assert stored_weight
    assert weight_record.id == stored_weight.id
    assert weight_record.weight == stored_weight.weight
    assert weight_record.weight_date == stored_weight.weight_date
    assert weight_record.snake.id == stored_weight.snake.id


def test_update_weight(db: Session) -> None:
    weight = random_weight_int()
    weight_date = "2020-04-20"

    # Create Fake Snake
    snake = create_random_snake(db)

    weight_in = WeightCreate(weight=weight, weight_date=weight_date, snake_id=snake.id)
    weight_record = crud.weight.create_with_snake(db=db, obj_in=weight_in)

    weight2 = random_weight_int()
    weight_update = WeightUpdate(weight=weight2)
    weight_record2 = crud.weight.update(
        db=db, db_obj=weight_record, obj_in=weight_update
    )
    assert weight_record.id == weight_record2.id
    assert weight_record.weight_date == weight_record2.weight_date
    assert weight_record2.weight == weight2
    assert weight_record.snake.id == weight_record2.snake.id


def test_delete_weight(db: Session) -> None:
    weight = random_weight_int()
    weight_date = "2020-04-20"

    # Create Fake Snake
    snake = create_random_snake(db)

    weight_in = WeightCreate(weight=weight, weight_date=weight_date, snake_id=snake.id)

    weight_record = crud.weight.create_with_snake(db=db, obj_in=weight_in)
    weight_record2 = crud.weight.remove(db=db, id=weight_record.id)
    weight_record3 = crud.weight.get(db=db, id=weight_record.id)
    assert weight_record3 is None
    assert weight_record2.id == weight_record.id
    assert weight_record2.weight_date == datetime.strptime(weight_date, "%Y-%m-%d")
    assert weight_record2.weight == weight
    assert weight_record2.snake.id == snake.id
