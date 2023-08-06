from app.repositories import ChildRepository
from app.types import Child

from .base import BaseService

__all__ = ["ChildService"]


class ChildService(BaseService):
    def find_all(self) -> list[Child]:
        return [
            Child(**child.to_dict())
            for child in ChildRepository(self.session).find_all()
        ]

    def find_one(self, id: int) -> Child | None:
        child = ChildRepository(self.session).find_by_id(id=id)
        return Child(**child.to_dict()) if child else None
