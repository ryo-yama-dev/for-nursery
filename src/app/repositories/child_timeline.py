from sqlalchemy import ScalarResult, select

from app.database import ChildTimelineModel
from app.repositories import BaseRepository


class ChildTimelineRepository(BaseRepository):
    """
    園児記録
    """

    def find_all(self) -> ScalarResult[ChildTimelineModel]:
        stmt = select(ChildTimelineModel)
        return self.session.scalars(stmt)
