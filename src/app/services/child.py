from app.repositories import ChildRepository
from app.types import Child

from .base import BaseService

__all__ = ["ChildService"]


class ChildService(BaseService):
    def get_all(self) -> list[Child]:
        return [
            Child(**child.__dict__) for child in ChildRepository(self.session).get_all()
        ]