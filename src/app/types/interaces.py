import datetime
from enum import Enum

import strawberry

__all__ = ["Record", "Sex", "Timestamp"]


@strawberry.interface(description="日次記録")
class Record:
    """
    日次記録
    """

    id: int
    date: datetime.date
    attend_time: datetime.time
    leave_time: datetime.time
    note: str
    edited: bool


@strawberry.enum(description="性別")
class Sex(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


@strawberry.interface(description="タイムスタンプ")
class Timestamp:
    """
    タイムスタンプ
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
