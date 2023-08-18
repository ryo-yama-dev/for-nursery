import strawberry

__all__ = ["ClassroomCreateInput", "ClassroomUpdateInput"]


@strawberry.interface(description="")
class ClassroomInput:
    """
    Classroom の汎用 input
    """

    name: str
    age: int


@strawberry.input(description="")
class ClassroomCreateInput(ClassroomInput):
    """
    Classroom の新規作成用 input
    """

    employee_ids: list[int] | None = None
    child_ids: list[int] | None = None


@strawberry.input(description="")
class ClassroomUpdateInput(ClassroomInput):
    """
    Classroom の更新用 input
    """

    employee_ids: list[int]
    child_ids: list[int]
