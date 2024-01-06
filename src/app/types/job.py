import strawberry

from .interfaces import Timestamp

__all__ = ["Job"]


@strawberry.type(description="職級")
class Job(Timestamp):
    """
    職種
    """

    id: int
    name: str
    rank: int
