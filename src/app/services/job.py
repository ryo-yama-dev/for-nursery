from app.repositories import JobRepository
from app.types import Job

from .base import BaseService

__all__ = ["JobService"]


class JobService(BaseService):
    def get_all(self) -> list[Job]:
        return [Job(**job.__dict__) for job in JobRepository(self.session).get_all()]