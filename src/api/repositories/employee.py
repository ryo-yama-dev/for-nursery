from sqlmodel import Session, select

from common.models import Employee

__all__ = ["Employee"]


class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Employee]:
        return self.session.exec(select(Employee)).all()
