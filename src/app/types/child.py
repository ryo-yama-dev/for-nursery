import strawberry

from .interaces import Record, Sex, Timestamp

__all__ = ["Child", "ChildRecord"]


@strawberry.type(description="園児")
class Child(Timestamp):
    """
    園児
    """

    id: int
    name: str
    age: int
    sex: Sex
    phone: str
    address: str
    parent: str


@strawberry.type(description="登退園記録")
class ChildRecord(Record):
    """
    登退園記録
    """

    child: Child
