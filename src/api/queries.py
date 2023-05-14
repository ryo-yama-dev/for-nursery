import strawberry
from sqlmodel import Session, select

from .types import *
from common.models import Job as JobModel, engine


@strawberry.type
class Query:
    @strawberry.field
    def jobs(self) -> list[Job | None]:
        with Session(engine) as session:
            statement = select(JobModel)
            results = session.exec(statement)
            # return [Job(row) for row in results.all()]
            return results.all()

