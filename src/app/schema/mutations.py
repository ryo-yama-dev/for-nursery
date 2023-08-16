import strawberry

from app.database import create_session
from app.inputs import ChildCreateInput, EmployeeCreateInput, JobCreateInput
from app.services import ChildService, EmployeeService, JobService
from app.types import Child, Employee, Job


@strawberry.type
class Mutation:
    """
    Mutation
    """

    @strawberry.mutation
    def job_create(self, input: JobCreateInput) -> Job:
        with create_session() as session:
            return JobService(session).create(input)

    @strawberry.mutation
    def child_create(self, input: ChildCreateInput) -> Child:
        with create_session() as session:
            return ChildService(session).create(input)

    @strawberry.mutation
    def employee_create(self, input: EmployeeCreateInput) -> Employee:
        with create_session() as session:
            return EmployeeService(session).create(input)
