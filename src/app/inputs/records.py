import datetime

import strawberry

from app.types import Status


@strawberry.input(description="")
class RecordsQueryInput:
    """
    登退園記録の抽出 Query input
    """

    year: int
    month: int
    week: int | None = None


@strawberry.input(description="ChildTimeline 登録用 input")
class ChildTimelineCreateInput:
    """
    ChildTimeline 登録用 input
    """

    date: datetime.date
    time: datetime.time
    event: Status
    child_id: int


@strawberry.input(description="")
class EmployeeRecordInput:
    """
    Record の汎用 input
    """

    date: datetime.date
    employee_id: int


@strawberry.input(description="")
class EmployeeRecordCreateInput(EmployeeRecordInput):
    """
    EmployeeRecord 登録用 input
    """

    attend_time: datetime.time
    leave_time: datetime.time | None = None


@strawberry.input(description="")
class EmployeeRecordUpdateInput(EmployeeRecordInput):
    """
    EmployeeRecord 更新用 input
    """

    attend_time: datetime.time | None = None
    leave_time: datetime.time | None = None
    note: str | None = None
