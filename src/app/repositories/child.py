from typing import Any

from sqlalchemy import ScalarResult, insert, select

from app.common import dict_exclude_none
from app.database import ChildModel
from app.repositories import BaseRepository

__all__ = ["ChildRepository"]


class ChildRepository(BaseRepository):
    """
    園児
    """

    def find_all(self) -> ScalarResult[ChildModel]:
        stmt = select(ChildModel)
        return self.session.scalars(stmt)

    def find_by_id(self, id: int) -> ChildModel | None:
        return self.session.scalar(select(ChildModel).where(ChildModel.id == id))

    def create(
        self,
        kwargs: dict[str, Any] = {},
    ) -> ChildModel:
        input: dict[str, Any] = dict_exclude_none(kwargs)
        child = self.session.execute(
            insert(ChildModel).values(**input).returning(ChildModel)
        )
        self.session.commit()
        return child.scalar_one()
