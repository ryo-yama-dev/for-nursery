from sqlalchemy import ScalarResult, select

from app.database import ChildRecordModel
from app.repositories import BaseRepository

__all__ = ["ChildRecordRepository"]


class ChildRecordRepository(BaseRepository):
    """
    園児記録
    """

    def find_all(self) -> ScalarResult[ChildRecordModel]:
        stmt = select(ChildRecordModel)
        return self.session.scalars(stmt)
