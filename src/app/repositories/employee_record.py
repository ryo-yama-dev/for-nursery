from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from app.database import EmployeeRecordModel

__all__ = ["EmployeeRecordRepository"]


class EmployeeRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> ScalarResult[EmployeeRecordModel]:
        stmt = select(EmployeeRecordModel)
        return self.session.scalars(stmt)
