import strawberry

from app.database import create_session
from app.inputs import JobCreateInput
from app.services import JobService
from app.types import Job


@strawberry.type
class Mutation:
    """
    Mutation
    """

    @strawberry.mutation
    def job_create(self, input: JobCreateInput) -> Job:
        with create_session() as session:
            return JobService(session).create(input)
