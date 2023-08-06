import strawberry

from app.database import create_session
from app.services import ChildService, ClassroomService, EmployeeService, JobService
from app.types import Child, Classroom, Employee, Job


@strawberry.type
class Query:
    @strawberry.field(description="職級一覧取得")
    def jobs(self) -> list[Job]:
        with create_session() as session:
            return JobService(session).find_all()

    @strawberry.field(description="従業員一覧取得")
    def employees(self) -> list[Employee]:
        with create_session() as session:
            return EmployeeService(session).find_all()

    @strawberry.field(description="従業員1件取得")
    def employee(self, id: int) -> Employee | None:
        with create_session() as session:
            return EmployeeService(session).find_one(id=id)

    @strawberry.field(description="園児一覧取得")
    def children(self) -> list[Child]:
        with create_session() as session:
            return ChildService(session).find_all()

    @strawberry.field(description="園児1件取得")
    def child(self, id: int) -> Child | None:
        with create_session() as session:
            return ChildService(session).find_one(id=id)

    @strawberry.field(description="子供部屋一覧取得")
    def classrooms(self) -> list[Classroom]:
        with create_session() as session:
            return ClassroomService(session).find_all()

    @strawberry.field(description="子供部屋1件取得")
    def classroom(self, id: int) -> Classroom | None:
        with create_session() as session:
            return ClassroomService(session).find_one(id=id)
