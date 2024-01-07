import strawberry

from app.types import Status

from .common import PersonInput


@strawberry.input(description="")
class ChildInput(PersonInput):
    """
    Child の汎用 input
    """

    age: int
    phone: str
    address: str
    parent: str
    status: Status
    classroom_id: int | None = None


@strawberry.input(description="")
class ChildCreateInput(ChildInput):
    """
    Child の新規作成用 input
    """

    pass


@strawberry.input(description="")
class ChildUpdateInput(ChildInput):
    """
    Child の更新用 input
    """

    pass
