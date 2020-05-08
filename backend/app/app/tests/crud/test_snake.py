from sqlalchemy.orm import Session

from app import crud
from app.schemas.snake import SnakeCreate, SnakeUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_snake(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    produced_by = "Breeder ABC"
    sex = "male"
    hatch_date = "2020-04-20"
    snake_in = SnakeCreate(
        name=name,
        description=description,
        hatch_date=hatch_date,
        sex=sex,
        produced_by=produced_by,
    )
    user = create_random_user(db)
    snake = crud.snake.create_with_owner(db=db, obj_in=snake_in, owner_id=user.id)
    assert snake.name == name
    assert snake.description == description
    assert snake.sex == sex
    assert hatch_date == '2020-04-20'
    assert produced_by == produced_by
    assert snake.owner_id == user.id


def test_get_snake(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    snake_in = SnakeCreate(name=name, description=description)
    user = create_random_user(db)
    snake = crud.snake.create_with_owner(db=db, obj_in=snake_in, owner_id=user.id)
    stored_snake = crud.snake.get(db=db, id=snake.id)
    assert stored_snake
    assert snake.id == stored_snake.id
    assert snake.name == stored_snake.name
    assert snake.description == stored_snake.description
    assert snake.owner_id == stored_snake.owner_id


def test_update_snake(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    snake_in = SnakeCreate(name=name, description=description)
    user = create_random_user(db)
    snake = crud.snake.create_with_owner(db=db, obj_in=snake_in, owner_id=user.id)
    description2 = random_lower_string()
    snake_update = SnakeUpdate(description=description2)
    snake2 = crud.snake.update(db=db, db_obj=snake, obj_in=snake_update)
    assert snake.id == snake2.id
    assert snake.name == snake2.name
    assert snake2.description == description2
    assert snake.owner_id == snake2.owner_id


def test_delete_snake(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    snake_in = SnakeCreate(name=name, description=description)
    user = create_random_user(db)
    snake = crud.snake.create_with_owner(db=db, obj_in=snake_in, owner_id=user.id)
    snake2 = crud.snake.remove(db=db, id=snake.id)
    snake3 = crud.snake.get(db=db, id=snake.id)
    assert snake3 is None
    assert snake2.id == snake.id
    assert snake2.name == name
    assert snake2.description == description
    assert snake2.owner_id == user.id
