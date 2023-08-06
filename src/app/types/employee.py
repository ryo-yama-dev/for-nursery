import strawberry

from .interaces import Record, Timestamp
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
    sex: str
    belong: bool
    job_id: int
    job: Job
    profiles: list[Profile]
    classroom_id: int | None


@strawberry.type(description="従業員記録")
class EmployeeRecord(Record):
    """
    従業員記録
    """

    employee: Employee
