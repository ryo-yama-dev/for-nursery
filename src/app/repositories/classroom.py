from typing import Any

from sqlalchemy import ScalarResult, insert, select

from app.common import dict_exclude_none
from app.database import ClassroomModel
from app.repositories import BaseRepository

__all__ = ["ClassroomRepository"]


class ClassroomRepository(BaseRepository):
    """
    クラス
    """

    def find_all(self) -> ScalarResult[ClassroomModel]:
        stmt = select(ClassroomModel)
        return self.session.scalars(stmt)

    def find_by_id(self, id: int) -> ClassroomModel | None:
        return self.session.scalar(
            select(ClassroomModel).where(ClassroomModel.id == id)
        )

    def create(
        self,
        kwargs: dict[str, Any] = {},
    ) -> ClassroomModel:
        input: dict[str, Any] = dict_exclude_none(kwargs)
        classroom = self.session.execute(
            insert(ClassroomModel).values(**input).returning(ClassroomModel)
        )
        self.session.commit()
        return classroom.scalar_one()
