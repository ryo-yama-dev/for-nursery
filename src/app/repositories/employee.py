from typing import Any

from sqlalchemy import ScalarResult, insert, select

from app.common import dict_exclude_none
from app.database import EmployeeModel
from app.repositories import BaseRepository

__all__ = ["EmployeeRepository"]


class EmployeeRepository(BaseRepository):
    """
    従業員
    """

    def find_all(self, **kwargs: Any) -> ScalarResult[EmployeeModel]:
        """
        条件を指定して従業員を全取得
        """
        stmt = select(EmployeeModel).filter_by(**kwargs)
        return self.session.scalars(stmt)

    def find_by_id(self, id: int) -> EmployeeModel | None:
        return self.session.scalar(select(EmployeeModel).where(EmployeeModel.id == id))

    def create(
        self,
        kwargs: dict[str, Any] = {},
    ) -> EmployeeModel:
        input: dict[str, Any] = dict_exclude_none(kwargs)
        employee = self.session.execute(
            insert(EmployeeModel).values(**input).returning(EmployeeModel)
        )
        self.session.commit()
        return employee.scalar_one()
