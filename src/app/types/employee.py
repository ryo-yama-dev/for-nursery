import strawberry

from .interfaces import Person, Record, Timestamp
from .job import Job

__all__ = [
    "Employee",
    "EmployeeRecord",
    "EmployeeRecordDaily",
]


@strawberry.type(description="プロフィール")
class Profile:
    """
    プロフィール
    """

    id: int
    headline: str
    letter: str


@strawberry.type(description="従業員")
class Employee(Person, Timestamp):
    """
    従業員
    """

    auth_id: str | None = None
    belong: bool
    job_id: int
    job: Job
    profiles: list[Profile] | None = None
    classroom_id: int | None = None


@strawberry.type(description="従業員記録")
class EmployeeRecord(Record):
    """
    従業員記録
    """

    employee_id: int


@strawberry.type(description="")
class EmployeeRecordDaily:
    """
    日次従業員記録
    """

    employee: Employee
    records: list[EmployeeRecord | None]
