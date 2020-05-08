from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.shed import ShedCreate, ShedUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_weight_int, random_lower_string
from app.tests.utils.snake import create_random_snake



def test_create_shed(db: Session) -> None:
    complete = False
    pre_lay = False
    shed_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    shed_in = ShedCreate(
        complete=complete,
        pre_lay=pre_lay,
        shed_date=shed_date,
        snake_id=snake.id
    )
    shed = crud.shed.create_with_snake(db=db, obj_in=shed_in)
    assert shed.complete == complete
    assert shed.pre_lay == pre_lay
    assert shed.shed_date == datetime.strptime(shed_date, '%Y-%m-%d')
    assert shed.snake_id == snake.id


def test_get_shed(db: Session) -> None:
    complete = False
    pre_lay = False
    shed_date = "2020-04-20"

    
    # Create fake snake
    snake = create_random_snake(db)

    shed_in = ShedCreate(
        complete=complete,
        pre_lay=pre_lay,
        shed_date=shed_date,
        snake_id=snake.id
    )
    shed = crud.shed.create_with_snake(db=db, obj_in=shed_in)
    stored_shed = crud.shed.get(db=db, id=shed.id)
    assert shed
    assert shed.id == stored_shed.id
    assert shed.complete == stored_shed.complete
    assert shed.pre_lay == stored_shed.pre_lay
    assert shed.shed_date == stored_shed.shed_date
    assert shed.snake.id == stored_shed.snake.id


def test_update_shed(db: Session) -> None:
    complete = False
    pre_lay = False
    shed_date = "2020-04-20"

    # Create Fake Snake
    snake = create_random_snake(db)

    shed_in = ShedCreate(
        complete=complete,
        pre_lay=pre_lay,
        shed_date=shed_date,
        snake_id=snake.id
    )
    shed = crud.shed.create_with_snake(db=db, obj_in=shed_in)
    
    complete2 = True
    shed_update = ShedUpdate(complete=complete2)
    shed2 = crud.shed.update(db=db, db_obj=shed, obj_in=shed_update)
    assert shed.id == shed2.id
    assert shed.shed_date == shed2.shed_date
    assert shed2.complete == complete2
    assert shed.pre_lay == shed2.pre_lay
    assert shed.snake.id == shed2.snake.id


def test_delete_shed(db: Session) -> None:
    complete = False
    pre_lay = False
    shed_date = "2020-04-20"

    # Create Fake Snake
    snake = create_random_snake(db)

    shed_in = ShedCreate(
        complete=complete,
        pre_lay=pre_lay,
        shed_date=shed_date,
        snake_id=snake.id
    )

    shed = crud.shed.create_with_snake(db=db, obj_in=shed_in)
    shed2 = crud.shed.remove(db=db, id=shed.id)
    shed3 = crud.shed.get(db=db, id=shed.id)
    assert shed3 is None
    assert shed2.id == shed.id
    assert shed2.shed_date == datetime.strptime(shed_date, '%Y-%m-%d')
    assert shed2.complete == complete
    assert shed2.pre_lay == pre_lay
    assert shed2.snake.id == snake.id
