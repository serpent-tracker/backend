from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.core.config import settings
from app.schemas.shed import ShedCreate
from app.tests.utils.snake import create_random_snake


def test_create_shed(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    snake = create_random_snake(db)
    data = {"complete": True, "pre_lay": False, "shed_date": "2020-04-20", "snake_id": snake.id}
    response = client.post(
        f"{settings.API_V1_STR}/sheds/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["complete"] == data["complete"]
    assert content["snake_id"] == data["snake_id"]
    assert "id" in content
    assert "created_at" in content
    assert "shed_date" in content


def test_read_shed(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
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

    response = client.get(
        f"{settings.API_V1_STR}/sheds/{shed.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["complete"] == shed.complete
    assert content["pre_lay"] == shed.pre_lay
    assert content["snake_id"] == shed.snake_id
    assert content["id"] == shed.id
    assert content["created_at"] == shed.created_at.isoformat()
    assert content["shed_date"] == "2020-04-20"