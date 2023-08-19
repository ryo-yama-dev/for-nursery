import strawberry

from app.database import create_session
from app.inputs import (
    ChildCreateInput,
    ClassroomCreateInput,
    EmployeeCreateInput,
    EmployeeRecordCreateInput,
    JobCreateInput,
)
from app.services import (
    ChildService,
    ClassroomService,
    EmployeeRecordService,
    EmployeeService,
    JobService,
)
from app.types import Child, Classroom, Employee, EmployeeRecord, Job


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

    @strawberry.mutation
    def classroom_create(self, input: ClassroomCreateInput) -> Classroom:
        with create_session() as session:
            return ClassroomService(session).create(input)

    @strawberry.mutation
    def employee_record_create(
        self, input: EmployeeRecordCreateInput
    ) -> EmployeeRecord:
        with create_session() as session:
            return EmployeeRecordService(session).create(input)
