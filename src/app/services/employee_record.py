import calendar
import datetime
from typing import Sequence

import strawberry
from sqlalchemy import ScalarResult

from app.database import EmployeeModel, EmployeeRecordModel
from app.inputs import EmployeeRecordCreateInput
from app.repositories import EmployeeRecordRepository, EmployeeRepository
from app.types import EmployeeRecord, EmployeeRecordDaily

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
        return EmployeeRecord(**data.to_dict())

    @staticmethod
    def _extract_record_by_employee(
        employee_id: int,
        records: list[EmployeeRecordModel] | Sequence[EmployeeRecordModel],
    ) -> list[EmployeeRecordModel]:
        """
        従業員の記録を抽出する
        """
        return [record for record in records if record.employee_id == employee_id]

    @staticmethod
    def _between_format(
        data: ScalarResult[EmployeeRecordModel],
        employees: ScalarResult[EmployeeModel],
        start: datetime.date,
        end: datetime.date,
    ) -> list[EmployeeRecordDaily]:
        """
        EmployeeRecordModel の内容を start と end の期間で整形する
        1. start と end 間の日付を算出してリスト化
        2. 従業員記録を従業員毎にカテゴリ分け
          2-a. 特定の従業員の記録を抽出
          2-b. 記録を日付順に並び変える
        """
        span = (end - start).days + 1
        date_list = [start + datetime.timedelta(days=i) for i in range(span)]
        employee_records = data.fetchall()
        result: list[EmployeeRecordDaily] = []
        for employee in employees.fetchall():
            records = EmployeeRecordService._extract_record_by_employee(
                employee.id, employee_records
            )
            # 日付順にソート
            records.sort(key=lambda record: record.date)

            # 指定の期間のすべての日付を設定
            # その日の記録がなければ空のリストを設定
            daily: list[EmployeeRecord] = []
            for date in date_list:
                # 該当の日付に記録がある場合にそのレコードのインデックスを取得
                # 該当レコードをインデックスでpopしていく
                indexes = [i for i, record in enumerate(records) if record.date == date]
                if len(indexes) > 0:
                    target = records.pop(indexes[0])
                    daily.append(EmployeeRecordService._data_format(target))
                # 該当レコードがなければ None を設定
                else:
                    daily.append(None)

            result.append(
                EmployeeRecordDaily(
                    employee=EmployeeService._data_format(employee),
                    records=daily,
                )
            )

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
    ) -> list[EmployeeRecordDaily]:
        """
        従業員記録を週次で取得
        """
        # TODO: week = 0 の場合のバリデーション
        w_list = calendar.monthcalendar(year, month)[week - 1]
        start = datetime.date(year, month, w_list[0])
        end = datetime.date(year, month, w_list[-1])
        records = EmployeeRecordRepository(self.session).find_by_between(start, end)
        employees = EmployeeRepository(self.session).find_all()
        return self._between_format(records, employees, start, end)

    def filter_by_month(self, year: int, month: int) -> list[EmployeeRecordDaily]:
        """
        従業員記録を月次で取得
        """
        records = EmployeeRecordRepository(self.session).find_by_month(year, month)
        employees = EmployeeRepository(self.session).find_all()
        return self._between_format(
            records,
            employees,
            datetime.date(year, month, 1),
            datetime.date(year, month, calendar.monthrange(year, month)[1]),
        )
