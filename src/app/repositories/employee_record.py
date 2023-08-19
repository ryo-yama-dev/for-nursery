from typing import Any

from sqlalchemy import ScalarResult, insert, select

from app.common import dict_exclude_none
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

    def create(
        self,
        kwargs: dict[str, Any] = {},
    ) -> EmployeeRecordModel:
        input: dict[str, Any] = dict_exclude_none(kwargs)
        employee = self.session.execute(
            insert(EmployeeRecordModel).values(**input).returning(EmployeeRecordModel)
        )
        self.session.commit()
        return employee.scalar_one()
