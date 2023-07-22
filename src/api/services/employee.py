from api.repositories import EmployeeRepository
from api.types import Employee

from .base import BaseService

__all__ = ["EmployeeService"]


class EmployeeService(BaseService):
    """ """

    def get_all(self) -> list[Employee]:
        return [
            Employee(**employee.__dict__)
            for employee in EmployeeRepository(self.session).get_all()
        ]
