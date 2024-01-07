import datetime

import strawberry

from .interfaces import Person, Timestamp
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

    serial_number: str
    auth_id: str | None = None
    belong: bool
    job_id: int
    job: Job
    profiles: list[Profile] | None = None
    classroom_id: int | None = None


@strawberry.type(description="従業員記録")
class EmployeeRecord:
    """
    従業員記録
    """

    id: int
    date: datetime.date
    attend_time: datetime.time
    leave_time: datetime.time | None = None
    note: str
    edited: bool
    employee_id: int


@strawberry.type(description="")
class EmployeeRecordDaily:
    """
    日次従業員記録
    """

    employee: Employee
    records: list[EmployeeRecord | None]
