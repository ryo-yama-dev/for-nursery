import datetime

import strawberry

from app.types import Status


@strawberry.input(description="")
class RecordInput:
    """
    Record の汎用 input
    """

    date: datetime.date
    attend_time: datetime.time
    leave_time: datetime.time | None = None


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
class EmployeeRecordCreateInput(RecordInput):
    """
    EmployeeRecord 登録用 input
    """

    employee_id: int


@strawberry.input(description="")
class EmployeeRecordUpdateInput(RecordInput):
    """
    EmployeeRecord 更新用 input
    """

    leave_time: datetime.time
