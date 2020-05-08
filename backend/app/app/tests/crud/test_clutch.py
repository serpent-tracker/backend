from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.clutch import ClutchCreate, ClutchUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.tests.utils.snake import create_random_snake


def test_create_clutch(db: Session) -> None:
    snake = create_random_snake(db)
    father = create_random_snake(db)

    clutch_type = 'egg'
    laid_date = "2020-04-20"
    due_date = "2020-06-20"
    egg_count = 8
    good_egg_count = 7
    bad_egg_count = 1

    clutch_in = ClutchCreate(
        clutch_type=clutch_type,
        snake_id=snake.id,
        father_id=father.id,
        laid_date=laid_date,
        due_date=due_date,
        egg_count=egg_count,
        good_egg_count=good_egg_count,
        bad_egg_count=bad_egg_count
    )
    clutch = crud.clutch.create_with_snake(db=db, obj_in=clutch_in)
    assert clutch.clutch_type == clutch_type
    assert clutch.egg_count == egg_count
    assert clutch.good_egg_count == good_egg_count
    assert clutch.bad_egg_count == bad_egg_count
    assert clutch.father_id == father.id
    assert clutch.laid_date == datetime.strptime(laid_date, '%Y-%m-%d')
    assert clutch.snake_id == snake.id


def test_get_clutch(db: Session) -> None:
    snake = create_random_snake(db)
    father = create_random_snake(db)

    clutch_type = 'egg'
    laid_date = "2020-04-20"
    due_date = "2020-06-20"
    egg_count = 8
    good_egg_count = 7
    bad_egg_count = 1

    clutch_in = ClutchCreate(
        clutch_type=clutch_type,
        snake_id=snake.id,
        father_id=father.id,
        laid_date=laid_date,
        due_date=due_date,
        egg_count=egg_count,
        good_egg_count=good_egg_count,
        bad_egg_count=bad_egg_count
    )
    clutch = crud.clutch.create_with_snake(db=db, obj_in=clutch_in)
    stored_clutch = crud.clutch.get(db=db, id=clutch.id)
    assert clutch
    assert clutch.id == stored_clutch.id
    assert clutch.egg_count == stored_clutch.egg_count
    assert clutch.good_egg_count == stored_clutch.good_egg_count
    assert clutch.bad_egg_count == stored_clutch.bad_egg_count
    assert clutch.father_id == stored_clutch.father_id
    assert clutch.laid_date == stored_clutch.laid_date
    assert clutch.snake.id == stored_clutch.snake.id


def test_update_clutch(db: Session) -> None:
    snake = create_random_snake(db)
    father = create_random_snake(db)

    clutch_type = 'egg'
    laid_date = "2020-04-20"
    egg_count = 8
    good_egg_count = 7
    bad_egg_count = 1

    clutch_in = ClutchCreate(
        clutch_type=clutch_type,
        snake_id=snake.id,
        father_id=father.id,
        laid_date=laid_date,
        egg_count=egg_count,
        good_egg_count=good_egg_count,
        bad_egg_count=bad_egg_count
    )
    clutch = crud.clutch.create_with_snake(db=db, obj_in=clutch_in)
    
    egg_count2 = 9
    bad_egg_count2 = 2
    clutch_update = ClutchUpdate(egg_count=egg_count2, bad_egg_count=bad_egg_count2)
    clutch2 = crud.clutch.update(db=db, db_obj=clutch, obj_in=clutch_update)
    assert clutch.id == clutch2.id
    assert clutch.laid_date == clutch2.laid_date
    assert clutch2.egg_count == egg_count2
    assert clutch2.bad_egg_count == bad_egg_count2
    assert snake.id == clutch2.snake.id
    assert clutch.father_id == clutch.father_id


def test_delete_clutch(db: Session) -> None:
    snake = create_random_snake(db)
    father = create_random_snake(db)

    clutch_type = 'egg'
    laid_date = "2020-04-20"
    egg_count = 8
    good_egg_count = 7
    bad_egg_count = 1

    clutch_in = ClutchCreate(
        clutch_type=clutch_type,
        snake_id=snake.id,
        father_id=father.id,
        laid_date=laid_date,
        egg_count=egg_count,
        good_egg_count=good_egg_count,
        bad_egg_count=bad_egg_count
    )
    clutch = crud.clutch.create_with_snake(db=db, obj_in=clutch_in)

    clutch2 = crud.clutch.remove(db=db, id=clutch.id)
    clutch3 = crud.clutch.get(db=db, id=clutch.id)
    assert clutch3 is None
    assert clutch2.id == clutch.id
    assert clutch2.laid_date == datetime.strptime(laid_date, '%Y-%m-%d')
    assert clutch2.clutch_type == clutch_type
    assert clutch2.egg_count == egg_count
    assert clutch2.bad_egg_count == bad_egg_count
    assert clutch2.good_egg_count == good_egg_count
    assert clutch2.snake.id == snake.id
    assert clutch2.father_id == father.id
