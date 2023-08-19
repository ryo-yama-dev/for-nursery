import strawberry

from app.database import EmployeeRecordModel, create_session
from app.inputs import EmployeeRecordCreateInput
from app.repositories import EmployeeRecordRepository
from app.types import EmployeeRecord

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
        print("data", data.to_dict())
        return EmployeeRecord(
            **data.to_dict(), employee=EmployeeService._data_format(data.employee)
        )

    def find_all(self) -> list[EmployeeRecord]:
        with create_session() as session:
            records = EmployeeRecordRepository(session).find_all()
            return [self._data_format(record) for record in records]

    def create(self, input: EmployeeRecordCreateInput) -> EmployeeRecord:
        with create_session() as session:
            record = EmployeeRecordRepository(session).create(strawberry.asdict(input))
            return self._data_format(record)
