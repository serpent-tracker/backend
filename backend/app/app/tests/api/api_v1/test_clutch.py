
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.clutch import ClutchCreate
from app.tests.utils.snake import create_random_snake


def test_create_clutch(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    father = create_random_snake(db)
    data = {
        "clutch_type": "egg",
        "laid_date": "2020-04-20",
        "egg_count": 8,
        "bad_egg_count": 3,
        "good_egg_count": 5,
        "snake_id": snake.id,
        "father_id": father.id
    }
    response = client.post(
        f"{settings.API_V1_STR}/clutches/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["clutch_type"] == data["clutch_type"]
    assert content["egg_count"] == data["egg_count"]
    assert content["good_egg_count"] == data["good_egg_count"]
    assert content["bad_egg_count"] == data["bad_egg_count"]
    assert content["father_id"] == data["father_id"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "laid_date" in content


def test_read_clutch(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    father = create_random_snake(db)

    clutch_type = 'egg'
    laid_date = "2020-04-20"
    notes = ""
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
        bad_egg_count=bad_egg_count,
        notes=notes
    )
    clutch = crud.clutch.create_with_snake(db=db, obj_in=clutch_in)

    response = client.get(
        f"{settings.API_V1_STR}/clutches/{clutch.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["clutch_type"] == clutch.clutch_type
    assert content["egg_count"] == clutch.egg_count
    assert content["good_egg_count"] == clutch.good_egg_count
    assert content["bad_egg_count"] == clutch.bad_egg_count
    assert content["father_id"] == clutch.father_id
    assert content["snake_id"] == clutch.snake_id
    assert content["id"] == clutch.id
    assert content["created_at"] == clutch.created_at.isoformat()
    assert content["laid_date"] == "2020-04-20"
