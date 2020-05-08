from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Weight])
def read_weights(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve weights.
    """
    if crud.user.is_superuser(current_user):
        weights = crud.weight.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        weights = crud.weight.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return weights


@router.post("/", response_model=schemas.Weight)
def create_weight(
    *,
    db: Session = Depends(deps.get_db),
    weight_in: schemas.WeightCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new weight.
    """
    weight = crud.weight.create_with_snake(db=db, obj_in=weight_in)
    return weight


@router.put("/{id}", response_model=schemas.Weight)
def update_weight(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    weight_in: schemas.WeightUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an weight.
    """
    weight = crud.weight.get(db=db, id=id)
    if not weight:
        raise HTTPException(status_code=404, detail="Weight not found")
    if not crud.user.is_superuser(current_user) and (weight.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    weight = crud.weight.update(db=db, db_obj=weight, obj_in=weight_in)
    return weight


@router.get("/{id}", response_model=schemas.Weight)
def read_weight(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get weight by ID.
    """
    weight = crud.weight.get(db=db, id=id)
    if not weight:
        raise HTTPException(status_code=404, detail="Weight not found")
    if not crud.user.is_superuser(current_user) and (weight.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return weight


@router.delete("/{id}", response_model=schemas.Weight)
def delete_weight(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an weight.
    """
    weight = crud.weight.get(db=db, id=id)
    if not weight:
        raise HTTPException(status_code=404, detail="Weight not found")
    if not crud.user.is_superuser(current_user) and (weight.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    weight = crud.weight.remove(db=db, id=id)
    return weight
