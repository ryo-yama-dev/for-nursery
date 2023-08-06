from app.repositories import ClassroomRepository
from app.types import Child, Classroom, Employee, Job, Profile

from .base import BaseService

__all__ = ["ClassroomService"]


class ClassroomService(BaseService):
    def find_all(self) -> list[Classroom]:
        return [
            Classroom(
                **classroom.to_dict(),
                employees=[
                    Employee(
                        **employee.to_dict(),
                        profiles=[
                            Profile(**prof.to_dict()) for prof in employee.profiles
                        ],
                        job=Job(**employee.job.to_dict()),
                    )
                    for employee in classroom.employees
                ],
                children=[Child(**child.to_dict()) for child in classroom.children],
            )
            for classroom in ClassroomRepository(self.session).find_all()
        ]

    def find_one(self, id: int) -> Classroom | None:
        classroom = ClassroomRepository(self.session).find_by_id(id=id)
        return (
            Classroom(
                **classroom.to_dict(),
                employees=[
                    Employee(
                        **employee.to_dict(),
                        profiles=[
                            Profile(**prof.to_dict()) for prof in employee.profiles
                        ],
                        job=Job(**employee.job.to_dict()),
                    )
                    for employee in classroom.employees
                ],
                children=[Child(**child.to_dict()) for child in classroom.children],
            )
            if classroom
            else None
        )
