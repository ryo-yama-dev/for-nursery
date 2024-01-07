import datetime

import strawberry

from .interfaces import Person, Status, Timestamp


@strawberry.type(description="園児")
class Child(Person, Timestamp):
    """
    園児
    """

    age: int
    phone: str
    address: str
    status: Status
    parent: str
    classroom_id: int | None = None


@strawberry.type(description="登退園記録")
class ChildTimeline:
    """
    登退園タイムライン
    """

    child_id: int
    date: datetime.date
    time: datetime.time
    event: Status
