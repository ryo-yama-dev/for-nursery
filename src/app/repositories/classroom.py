from sqlalchemy import ScalarResult, select

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
