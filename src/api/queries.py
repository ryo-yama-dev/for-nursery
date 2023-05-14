import strawberry
from sqlmodel import Session

from common.models import engine

from .repositories import *
from .types import *


@strawberry.type
class Query:
    @strawberry.field
    def jobs(self) -> list[Job | None]:
        with Session(engine) as session:
            return JobRepository(session).get_all()

    @strawberry.field
    def employees(self) -> list[Employee | None]:
        with Session(engine) as session:
            return EmployeeRepository(session).get_all()

    @strawberry.field
    def children(self) -> list[Child | None]:
        with Session(engine) as session:
            return ChildRepository(session).get_all()

    @strawberry.field
    def classrooms(self) -> list[Classroom | None]:
        with Session(engine) as session:
            return ClassroomRepository(session).get_all()
