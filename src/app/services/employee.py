from typing import Any

import strawberry

from app.database import EmployeeModel
from app.inputs import EmployeeCreateInput, EmployeeFilterInput
from app.repositories import EmployeeRepository
from app.types import Employee, Job, Profile

from .base import BaseService

__all__ = ["EmployeeService"]


# TODO: Profiles の並び順調整
class EmployeeService(BaseService):
    """
    従業員操作のための業務ロジック
    """

    @staticmethod
    def _data_format(data: EmployeeModel) -> Employee:
        """
        EmployeeModel を Employee に変換する
        """
        return Employee(
            **data.to_dict(),
            job=Job(**data.job.to_dict()),
            profiles=[Profile(**prof.to_dict()) for prof in data.profiles],
        )

    def find_all(self, input: EmployeeFilterInput | None = None) -> list[Employee]:
        """
        条件を指定して従業員を全取得
        """
        d_input: dict[str, Any] = {}
        if input is not None:
            for key, value in strawberry.asdict(input).items():
                if value is not None:
                    d_input[key] = value

        return [
            self._data_format(employee)
            for employee in EmployeeRepository(self.session).find_all(**d_input)
        ]

    def find_one(self, id: int) -> Employee | None:
        employee = EmployeeRepository(self.session).find_by_id(id=id)
        return self._data_format(employee) if employee else None

    def create(self, input: EmployeeCreateInput) -> Employee:
        employee = EmployeeRepository(self.session).create(
            (strawberry.asdict(input) | {"sex": input.sex.value})
        )
        return self._data_format(employee)
