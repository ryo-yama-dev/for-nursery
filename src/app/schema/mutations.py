import strawberry

from app.database import create_session
from app.inputs import ChildCreateInput, JobCreateInput
from app.services import ChildService, JobService
from app.types import Child, Job


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
