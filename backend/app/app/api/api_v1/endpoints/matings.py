from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Mating])
def read_matings(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve matings.
    """
    if crud.user.is_superuser(current_user):
        matings = crud.mating.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        matings = crud.mating.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return matings


@router.post("/", response_model=schemas.Mating)
def create_mating(
    *,
    db: Session = Depends(deps.get_db),
    mating_in: schemas.MatingCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new mating.
    """
    mating = crud.mating.create_with_snake(db=db, obj_in=mating_in)
    return mating


@router.put("/{id}", response_model=schemas.Mating)
def update_mating(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    mating_in: schemas.MatingUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an mating.
    """
    mating = crud.mating.get(db=db, id=id)
    if not mating:
        raise HTTPException(status_code=404, detail="Mating not found")
    if not crud.user.is_superuser(current_user) and (mating.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    mating = crud.mating.update(db=db, db_obj=mating, obj_in=mating_in)
    return mating


@router.get("/{id}", response_model=schemas.Mating)
def read_mating(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get mating by ID.
    """
    mating = crud.mating.get(db=db, id=id)
    if not mating:
        raise HTTPException(status_code=404, detail="Mating not found")
    if not crud.user.is_superuser(current_user) and (mating.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return mating


@router.delete("/{id}", response_model=schemas.Mating)
def delete_mating(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an mating.
    """
    mating = crud.mating.get(db=db, id=id)
    if not mating:
        raise HTTPException(status_code=404, detail="Mating not found")
    if not crud.user.is_superuser(current_user) and (mating.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    mating = crud.mating.remove(db=db, id=id)
    return mating
