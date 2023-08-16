from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from devtools import debug
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

__all__ = ["BaseRepository", "RepositoryError", "repository_error_handler"]

P = ParamSpec("P")
R = TypeVar("R")


class BaseRepository:
    """
    usecase に合わせて DB 操作処理を実装するための基底クラス
    """

    session: Session

    def __init__(self, session: Session):
        self.session = session


# TODO: エラーコード正式実装
class ErrorCode:
    """
    DB エラーコード
    """

    NOT_FOUND: str = "NOT_FOUND"

    @classmethod
    def _code(cls, message: str) -> str:
        if message == "":
            return cls.NOT_FOUND
        else:
            return ""

    @classmethod
    def _message(cls, code: str) -> str:
        if code == "":
            return cls.NOT_FOUND
        else:
            return ""


class RepositoryError(Exception):
    """
    DB 操作エラーにおける例外クラス
    """

    code: str
    message: str
    location: list[str | int]

    def __init__(self, message: str, location: list[str | int]):
        self.message = message
        self.location = location
        self.code = ErrorCode._code(message)


# TODO: デバッグ用引数追加
def repository_error_handler(
    func_name: str,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Repository 例外ハンドラー
    """

    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except SQLAlchemyError as sql_e:
                debug(func.__class__)
                # TODO: 呼び出し元に UserError を渡したい
                raise RepositoryError(message=sql_e._message(), location=[])

        return inner

    return wrapper
