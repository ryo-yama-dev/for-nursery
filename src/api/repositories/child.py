from sqlmodel import Session, select

from common.models import Child

__all__ = ["ChildRepository"]


class ChildRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Child]:
        return self.session.exec(select(Child)).all()
