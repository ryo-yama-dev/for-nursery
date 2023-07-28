from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from app.database import EmployeeModel

__all__ = ["EmployeeRepository"]


class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> ScalarResult[EmployeeModel]:
        stmt = select(EmployeeModel)
        return self.session.scalars(stmt)
