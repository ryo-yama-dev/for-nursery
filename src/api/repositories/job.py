from sqlmodel import Session, select

from common.models import Job

__all__ = ["JobRepository"]


class JobRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Job]:
        return self.session.exec(select(Job)).all()
