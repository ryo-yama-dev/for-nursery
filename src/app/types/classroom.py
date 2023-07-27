import strawberry

__all__ = ["Classroom"]


@strawberry.type
class Classroom:
    """
    教室
    """

    id: int
    name: str
    # TODO: add more fields
