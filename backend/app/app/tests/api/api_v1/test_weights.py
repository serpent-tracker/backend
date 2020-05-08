from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.weight import WeightCreate
from app.tests.utils.utils import random_weight_int
from app.tests.utils.snake import create_random_snake


def test_create_weight(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    data = {"weight": 100, "weight_date": "2020-04-20", "snake_id": snake.id}
    response = client.post(
        f"{settings.API_V1_STR}/weights/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["weight"] == data["weight"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "weight_date" in content


def test_read_weight(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    weight = random_weight_int()
    weight_date = "2020-04-20"

    snake = create_random_snake(db)

    weight_in = WeightCreate(
        weight=weight,
        weight_date=weight_date,
        snake_id=snake.id
    )
    weight_record = crud.weight.create_with_snake(db=db, obj_in=weight_in)

    response = client.get(
        f"{settings.API_V1_STR}/weights/{weight_record.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["weight"] == weight_record.weight
    assert content["snake_id"] == weight_record.snake_id
    assert content["id"] == weight_record.id
    assert content["created_at"] == weight_record.created_at.isoformat()
    assert content["weight_date"] == '2020-04-20'