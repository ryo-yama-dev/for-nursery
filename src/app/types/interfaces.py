import datetime
from enum import Enum

import strawberry

from app.database import SexEnum

__all__ = ["Person", "Record", "Sex", "Timestamp"]


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
    MALE = SexEnum.male
    FEMALE = SexEnum.female


@strawberry.interface(description="タイムスタンプ")
class Timestamp:
    """
    タイムスタンプ
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime


@strawberry.interface(description="人物基本情報")
class Person:
    """
    人物基本情報
    """

    id: int
    first_name: str
    last_name: str
    sex: Sex
