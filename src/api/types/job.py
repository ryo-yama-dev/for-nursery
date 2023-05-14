import strawberry

from common.models import Job as JobModel

__all__ = ["Job"]


@strawberry.experimental.pydantic.type(model=JobModel)
class Job:
    """
    職種
    """

    id: strawberry.auto
    name: strawberry.auto
    rank: strawberry.auto
