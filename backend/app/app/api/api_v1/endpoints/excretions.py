from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Excretion])
def read_excretions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve excretions.
    """
    if crud.user.is_superuser(current_user):
        excretions = crud.excretion.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        excretions = crud.excretion.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return excretions


@router.post("/", response_model=schemas.Excretion)
def create_excretion(
    *,
    db: Session = Depends(deps.get_db),
    excretion_in: schemas.ExcretionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new excretion.
    """
    excretion = crud.excretion.create_with_snake(db=db, obj_in=excretion_in)
    return excretion


@router.put("/{id}", response_model=schemas.Excretion)
def update_excretion(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    excretion_in: schemas.ExcretionUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an excretion.
    """
    excretion = crud.excretion.get(db=db, id=id)
    if not excretion:
        raise HTTPException(status_code=404, detail="Excretion not found")
    if not crud.user.is_superuser(current_user) and (excretion.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    excretion = crud.excretion.update(db=db, db_obj=excretion, obj_in=excretion_in)
    return excretion


@router.get("/{id}", response_model=schemas.Excretion)
def read_excretion(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get excretion by ID.
    """
    excretion = crud.excretion.get(db=db, id=id)
    if not excretion:
        raise HTTPException(status_code=404, detail="Excretion not found")
    if not crud.user.is_superuser(current_user) and (excretion.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return excretion


@router.delete("/{id}", response_model=schemas.Excretion)
def delete_excretion(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an excretion.
    """
    excretion = crud.excretion.get(db=db, id=id)
    if not excretion:
        raise HTTPException(status_code=404, detail="Excretion not found")
    if not crud.user.is_superuser(current_user) and (excretion.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    excretion = crud.excretion.remove(db=db, id=id)
    return excretion
