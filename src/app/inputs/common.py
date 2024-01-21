import datetime

import strawberry

from app.types import Sex


@strawberry.input(description="人物設定用の共通 input")
class PersonInput:
    """
    人物設定の汎用 input
    """

    first_name: str
    last_name: str
    sex: Sex
    birthday: datetime.date
