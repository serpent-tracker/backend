from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.feed import FeedCreate
from app.tests.utils.snake import create_random_snake


def test_create_feed(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    data = {
        "prey": "rat",
        "prey_type": "ft",
        "prey_size": "small",
        "feed_date": "2020-04-20",
        "count": 1,
        "snake_id": snake.id,
    }
    response = client.post(
        f"{settings.API_V1_STR}/feeds/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["prey"] == data["prey"]
    assert content["prey_type"] == data["prey_type"]
    assert content["prey_size"] == data["prey_size"]
    assert content["count"] == data["count"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "feed_date" in content


def test_read_shed(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
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

    response = client.get(
        f"{settings.API_V1_STR}/feeds/{feed.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["prey"] == feed.prey
    assert content["prey_type"] == feed.prey_type
    assert content["prey_size"] == feed.prey_size
    assert content["count"] == feed.count
    assert content["snake_id"] == feed.snake_id
    assert content["id"] == feed.id
    assert content["created_at"] == feed.created_at.isoformat()
    assert content["feed_date"] == "2020-04-20"
