import strawberry

from .common import PersonInput

__all__ = ["ProfileInput", "EmployeeCreateInput", "EmployeeUpdateInput"]


@strawberry.input(description="")
class EmployeeInput(PersonInput):
    """
    従業員の汎用 input
    """

    belong: bool
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

    serial_number: str
    profiles: list[ProfileInput] | None = None


@strawberry.input(description="")
class EmployeeUpdateInput(EmployeeInput):
    """
    従業員の更新用 input
    """

    profiles: list[ProfileInput]
