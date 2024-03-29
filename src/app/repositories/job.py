from sqlalchemy import ScalarResult, insert, select

from app.database import JobModel
from app.repositories import BaseRepository

__all__ = ["JobRepository"]


class JobRepository(BaseRepository):
    """
    職種
    """

    def find_all(self) -> ScalarResult[JobModel]:
        """
        職種・職級を全取得
        """
        stmt = select(JobModel)
        return self.session.scalars(stmt)

    def create(self, name: str, rank: int) -> JobModel:
        """
        職種・職級を作成
        """
        job = self.session.execute(
            insert(JobModel).values(name=name, rank=rank).returning(JobModel)
        )
        self.session.commit()
        return job.scalar_one()
