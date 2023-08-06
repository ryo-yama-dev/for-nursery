from typing import Any

from sqlalchemy import ScalarResult, insert, select
from sqlalchemy.orm import Session

from app.database import ChildModel

__all__ = ["ChildRepository"]


class ChildRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> ScalarResult[ChildModel]:
        stmt = select(ChildModel)
        return self.session.scalars(stmt)

    def find_by_id(self, id: int) -> ChildModel | None:
        return self.session.scalar(select(ChildModel).where(ChildModel.id == id))

    def create(
        self,
        kwargs: dict[str, Any] = {},
    ) -> ChildModel:
        input: dict[str, Any] = {}
        for key, value in kwargs.items():
            if value is not None:
                input[key] = value
        print("create", input)
        child = self.session.execute(
            insert(ChildModel).values(**input).returning(ChildModel)
        )
        self.session.commit()
        return child.scalar_one()
