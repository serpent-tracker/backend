from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.mating import Mating
from app.schemas.mating import MatingCreate, MatingUpdate


class CRUDMating(CRUDBase[Mating, MatingCreate, MatingUpdate]):
    def create_with_snake(
        self, db: Session, *, obj_in: MatingCreate
    ) -> Mating:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_snake(
        self, db: Session, *, snake_id: int, skip: int = 0, limit: int = 100
    ) -> List[Mating]:
        return (
            db.query(self.model)
            .filter(Mating.snake_id == snake_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


mating = CRUDMating(Mating)
