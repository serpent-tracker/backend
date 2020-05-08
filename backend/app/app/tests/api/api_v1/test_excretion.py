from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.excretion import ExcretionCreate
from app.tests.utils.snake import create_random_snake


def test_create_excretion(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    data = {"urates": True, "feces": False, "notes": "test note", "excretion_date": "2020-04-20", "snake_id": snake.id}
    response = client.post(
        f"{settings.API_V1_STR}/excretions/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["urates"] == data["urates"]
    assert content["feces"] == data["feces"]
    assert content["notes"] == data["notes"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "excretion_date" in content


def test_read_excretion(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    urates = False
    feces = False
    notes = "test note"
    excretion_date = "2020-04-20"

    # Create fake snake
    snake = create_random_snake(db)

    excretion_in = ExcretionCreate(
        urates=urates,
        feces=feces,
        notes=notes,
        excretion_date=excretion_date,
        snake_id=snake.id
    )
    excretion = crud.excretion.create_with_snake(db=db, obj_in=excretion_in)

    response = client.get(
        f"{settings.API_V1_STR}/excretions/{excretion.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["urates"] == excretion.urates
    assert content["feces"] == excretion.feces
    assert content["notes"] == excretion.notes
    assert content["snake_id"] == excretion.snake_id
    assert content["id"] == excretion.id
    assert content["created_at"] == excretion.created_at.isoformat()
    assert content["excretion_date"] == "2020-04-20"