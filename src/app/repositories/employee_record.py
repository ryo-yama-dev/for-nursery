from sqlalchemy import ScalarResult, select

from app.database import EmployeeRecordModel
from app.repositories import BaseRepository

__all__ = ["EmployeeRecordRepository"]


class EmployeeRecordRepository(BaseRepository):
    """
    従業員記録
    """

    def find_all(self) -> ScalarResult[EmployeeRecordModel]:
        stmt = select(EmployeeRecordModel)
        return self.session.scalars(stmt)
