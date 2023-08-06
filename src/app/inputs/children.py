import strawberry

from app.types import Sex

__all__ = ["ChildCreateInput", "ChildUpdateInput"]


@strawberry.interface(description="")
class ChildInput:
    """
    Child の汎用 input
    """

    name: str
    age: int
    phone: str
    address: str
    parent: str
    sex: Sex
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
