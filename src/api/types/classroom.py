import strawberry
from sqlmodel import Session

from api.repositories import *
from api.types import Child, Employee
from common.models import Classroom as ClassroomModel
from common.models import engine

__all__ = ["Classroom"]


@strawberry.experimental.pydantic.type(model=ClassroomModel)
class Classroom:
    """
    教室
    """

    id: strawberry.auto
    name: strawberry.auto

    def employees(self) -> list[Employee | None]:
        with Session(engine) as session:
            return EmployeeRepository(session).get_all()

    def children(self) -> list[Child | None]:
        with Session(engine) as session:
            return ChildRepository(session).get_all()
