from sqlalchemy.orm import Session

__all__ = ["BaseService"]


class BaseService:
    """
    業務処理クラスの基底クラス
    """

    session: Session

    def __init__(self, session: Session):
        self.session = session
