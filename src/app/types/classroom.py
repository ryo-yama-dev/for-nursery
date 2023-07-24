import strawberry

__all__ = ["Classroom"]


@strawberry.type
class Classroom:
    """
    教室
    """

    id: strawberry.auto
    name: strawberry.auto
    # TODO: add more fields
