from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from app.database import ClassroomModel

__all__ = ["ClassroomRepository"]


class ClassroomRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> ScalarResult[ClassroomModel]:
        stmt = select(ClassroomModel)
        return self.session.scalars(stmt)
