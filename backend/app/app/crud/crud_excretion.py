from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.excretion import Excretion
from app.schemas.excretion import ExcretionCreate, ExcretionUpdate


class CRUDExcretion(CRUDBase[Excretion, ExcretionCreate, ExcretionUpdate]):
    def create_with_snake(
        self, db: Session, *, obj_in: ExcretionCreate
    ) -> Excretion:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_snake(
        self, db: Session, *, snake_id: int, skip: int = 0, limit: int = 100
    ) -> List[Excretion]:
        return (
            db.query(self.model)
            .filter(Excretion.snake_id == snake_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


excretion = CRUDExcretion(Excretion)
