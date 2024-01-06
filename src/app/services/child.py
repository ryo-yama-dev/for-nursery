import strawberry

from app.database import ChildModel
from app.inputs import ChildCreateInput
from app.repositories import ChildRepository
from app.types import Child

from .base import BaseService

__all__ = ["ChildService"]


class ChildService(BaseService):
    """
    園児データの操作用ロジック
    """

    @staticmethod
    def _data_format(data: ChildModel) -> Child:
        """
        ChildModel を Child に変換する
        """
        return Child(**data.to_dict())

    def find_all(self) -> list[Child]:
        return [
            self._data_format(child)
            for child in ChildRepository(self.session).find_all()
        ]

    def find_one(self, id: int) -> Child | None:
        child = ChildRepository(self.session).find_by_id(id=id)
        return self._data_format(child) if child else None

    def create(self, input: ChildCreateInput) -> Child:
        child = ChildRepository(self.session).create(
            (strawberry.asdict(input) | {"sex": input.sex.value})
        )
        return self._data_format(child)
