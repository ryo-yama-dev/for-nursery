import strawberry

from .interaces import Record, Sex, Timestamp
from .job import Job

__all__ = ["Employee", "EmployeeRecord"]


@strawberry.type(description="プロフィール")
class Profile:
    """
    プロフィール
    """

    id: int
    order: int
    headline: str
    letter: str


@strawberry.type(description="従業員")
class Employee(Timestamp):
    """
    従業員
    """

    id: int
    auth_id: str | None
    name: str
    sex: Sex
    belong: bool
    job: Job
    profiles: list[Profile]


@strawberry.type(description="従業員記録")
class EmployeeRecord(Record):
    """
    従業員記録
    """

    employee: Employee
