from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from app.database import ChildModel

__all__ = ["ChildRepository"]


class ChildRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> ScalarResult[ChildModel]:
        stmt = select(ChildModel)
        return self.session.scalars(stmt)

    def find_by_id(self, id: int) -> ChildModel | None:
        return self.session.scalar(select(ChildModel).where(ChildModel.id == id))
