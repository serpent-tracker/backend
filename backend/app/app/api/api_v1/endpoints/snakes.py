from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Snake])
def read_snakes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve snakes.
    """
    if crud.user.is_superuser(current_user):
        snakes = crud.snake.get_multi(db, skip=skip, limit=limit)
    else:
        snakes = crud.snake.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return snakes


@router.post("/", response_model=schemas.Snake)
def create_snake(
    *,
    db: Session = Depends(deps.get_db),
    snake_in: schemas.SnakeCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new snake.
    """
    snake = crud.snake.create_with_owner(db=db, obj_in=snake_in, owner_id=current_user.id)
    return snake


@router.put("/{id}", response_model=schemas.Snake)
def update_snake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    snake_in: schemas.SnakeUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an snake.
    """
    snake = crud.snake.get(db=db, id=id)
    if not snake:
        raise HTTPException(status_code=404, detail="Snake not found")
    if not crud.user.is_superuser(current_user) and (snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    snake = crud.snake.update(db=db, db_obj=snake, obj_in=snake_in)
    return snake


@router.get("/{id}", response_model=schemas.Snake)
def read_snake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get snake by ID.
    """
    snake = crud.snake.get(db=db, id=id)
    if not snake:
        raise HTTPException(status_code=404, detail="Snake not found")
    if not crud.user.is_superuser(current_user) and (snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return snake


@router.delete("/{id}", response_model=schemas.Snake)
def delete_snake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an snake.
    """
    snake = crud.snake.get(db=db, id=id)
    if not snake:
        raise HTTPException(status_code=404, detail="Snake not found")
    if not crud.user.is_superuser(current_user) and (snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    snake = crud.snake.remove(db=db, id=id)
    return snake
