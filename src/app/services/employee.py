import strawberry

from app.database import EmployeeModel
from app.inputs import EmployeeCreateInput
from app.repositories import EmployeeRepository
from app.types import Employee, Job, Profile

from .base import BaseService

__all__ = ["EmployeeService"]


# TODO: Profiles の並び順調整
class EmployeeService(BaseService):
    """
    従業員操作のための業務ロジック
    """

    @classmethod
    def _data_format(cls, data: EmployeeModel) -> Employee:
        """
        EmployeeModel を Employee に変換する
        """
        return Employee(
            **data.to_dict(),
            job=Job(**data.job.to_dict()),
            profiles=[Profile(**prof.to_dict()) for prof in data.profiles],
        )

    def find_all(self) -> list[Employee]:
        return [
            self._data_format(employee)
            for employee in EmployeeRepository(self.session).find_all()
        ]

    def find_one(self, id: int) -> Employee | None:
        employee = EmployeeRepository(self.session).find_by_id(id=id)
        return self._data_format(employee) if employee else None

    def create(self, input: EmployeeCreateInput) -> Employee:
        employee = EmployeeRepository(self.session).create(strawberry.asdict(input))
        return self._data_format(employee)
