from sqlalchemy import ScalarResult, select

from app.database import EmployeeModel
from app.repositories import BaseRepository

__all__ = ["EmployeeRepository"]


class EmployeeRepository(BaseRepository):
    """
    従業員
    """

    def find_all(self) -> ScalarResult[EmployeeModel]:
        stmt = select(EmployeeModel)
        return self.session.scalars(stmt)

    def find_by_id(self, id: int) -> EmployeeModel | None:
        return self.session.scalar(select(EmployeeModel).where(EmployeeModel.id == id))
