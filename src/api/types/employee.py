import strawberry

__all__ = ["Employee"]


@strawberry.type
class Employee:
    """
    従業員
    """

    id: int
    auth_id: str | None
    name: str
    belong: bool
    # TODO: 職級
