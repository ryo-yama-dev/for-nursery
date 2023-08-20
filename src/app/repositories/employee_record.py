import calendar
import datetime
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

    def find_by_date(self, date: datetime.date) -> ScalarResult[EmployeeRecordModel]:
        """
        従業員記録を日次で取得
        """
        stmt = select(EmployeeRecordModel).where(EmployeeRecordModel.date == date)
        return self.session.scalars(stmt)

    def find_by_between(
        self, start: datetime.date, end: datetime.date
    ) -> ScalarResult[EmployeeRecordModel]:
        """
        従業員記録を期間で取得
        """
        stmt = select(EmployeeRecordModel).where(
            EmployeeRecordModel.date >= start, EmployeeRecordModel.date <= end
        )
        return self.session.scalars(stmt)

    def find_by_month(self, year: int, month: int) -> ScalarResult[EmployeeRecordModel]:
        """
        従業員記録を月次で取得
        """
        start = datetime.date(year, month, 1)
        end = datetime.date(year, month, calendar.monthrange(year, month)[1])
        stmt = select(EmployeeRecordModel).where(
            EmployeeRecordModel.date >= start, EmployeeRecordModel.date <= end
        )
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
