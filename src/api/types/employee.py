import strawberry
from sqlmodel import Session

from api.repositories import *
from api.types import Job
from common.models import Employee as EmployeeModel
from common.models import engine

__all__ = ["Employee"]


@strawberry.experimental.pydantic.type(model=EmployeeModel)
class Employee:
    """
    従業員
    """

    id: strawberry.auto
    auth_id: strawberry.auto
    name: strawberry.auto
    belong: strawberry.auto

    def jobs(self) -> list[Job | None]:
        with Session(engine) as session:
            return JobRepository(session).get_all()
