import strawberry

__all__ = ["Child"]


@strawberry.type
class Child:
    """
    園児
    """

    id: int
    name: str
    age: int
    sex: str
    phone: str
    address: str
    parent: int
