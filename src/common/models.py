import datetime
import os
import re

from dotenv import load_dotenv
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    Time,
    create_engine,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    declared_attr,
    mapped_column,
    relationship,
)

load_dotenv()
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
user_password = f"{postgres_user}:{postgres_password}"
postgres_host = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")
host_port = f"{postgres_host}:{postgres_port}"

__all__ = [
    "engine",
    "JobModel",
    "ClassroomModel",
    "ChildModel",
    "EmployeeModel",
    "ProfileModel",
    "ChildRecordModel",
    "EmployeeRecordModel",
]


def pascal_to_snake_tablename(tablename: str) -> str:
    """
    パスカルケースのモデル名をスネークケースに変換し、末尾の"Model"を除外する
    ※実際の DB のテーブル物理名がスネークケースであることが前提
    """

    blocks = [
        block.group(0).lower() for block in re.finditer(r"[A-Za-z][^A-Z]+", tablename)
    ]
    blocks.pop()
    if len(blocks) > 1:
        result = blocks.pop(0)
        for block in blocks:
            result += f"_{block}"
        return result
    return blocks[0]


class Base(DeclarativeBase, MappedAsDataclass):
    """
    全 Model の基底クラス
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        クラス名から "Model" を除外してスネークケースの tablename に
        """

        return pascal_to_snake_tablename(cls.__name__)

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, unique=True, nullable=False, init=False
    )


class TimestampMixin:
    """
    タイムスタンプのクラス
    """

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), server_default=func.current_timestamp(), nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), server_default=func.current_timestamp(), nullable=False
    )


class JobModel(Base, TimestampMixin):
    """
    職種・職級
    """

    name: Mapped[str] = mapped_column(String, nullable=False, description="職種名")
    rank: Mapped[int] = mapped_column(Integer, nullable=False, description="職級")


class ChildModel(Base, TimestampMixin):
    """
    園児
    """

    name: Mapped[str] = mapped_column(String, description="氏名")
    age: Mapped[int] = mapped_column(Integer, description="年齢")
    sex: Mapped[str] = mapped_column(String, description="性別")
    phone: Mapped[str] = mapped_column(String, description="連絡先電話番号")
    address: Mapped[str] = mapped_column(String, description="連絡先住所")
    parent: Mapped[str] = mapped_column(String, description="保護者")


class EmployeeModel(Base, TimestampMixin):
    """
    従業員
    """

    __table_args__ = (PrimaryKeyConstraint("id", name="employee_pkey"),)

    name: Mapped[str] = mapped_column(String, description="氏名")
    belong: Mapped[bool] = mapped_column(Boolean, description="在職中か否か")
    # TODO: 単独に変える
    jobs: Mapped[list[int]] = mapped_column(description="職種")
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey("job.id"))
    job: Mapped[JobModel] = relationship(
        JobModel, back_populates="employee", default=None
    )
    auth_id: Mapped[str] = mapped_column(default=None, description="認証ID")


class ProfileModel(Base):
    """
    固有プロフィール
    """

    person_id: Mapped[int] = mapped_column(
        Integer, description="紐づけられているEmployeeもしくはChildのID"
    )
    headline: Mapped[str] = mapped_column(String, description="見出し")
    letter: Mapped[str | None] = mapped_column(String, description="本文")


class ClassroomModel(Base):
    """
    クラス
    """

    name: Mapped[str] = mapped_column(String, unique=True, description="組名")
    age: Mapped[int] = mapped_column(Integer, description="年齢")
    employees: Mapped[list[int]] = mapped_column(description="担当従業員")
    children: Mapped[list[int]] = mapped_column(description="所属園児")


class ChildRecordModel(Base):
    """
    園児記録
    """

    child_id: Mapped[int | None] = mapped_column(
        Integer, description="園児", foreign_key="child.id"
    )
    date: Mapped[datetime.date] = mapped_column(Date, description="日付")
    attend_time: Mapped[datetime.time] = mapped_column(Time, description="登園時間")
    leave_time: Mapped[datetime.time] = mapped_column(Time, description="退園時間")
    note: Mapped[str | None] = mapped_column(String, description="備考")
    edited: Mapped[bool] = mapped_column(Boolean, default=False, description="編集済みか否か")


class EmployeeRecordModel(Base):
    """
    従業員記録
    """

    employee_id: Mapped[int] | None = mapped_column(
        Integer, description="従業員", foreign_key="employee.id"
    )
    date: Mapped[datetime.date] = mapped_column(Date, description="日付")
    attend_time: Mapped[datetime.time] = mapped_column(Time, description="出勤時間")
    leave_time: Mapped[datetime.time] = mapped_column(Time, description="退勤時間")
    note: Mapped[str | None] = mapped_column(String, description="備考")
    edited: Mapped[bool] = mapped_column(Boolean, default=False, description="編集済みか否か")


postgre_url = f"postgresql+psycopg://{user_password}@{host_port}/postgres"

engine = create_engine(postgre_url)
