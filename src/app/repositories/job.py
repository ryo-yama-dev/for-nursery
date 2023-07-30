from sqlalchemy import ScalarResult, insert, select
from sqlalchemy.orm import Session

from app.database import JobModel

__all__ = ["JobRepository"]


class JobRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> ScalarResult[JobModel]:
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
        print("test", job)
        return job.scalar_one()
