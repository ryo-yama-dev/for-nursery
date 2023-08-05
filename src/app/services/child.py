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
