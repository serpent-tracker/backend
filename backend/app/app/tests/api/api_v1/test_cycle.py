from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.cycle import CycleCreate
from app.tests.utils.snake import create_random_snake


def test_create_cycle(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    data = {
        "cycle_type": "follicles",
        "cycle_date": "2020-04-20",
        "notes": "",
        "snake_id": snake.id,
    }
    response = client.post(
        f"{settings.API_V1_STR}/cycles/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["cycle_type"] == data["cycle_type"]
    assert content["notes"] == data["notes"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "cycle_date" in content


def test_read_cycle(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)

    cycle_type = 'ovulation'
    notes = ""
    snake_id = snake.id
    cycle_date = "2020-04-20"

    cycle_in = CycleCreate(
        cycle_type=cycle_type,
        notes=notes,
        snake_id=snake.id,
        cycle_date=cycle_date,
    )
    cycle = crud.cycle.create_with_snake(db=db, obj_in=cycle_in)

    response = client.get(
        f"{settings.API_V1_STR}/cycles/{cycle.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["cycle_type"] == cycle.cycle_type
    assert content["notes"] == cycle.notes
    assert content["snake_id"] == cycle.snake_id
    assert content["id"] == cycle.id
    assert content["created_at"] == cycle.created_at.isoformat()
    assert content["cycle_date"] == "2020-04-20"
