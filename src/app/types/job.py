import strawberry

__all__ = ["Job"]


@strawberry.type
class Job:
    """
    職種
    """

    id: int
    name: str
    rank: int
