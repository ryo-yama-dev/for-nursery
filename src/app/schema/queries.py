import strawberry

from app.database import create_session
from app.services import ChildService, ClassroomService, EmployeeService, JobService
from app.types import Child, Classroom, Employee, Job


@strawberry.type
class Query:
    @strawberry.field
    def jobs(self) -> list[Job]:
        with create_session() as session:
            return JobService(session).find_all()

    @strawberry.field
    def employees(self) -> list[Employee]:
        with create_session() as session:
            return EmployeeService(session).find_all()

    @strawberry.field
    def children(self) -> list[Child]:
        with create_session() as session:
            return ChildService(session).find_all()

    @strawberry.field
    def classrooms(self) -> list[Classroom]:
        with create_session() as session:
            return ClassroomService(session).find_all()
