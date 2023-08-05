from app.inputs import JobCreateInput
from app.repositories import JobRepository
from app.types import Job

from .base import BaseService

__all__ = ["JobService"]


class JobService(BaseService):
    def find_all(self) -> list[Job]:
        return [Job(**job.to_dict()) for job in JobRepository(self.session).find_all()]

    def create(self, input: JobCreateInput) -> Job:
        job = JobRepository(self.session).create(name=input.name, rank=input.rank)
        return Job(**job.to_dict())
