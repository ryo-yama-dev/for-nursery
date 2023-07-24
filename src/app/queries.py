import strawberry

from app.common.models import create_session

from .services import ChildService, ClassroomService, EmployeeService, JobService
from .types import Child, Classroom, Employee, Job


@strawberry.type
class Query:
    @strawberry.field
    def jobs(self) -> list[Job]:
        with create_session() as session:
            return JobService(session).get_all()

    @strawberry.field
    def employees(self) -> list[Employee]:
        with create_session() as session:
            return EmployeeService(session).get_all()

    @strawberry.field
    def children(self) -> list[Child]:
        with create_session() as session:
            return ChildService(session).get_all()

    @strawberry.field
    def classrooms(self) -> list[Classroom]:
        with create_session() as session:
            return ClassroomService(session).get_all()
