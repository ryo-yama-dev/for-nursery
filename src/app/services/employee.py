from app.repositories import EmployeeRepository
from app.types import Employee

from .base import BaseService

__all__ = ["EmployeeService"]


class EmployeeService(BaseService):
    """ """

    def find_all(self) -> list[Employee]:
        return [
            Employee(**employee.__dict__)
            for employee in EmployeeRepository(self.session).find_all()
        ]
