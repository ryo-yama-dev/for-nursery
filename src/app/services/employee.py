from app.repositories import EmployeeRepository
from app.types import Employee, Job, Profile

from .base import BaseService

__all__ = ["EmployeeService"]


class EmployeeService(BaseService):
    """ """

    def find_all(self) -> list[Employee]:
        return [
            Employee(
                **employee.to_dict(),
                job=Job(**employee.job.to_dict()),
                profiles=[Profile(**prof.to_dict()) for prof in employee.profiles],
            )
            for employee in EmployeeRepository(self.session).find_all()
        ]

    def find_one(self, id: int) -> Employee | None:
        employee = EmployeeRepository(self.session).find_by_id(id=id)
        return (
            Employee(
                **employee.to_dict(),
                job=Job(**employee.job.to_dict()),
                profiles=[Profile(**prof.to_dict()) for prof in employee.profiles],
            )
            if employee
            else None
        )
