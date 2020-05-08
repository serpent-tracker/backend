from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Shed])
def read_sheds(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve sheds.
    """
    if crud.user.is_superuser(current_user):
        sheds = crud.shed.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        sheds = crud.shed.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return sheds


@router.post("/", response_model=schemas.Shed)
def create_shed(
    *,
    db: Session = Depends(deps.get_db),
    shed_in: schemas.ShedCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new shed.
    """
    shed = crud.shed.create_with_snake(db=db, obj_in=shed_in)
    return shed


@router.put("/{id}", response_model=schemas.Shed)
def update_shed(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    shed_in: schemas.ShedUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an shed.
    """
    shed = crud.shed.get(db=db, id=id)
    if not shed:
        raise HTTPException(status_code=404, detail="Shed not found")
    if not crud.user.is_superuser(current_user) and (shed.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    shed = crud.shed.update(db=db, db_obj=shed, obj_in=shed_in)
    return shed


@router.get("/{id}", response_model=schemas.Shed)
def read_shed(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get shed by ID.
    """
    shed = crud.shed.get(db=db, id=id)
    if not shed:
        raise HTTPException(status_code=404, detail="Shed not found")
    if not crud.user.is_superuser(current_user) and (shed.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return shed


@router.delete("/{id}", response_model=schemas.Shed)
def delete_shed(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an shed.
    """
    shed = crud.shed.get(db=db, id=id)
    if not shed:
        raise HTTPException(status_code=404, detail="Shed not found")
    if not crud.user.is_superuser(current_user) and (shed.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    shed = crud.shed.remove(db=db, id=id)
    return shed
