import calendar
import datetime

import strawberry
from sqlalchemy import ScalarResult

from app.database import EmployeeRecordModel
from app.inputs import EmployeeRecordCreateInput
from app.repositories import EmployeeRecordRepository
from app.types import EmployeeDailyRecord, EmployeeRecord

from .base import BaseService
from .employee import EmployeeService

__all__ = ["EmployeeRecordService"]


class EmployeeRecordService(BaseService):
    """
    日次記録の操作用ロジック
    """

    @staticmethod
    def _data_format(data: EmployeeRecordModel) -> EmployeeRecord:
        """
        EmployeeRecordModel を EmployeeRecord に変換する
        """
        return EmployeeRecord(
            **data.to_dict(), employee=EmployeeService._data_format(data.employee)
        )

    @staticmethod
    def _between_format(
        data: ScalarResult[EmployeeRecordModel],
        start: datetime.date,
        end: datetime.date,
    ) -> list[EmployeeDailyRecord]:
        """
        EmployeeRecordModel の内容を start と end の期間で整形する
        1. start と end 間の日付を算出してリスト化
        2. 従業員記録を日付毎にカテゴリ分け
        """
        span = (end - start).days + 1
        date_list = [start + datetime.timedelta(days=i) for i in range(span)]
        records = data.fetchall()
        result: list[EmployeeDailyRecord] = []
        for date in date_list:
            targets = [
                EmployeeRecordService._data_format(record)
                for record in records
                if record.date == date
            ]
            if len(targets) > 0:
                result.append(EmployeeDailyRecord(date=date, records=targets))

            else:
                result.append(EmployeeDailyRecord(date=date, records=[]))

        return result

    def create(self, input: EmployeeRecordCreateInput) -> EmployeeRecord:
        record = EmployeeRecordRepository(self.session).create(strawberry.asdict(input))
        return self._data_format(record)

    def filter_by_date(self, date: datetime.date) -> list[EmployeeRecord]:
        """
        従業員記録を日次で取得
        """
        records = EmployeeRecordRepository(self.session).find_by_date(date)
        return [self._data_format(record) for record in records]

    def filter_by_week(
        self, year: int, month: int, week: int
    ) -> list[EmployeeDailyRecord]:
        """
        従業員記録を週次で取得
        """
        # TODO: week = 0 の場合のバリデーション
        w_list = calendar.monthcalendar(year, month)[week - 1]
        start = datetime.date(year, month, w_list[0])
        end = datetime.date(year, month, w_list[-1])
        records = EmployeeRecordRepository(self.session).find_by_between(start, end)
        return self._between_format(records, start, end)

    def filter_by_month(self, year: int, month: int) -> list[EmployeeDailyRecord]:
        """
        従業員記録を月次で取得
        """
        records = EmployeeRecordRepository(self.session).find_by_month(year, month)
        return self._between_format(
            records,
            datetime.date(year, month, 1),
            datetime.date(year, month, calendar.monthrange(year, month)[1]),
        )
