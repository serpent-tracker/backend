from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Clutch])
def read_clutchs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve clutchs.
    """
    if crud.user.is_superuser(current_user):
        clutchs = crud.clutch.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        clutchs = crud.clutch.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return clutchs


@router.post("/", response_model=schemas.Clutch)
def create_clutch(
    *,
    db: Session = Depends(deps.get_db),
    clutch_in: schemas.ClutchCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new clutch.
    """
    clutch = crud.clutch.create_with_snake(db=db, obj_in=clutch_in)
    return clutch


@router.put("/{id}", response_model=schemas.Clutch)
def update_clutch(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    clutch_in: schemas.ClutchUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an clutch.
    """
    clutch = crud.clutch.get(db=db, id=id)
    if not clutch:
        raise HTTPException(status_code=404, detail="Clutch not found")
    if not crud.user.is_superuser(current_user) and (clutch.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    clutch = crud.clutch.update(db=db, db_obj=clutch, obj_in=clutch_in)
    return clutch


@router.get("/{id}", response_model=schemas.Clutch)
def read_clutch(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get clutch by ID.
    """
    clutch = crud.clutch.get(db=db, id=id)
    if not clutch:
        raise HTTPException(status_code=404, detail="Clutch not found")
    if not crud.user.is_superuser(current_user) and (clutch.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return clutch


@router.delete("/{id}", response_model=schemas.Clutch)
def delete_clutch(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an clutch.
    """
    clutch = crud.clutch.get(db=db, id=id)
    if not clutch:
        raise HTTPException(status_code=404, detail="Clutch not found")
    if not crud.user.is_superuser(current_user) and (clutch.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    clutch = crud.clutch.remove(db=db, id=id)
    return clutch
