from api.repositories import ClassroomRepository
from api.types import Classroom

from .base import BaseService

__all__ = ["ClassroomService"]


class ClassroomService(BaseService):
    def get_all(self) -> list[Classroom]:
        return [
            Classroom(**classroom.__dict__)
            for classroom in ClassroomRepository(self.session).get_all()
        ]
