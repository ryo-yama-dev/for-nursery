from sqlmodel import Session, select

from common.models import Classroom

__all__ = ["ClassroomRepository"]


class ClassroomRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Classroom]:
        return self.session.exec(select(Classroom)).all()
