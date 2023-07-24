from sqlalchemy import ScalarResult, select
from sqlalchemy.orm import Session

from app.common.models import JobModel

__all__ = ["JobRepository"]


class JobRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> ScalarResult[JobModel]:
        stmt = select(JobModel)
        return self.session.scalars(stmt)
