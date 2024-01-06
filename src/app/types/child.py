import strawberry

from .interfaces import Person, Record, Timestamp

__all__ = ["Child", "ChildRecord"]


@strawberry.type(description="園児")
class Child(Person, Timestamp):
    """
    園児
    """

    age: int
    phone: str
    address: str
    parent: str
    classroom_id: int | None = None


@strawberry.type(description="登退園記録")
class ChildRecord(Record):
    """
    登退園記録
    """

    child: Child
