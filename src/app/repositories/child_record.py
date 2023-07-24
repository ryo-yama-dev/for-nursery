from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from app.common.models import ChildRecordModel

__all__ = ["ChildRecordRepository"]


class ChildRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> ScalarResult[ChildRecordModel]:
        stmt = select(ChildRecordModel)
        return self.session.scalars(stmt)
