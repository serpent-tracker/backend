from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Cycle])
def read_cycles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve cycles.
    """
    if crud.user.is_superuser(current_user):
        cycles = crud.cycle.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        cycles = crud.cycle.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return cycles


@router.post("/", response_model=schemas.Cycle)
def create_cycle(
    *,
    db: Session = Depends(deps.get_db),
    cycle_in: schemas.CycleCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new cycle.
    """
    cycle = crud.cycle.create_with_snake(db=db, obj_in=cycle_in)
    return cycle


@router.put("/{id}", response_model=schemas.Cycle)
def update_cycle(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    cycle_in: schemas.CycleUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an cycle.
    """
    cycle = crud.cycle.get(db=db, id=id)
    if not cycle:
        raise HTTPException(status_code=404, detail="Cycle not found")
    if not crud.user.is_superuser(current_user) and (cycle.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    cycle = crud.cycle.update(db=db, db_obj=cycle, obj_in=cycle_in)
    return cycle


@router.get("/{id}", response_model=schemas.Cycle)
def read_cycle(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get cycle by ID.
    """
    cycle = crud.cycle.get(db=db, id=id)
    if not cycle:
        raise HTTPException(status_code=404, detail="Cycle not found")
    if not crud.user.is_superuser(current_user) and (cycle.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return cycle


@router.delete("/{id}", response_model=schemas.Cycle)
def delete_cycle(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an cycle.
    """
    cycle = crud.cycle.get(db=db, id=id)
    if not cycle:
        raise HTTPException(status_code=404, detail="Cycle not found")
    if not crud.user.is_superuser(current_user) and (cycle.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    cycle = crud.cycle.remove(db=db, id=id)
    return cycle
