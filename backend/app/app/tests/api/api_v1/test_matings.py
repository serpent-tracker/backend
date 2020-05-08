from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.mating import MatingCreate
from app.tests.utils.snake import create_random_snake


def test_create_mating(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    mate = create_random_snake(db)
    data = {
        "event": "introduction",
        "event_date": "2020-04-20",
        "snake_id": snake.id,
        "mate_id": mate.id
    }
    response = client.post(
        f"{settings.API_V1_STR}/matings/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["event"] == data["event"]
    assert content["mate_id"] == data["mate_id"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "event_date" in content


def test_read_mating(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    mate = create_random_snake(db)

    event = 'introduction'
    snake_id = snake.id
    mate_id = mate.id
    event_date = "2020-04-20"

    mate_in = MatingCreate(
        event=event,
        snake_id=snake_id,
        mate_id=mate_id,
        event_date=event_date,
    )
    mating = crud.mating.create_with_snake(db=db, obj_in=mate_in)

    response = client.get(
        f"{settings.API_V1_STR}/matings/{mating.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["event"] == mating.event
    assert content["mate_id"] == mating.mate_id
    assert content["snake_id"] == mating.snake_id
    assert content["id"] == mating.id
    assert content["created_at"] == mating.created_at.isoformat()
    assert content["event_date"] == "2020-04-20"
