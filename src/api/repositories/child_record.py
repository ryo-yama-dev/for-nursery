from sqlmodel import Session, select

from common.models import ChildRecord

__all__ = ["ChildRecordRepository"]


class ChildRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[ChildRecord]:
        return self.session.exec(select(ChildRecord)).all()
