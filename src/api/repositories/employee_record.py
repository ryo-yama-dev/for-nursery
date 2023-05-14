from sqlmodel import Session, select

from common.models import EmployeeRecord

__all__ = ["EmployeeRecordRepository"]


class EmployeeRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[EmployeeRecord]:
        return self.session.exec(select(EmployeeRecord)).all()
