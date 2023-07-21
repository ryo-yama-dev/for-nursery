from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from common.models import EmployeeRecordModel

__all__ = ["EmployeeRecordRepository"]


class EmployeeRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> ScalarResult[EmployeeRecordModel]:
        stmt = select(EmployeeRecordModel)
        return self.session.scalars(stmt)
