import strawberry

from common.models import Child as ChildModel

__all__ = ["Child"]


@strawberry.experimental.pydantic.type(model=ChildModel)
class Child:
    """
    園児
    """
    id: strawberry.auto
    name: strawberry.auto
    age: strawberry.auto
    sex: strawberry.auto
    phone: strawberry.auto
    address: strawberry.auto
    parent: strawberry.auto
