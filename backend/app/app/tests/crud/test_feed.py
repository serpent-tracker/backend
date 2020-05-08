from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.snake import SnakeCreate
from app.schemas.feed import FeedCreate, FeedUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.tests.utils.snake import create_random_snake



def test_create_feed(db: Session) -> None:
    prey = 'rat'
    prey_type = 'ft'
    prey_size = 'small'
    count = 1
    feed_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    feed_in = FeedCreate(
        prey=prey,
        prey_type=prey_type,
        prey_size=prey_size,
        count=count,
        feed_date=feed_date,
        snake_id=snake.id
    )
    feed = crud.feed.create_with_snake(db=db, obj_in=feed_in)
    assert feed.prey == prey
    assert feed.prey_type == prey_type
    assert feed.prey_size == prey_size
    assert feed.count == count
    assert feed.feed_date == datetime.strptime(feed_date, '%Y-%m-%d')
    assert feed.snake_id == snake.id


def test_get_feed(db: Session) -> None:
    prey = 'rat'
    prey_type = 'ft'
    prey_size = 'small'
    count = 1
    feed_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    feed_in = FeedCreate(
        prey=prey,
        prey_type=prey_type,
        prey_size=prey_size,
        count=count,
        feed_date=feed_date,
        snake_id=snake.id
    )
    feed = crud.feed.create_with_snake(db=db, obj_in=feed_in)
    stored_feed = crud.feed.get(db=db, id=feed.id)
    assert feed
    assert feed.id == stored_feed.id
    assert feed.prey == stored_feed.prey
    assert feed.prey_type == stored_feed.prey_type
    assert feed.prey_size == stored_feed.prey_size
    assert feed.count == stored_feed.count
    assert feed.feed_date == stored_feed.feed_date
    assert feed.snake.id == stored_feed.snake.id


def test_update_feed(db: Session) -> None:
    prey = 'rat'
    prey_type = 'ft'
    prey_size = 'small'
    count = 1
    feed_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    feed_in = FeedCreate(
        prey=prey,
        prey_type=prey_type,
        prey_size=prey_size,
        count=count,
        feed_date=feed_date,
        snake_id=snake.id
    )
    feed = crud.feed.create_with_snake(db=db, obj_in=feed_in)
    
    count2 = 2
    prey_size2 = 'large'
    feed_update = FeedUpdate(count=count2, prey_size=prey_size2)
    feed2 = crud.feed.update(db=db, db_obj=feed, obj_in=feed_update)
    assert feed.id == feed2.id
    assert feed.feed_date == feed2.feed_date
    assert feed2.count == count2
    assert feed2.prey_size == prey_size2
    assert feed.snake.id == feed2.snake.id


def test_delete_feed(db: Session) -> None:
    prey = 'rat'
    prey_type = 'ft'
    prey_size = 'small'
    count = 1
    feed_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    feed_in = FeedCreate(
        prey=prey,
        prey_type=prey_type,
        prey_size=prey_size,
        count=count,
        feed_date=feed_date,
        snake_id=snake.id
    )

    feed = crud.feed.create_with_snake(db=db, obj_in=feed_in)
    feed2 = crud.feed.remove(db=db, id=feed.id)
    feed3 = crud.feed.get(db=db, id=feed.id)
    assert feed3 is None
    assert feed2.id == feed.id
    assert feed2.feed_date == datetime.strptime(feed_date, '%Y-%m-%d')
    assert feed2.count == count
    assert feed2.snake.id == snake.id
