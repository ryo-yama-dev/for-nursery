import datetime
from enum import Enum

import strawberry

from app.database import SexEnum, StatusEnum


@strawberry.enum(description="性別")
class Sex(Enum):
    MALE = SexEnum.male
    FEMALE = SexEnum.female


@strawberry.enum(description="在内・在外")
class Status(Enum):
    not_come = StatusEnum.not_come
    attend = StatusEnum.attend
    leave = StatusEnum.leave
    absence = StatusEnum.absence
    outing = StatusEnum.outing


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
    birthday: datetime.date
