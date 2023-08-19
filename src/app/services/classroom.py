import strawberry

from app.database import ClassroomModel
from app.inputs import ClassroomCreateInput
from app.repositories import ClassroomRepository
from app.types import Child, Classroom, Employee, Job, Profile

from .base import BaseService

__all__ = ["ClassroomService"]


class ClassroomService(BaseService):
    """
    子供部屋の操作用ロジック
    """

    @staticmethod
    def _data_format(data: ClassroomModel) -> Classroom:
        """
        ClassroomModel を Classroom に変換する
        """
        return Classroom(
            **data.to_dict(),
            employees=[
                Employee(
                    **employee.to_dict(),
                    profiles=[Profile(**prof.to_dict()) for prof in employee.profiles],
                    job=Job(**employee.job.to_dict()),
                )
                for employee in data.employees
            ],
            children=[Child(**child.to_dict()) for child in data.children],
        )

    def find_all(self) -> list[Classroom]:
        return [
            self._data_format(classroom)
            for classroom in ClassroomRepository(self.session).find_all()
        ]

    def find_one(self, id: int) -> Classroom | None:
        classroom = ClassroomRepository(self.session).find_by_id(id=id)
        return self._data_format(classroom) if classroom else None

    def create(self, input: ClassroomCreateInput) -> Classroom:
        classroom = ClassroomRepository(self.session).create(strawberry.asdict(input))
        return self._data_format(classroom)
