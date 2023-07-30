import strawberry

from .child import Child
from .employee import Employee

__all__ = ["Classroom"]


@strawberry.type(description="子供組")
class Classroom:
    """
    教室
    """

    id: int
    name: str
    age: int
    children: list[Child]
    employees: list[Employee]
