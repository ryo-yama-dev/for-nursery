import strawberry

__all__ = ["JobCreateInput", "JobUpdateInput"]


@strawberry.input(description="Job の汎用 input")
class JobInput:
    """
    Job の汎用 input
    """

    name: str
    rank: int


@strawberry.input(description="職級の新規作成用 input")
class JobCreateInput(JobInput):
    """
    職級の新規作成用 input
    """

    pass


@strawberry.input(description="職級の更新用 input")
class JobUpdateInput(JobInput):
    """
    職級の更新用 input
    """

    pass
