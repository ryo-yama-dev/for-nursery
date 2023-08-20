import strawberry

from app.types import Sex

__all__ = ["ProfileInput", "EmployeeCreateInput", "EmployeeUpdateInput"]


@strawberry.input(description="")
class EmployeeInput:
    """
    従業員の汎用 input
    """

    name: str
    belong: bool
    sex: Sex
    job_id: int


@strawberry.input(description="")
class ProfileInput:
    """
    固有プロフィールの input
    """

    id: int | None = None
    headline: str
    letter: str | None = None


@strawberry.input(description="")
class EmployeeCreateInput(EmployeeInput):
    """
    従業員の新規作成用 input
    """

    profiles: list[ProfileInput] | None = None


@strawberry.input(description="")
class EmployeeUpdateInput(EmployeeInput):
    """
    従業員の更新用 input
    """

    profiles: list[ProfileInput]
