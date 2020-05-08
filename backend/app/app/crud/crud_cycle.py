from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.cycle import Cycle
from app.schemas.cycle import CycleCreate, CycleUpdate


class CRUDCycle(CRUDBase[Cycle, CycleCreate, CycleUpdate]):
    def create_with_snake(
        self, db: Session, *, obj_in: CycleCreate
    ) -> Cycle:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_snake(
        self, db: Session, *, snake_id: int, skip: int = 0, limit: int = 100
    ) -> List[Cycle]:
        return (
            db.query(self.model)
            .filter(Cycle.snake_id == snake_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


cycle = CRUDCycle(Cycle)
