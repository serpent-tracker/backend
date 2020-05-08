from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.config import settings
from app.tests.utils.snake import create_random_snake


def test_create_snake(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"name": "test snake", "description": "test snake"}
    response = client.post(
        f"{settings.API_V1_STR}/snakes/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content
    assert "created_at" in content
    assert "hatch_date" in content
    assert "sex" in content
    assert "produced_by" in content


def test_read_snake(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    response = client.get(
        f"{settings.API_V1_STR}/snakes/{snake.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == snake.name
    assert content["description"] == snake.description
    assert content["id"] == snake.id
    assert content["owner_id"] == snake.owner_id
    assert content["created_at"] == snake.created_at.isoformat()
    assert content["hatch_date"] == '2020-04-20'
    assert content["sex"] == snake.sex
    assert content["produced_by"] == snake.produced_by
