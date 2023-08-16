from sqlalchemy.orm import Session

__all__ = ["BaseRepository"]


class BaseRepository:
    """
    usecase に合わせて DB 操作処理を実装するための基底クラス
    """

    session: Session

    def __init__(self, session: Session):
        self.session = session
