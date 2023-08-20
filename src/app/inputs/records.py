import datetime

import strawberry

__all__ = [
    "ChildRecordCreateInput",
    "ChildRecordUpdateInput",
    "EmployeeRecordCreateInput",
    "EmployeeRecordUpdateInput",
    "RecordsQueryInput",
]


@strawberry.input(description="")
class RecordInput:
    """
    Record の汎用 input
    """

    # TODO: attend と leave のどちらかだけを必須にする
    date: datetime.date
    attend_time: datetime.time
    leave_time: datetime.time


@strawberry.input(description="")
class RecordsQueryInput:
    """
    登退園記録の抽出 Query input
    """

    year: int
    month: int
    week: int | None = None


@strawberry.input(description="")
class ChildRecordCreateInput(RecordInput):
    pass


@strawberry.input(description="")
class ChildRecordUpdateInput(RecordInput):
    pass


@strawberry.input(description="")
class EmployeeRecordCreateInput(RecordInput):
    """
    EmployeeRecord 登録用 input
    """

    employee_id: int


@strawberry.input(description="")
class EmployeeRecordUpdateInput(RecordInput):
    pass
