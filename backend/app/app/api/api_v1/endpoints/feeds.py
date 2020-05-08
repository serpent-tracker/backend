from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Feed])
def read_feeds(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    snake_id: int = 0,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve feeds.
    """
    if crud.user.is_superuser(current_user):
        feeds = crud.feed.get_multi_by_snake(db, snake_id=snake_id, skip=skip, limit=limit)
    else:
        feeds = crud.feed.get_multi_by_snake(
            db=db, snake_id=snake_id, skip=skip, limit=limit
        )
    return feeds


@router.post("/", response_model=schemas.Feed)
def create_feed(
    *,
    db: Session = Depends(deps.get_db),
    feed_in: schemas.FeedCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new feed.
    """
    feed = crud.feed.create_with_snake(db=db, obj_in=feed_in)
    return feed


@router.put("/{id}", response_model=schemas.Feed)
def update_feed(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    feed_in: schemas.FeedUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an feed.
    """
    feed = crud.feed.get(db=db, id=id)
    if not feed:
        raise HTTPException(status_code=404, detail="Feed not found")
    if not crud.user.is_superuser(current_user) and (feed.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    feed = crud.feed.update(db=db, db_obj=feed, obj_in=feed_in)
    return feed


@router.get("/{id}", response_model=schemas.Feed)
def read_feed(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get feed by ID.
    """
    feed = crud.feed.get(db=db, id=id)
    if not feed:
        raise HTTPException(status_code=404, detail="Feed not found")
    if not crud.user.is_superuser(current_user) and (feed.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return feed


@router.delete("/{id}", response_model=schemas.Feed)
def delete_feed(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an feed.
    """
    feed = crud.feed.get(db=db, id=id)
    if not feed:
        raise HTTPException(status_code=404, detail="Feed not found")
    if not crud.user.is_superuser(current_user) and (feed.snake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    feed = crud.feed.remove(db=db, id=id)
    return feed
