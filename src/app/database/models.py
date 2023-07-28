import datetime
import os
import re
from enum import Enum

from dotenv import load_dotenv
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Time,
    create_engine,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    Session,
    declared_attr,
    mapped_column,
    relationship,
    sessionmaker,
)

load_dotenv()
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
user_password = f"{postgres_user}:{postgres_password}"
postgres_host = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")
host_port = f"{postgres_host}:{postgres_port}"
engine = create_engine(f"postgresql+psycopg://{user_password}@{host_port}/postgres")

__all__ = [
    "engine",
    "create_session",
    "JobModel",
    "ClassroomModel",
    "ChildModel",
    "EmployeeModel",
    "ProfileModel",
    "ChildRecordModel",
    "EmployeeRecordModel",
    "SexEnum",
    "Record",
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


class SexEnum(Enum):
    """
    性別
    """

    MALE = "男性"
    FEMALE = "女性"


class JobModel(Base, TimestampMixin):
    """
    職種・職級
    """

    name: Mapped[str] = mapped_column(String, nullable=False, comment="職種名")
    rank: Mapped[int] = mapped_column(Integer, nullable=False, comment="職級")
    employees: Mapped[list["EmployeeModel"]] = relationship(
        "EmployeeModel",
        back_populates="job",
        default=None,
    )


class ChildModel(Base, TimestampMixin):
    """
    園児
    """

    name: Mapped[str] = mapped_column(String, comment="氏名")
    age: Mapped[int] = mapped_column(Integer, comment="年齢")
    sex: Mapped[SexEnum]
    phone: Mapped[str] = mapped_column(String, comment="連絡先電話番号")
    address: Mapped[str] = mapped_column(String, comment="連絡先住所")
    parent: Mapped[str] = mapped_column(String, comment="保護者")
    classroom_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("classroom.id"), comment="教室", default=None
    )
    classroom: Mapped["ClassroomModel"] = relationship(
        "ClassroomModel", back_populates="children", default=None
    )
    records: Mapped[list["ChildRecordModel"]] = relationship(
        "ChildRecordModel",
        back_populates="child",
        default=None,
    )


class EmployeeModel(Base, TimestampMixin):
    """
    従業員
    """

    name: Mapped[str] = mapped_column(String, comment="氏名")
    belong: Mapped[bool] = mapped_column(Boolean, comment="在職中か否か")
    sex: Mapped[SexEnum]
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey("job.id"))
    job: Mapped[JobModel] = relationship(
        "JobModel", back_populates="employees", default=None
    )
    profiles: Mapped[list["ProfileModel"]] = relationship(
        "ProfileModel", back_populates="employee", default=None
    )
    auth_id: Mapped[str | None] = mapped_column(String, default=None, comment="認証ID")
    classroom_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("classroom.id"), comment="教室", default=None
    )
    classroom: Mapped["ClassroomModel"] = relationship(
        "ClassroomModel", back_populates="employees", default=None
    )
    records: Mapped[list["EmployeeRecordModel"]] = relationship(
        "EmployeeRecordModel",
        back_populates="employee",
        default=None,
    )


class ProfileModel(Base):
    """
    固有プロフィール
    """

    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employee.id"), comment="紐づけられている従業員のID"
    )
    employee: Mapped[EmployeeModel] = relationship(
        "EmployeeModel", back_populates="profiles"
    )
    order: Mapped[int] = mapped_column(Integer, comment="並び順")
    headline: Mapped[str] = mapped_column(String, comment="見出し")
    letter: Mapped[str | None] = mapped_column(String, comment="本文")


class ClassroomModel(Base):
    """
    クラス
    """

    name: Mapped[str] = mapped_column(String, unique=True, comment="組名")
    age: Mapped[int] = mapped_column(Integer, comment="年齢")
    employees: Mapped[list[EmployeeModel]] = relationship(
        "EmployeeModel", back_populates="classroom", default=None
    )
    children: Mapped[list[ChildModel]] = relationship(
        "ChildModel", back_populates="classroom", default=None
    )


class Record:
    """
    日毎の記録
    """

    date: Mapped[datetime.date] = mapped_column(Date, comment="日付")
    attend_time: Mapped[datetime.time] = mapped_column(Time, comment="登園時間")
    leave_time: Mapped[datetime.time] = mapped_column(Time, comment="退園時間")
    note: Mapped[str | None] = mapped_column(String, comment="備考")
    edited: Mapped[bool] = mapped_column(Boolean, default=False, comment="編集済みか否か")


class ChildRecordModel(Base, Record):
    """
    園児記録
    """

    child_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("child.id"), default=None, comment="園児"
    )
    child: Mapped[ChildModel] = relationship(
        "ChildModel", default=None, back_populates="records"
    )
    # date: Mapped[datetime.date] = mapped_column(Date, comment="日付")
    # attend_time: Mapped[datetime.time] = mapped_column(Time, comment="登園時間")
    # leave_time: Mapped[datetime.time] = mapped_column(Time, comment="退園時間")
    # note: Mapped[str | None] = mapped_column(String, comment="備考")
    # edited: Mapped[bool] = mapped_column(Boolean, default=False, comment="編集済みか否か")


class EmployeeRecordModel(Base, Record):
    """
    従業員記録
    """

    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employee.id"), default=None, comment="従業員"
    )
    employee: Mapped[EmployeeModel] = relationship(
        "EmployeeModel", default=None, back_populates="records"
    )
    # date: Mapped[datetime.date] = mapped_column(Date, comment="日付")
    # attend_time: Mapped[datetime.time] = mapped_column(Time, comment="出勤時間")
    # leave_time: Mapped[datetime.time] = mapped_column(Time, comment="退勤時間")
    # note: Mapped[str | None] = mapped_column(String, comment="備考")
    # edited: Mapped[bool] = mapped_column(Boolean, default=False, comment="編集済みか否か")


postgre_url = f"postgresql+psycopg://{user_password}@{host_port}/postgres"

engine = create_engine(postgre_url)


def create_session() -> Session:
    """
    セッションを作成
    """

    return sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    )()
