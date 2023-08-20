import datetime

import strawberry

from .interaces import Record, Timestamp
from .job import Job

__all__ = ["Employee", "EmployeeRecord", "EmployeeDailyRecord"]


@strawberry.type(description="プロフィール")
class Profile:
    """
    プロフィール
    """

    id: int
    headline: str
    letter: str


@strawberry.type(description="従業員")
class Employee(Timestamp):
    """
    従業員
    """

    id: int
    auth_id: str | None = None
    name: str
    sex: str
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
    employee: Employee


@strawberry.type(description="日次従業員記録")
class EmployeeDailyRecord:
    """
    日次従業員記録
    """

    date: datetime.date
    records: list[EmployeeRecord]
