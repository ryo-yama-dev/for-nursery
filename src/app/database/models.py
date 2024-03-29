import copy
import datetime
import enum
import os
import re
from typing import Any

from dotenv import load_dotenv
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum,
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
    "SexEnum",
    "StatusEnum",
    "JobModel",
    "ClassroomModel",
    "ChildModel",
    "EmployeeModel",
    "ProfileModel",
    "ChildTimelineModel",
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

    def to_dict(self) -> dict[str, Any]:
        """
        _sa_instance_state を削除した上でデータクラスを辞書に変換する
        """
        cp_dict = copy.deepcopy(self.__dict__)
        cp_dict.pop("_sa_instance_state", None)
        return cp_dict


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


class SexEnum(enum.Enum):
    """
    性別の列挙値
    """

    male = "男"
    female = "女"


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


class StatusEnum(enum.Enum):
    """
    在内・在外ステータスの列挙値
    """

    not_come = 1
    attend = 2
    leave = 3
    absence = 4
    outing = 5


class ChildModel(Base, TimestampMixin):
    """
    園児
    """

    first_name: Mapped[str] = mapped_column(String, comment="名")
    last_name: Mapped[str] = mapped_column(String, comment="姓")
    birthday: Mapped[datetime.date] = mapped_column(Date, comment="誕生日")
    sex: Mapped[str] = mapped_column(Enum(SexEnum), comment="性別")
    phone: Mapped[str] = mapped_column(String, comment="連絡先電話番号")
    address: Mapped[str] = mapped_column(String, comment="連絡先住所")
    parent: Mapped[str] = mapped_column(String, comment="保護者")
    status: Mapped[int] = mapped_column(Enum(StatusEnum), comment="在内・在外ステータス")
    classroom_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("classroom.id"), comment="教室", default=None
    )
    classroom: Mapped["ClassroomModel"] = relationship(
        "ClassroomModel", back_populates="children", default=None
    )
    timelines: Mapped[list["ChildTimelineModel"]] = relationship(
        "ChildTimelineModel",
        back_populates="child",
        default=None,
    )


class ChildTimelineModel(Base):
    """
    園児のタイムライン
    """

    date: Mapped[datetime.date] = mapped_column(Date, comment="日付")
    time: Mapped[datetime.time] = mapped_column(Time, comment="時刻")
    event: Mapped[int] = mapped_column(Enum(StatusEnum), comment="記録の種類")
    child_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("child.id"), default=None, comment="園児"
    )
    child: Mapped[ChildModel] = relationship(
        "ChildModel", default=None, back_populates="timelines"
    )


class EmployeeModel(Base, TimestampMixin):
    """
    従業員
    """

    serial_number: Mapped[str] = mapped_column(String, comment="社員番号", unique=True)
    first_name: Mapped[str] = mapped_column(String, comment="名")
    last_name: Mapped[str] = mapped_column(String, comment="姓")
    belong: Mapped[bool] = mapped_column(Boolean, comment="在職中か否か")
    birthday: Mapped[datetime.date] = mapped_column(Date, comment="誕生日")
    sex: Mapped[str] = mapped_column(Enum(SexEnum), comment="性別")
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey("job.id"))
    job: Mapped[JobModel] = relationship(
        "JobModel", back_populates="employees", default=None
    )
    profiles: Mapped[list["ProfileModel"]] = relationship(
        "ProfileModel", back_populates="employee", default=None
    )
    auth_id: Mapped[str | None] = mapped_column(
        String, default=None, comment="認証ID", unique=True
    )
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


class EmployeeRecordModel(Base):
    """
    従業員記録
    """

    date: Mapped[datetime.date] = mapped_column(Date, comment="日付")
    attend_time: Mapped[datetime.time] = mapped_column(Time, comment="登園時間")
    note: Mapped[str | None] = mapped_column(String, comment="備考")
    leave_time: Mapped[datetime.time | None] = mapped_column(
        Time, default=None, comment="退園時間"
    )
    edited: Mapped[bool] = mapped_column(Boolean, default=False, comment="編集済みか否か")
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("employee.id"), default=None, comment="従業員"
    )
    employee: Mapped[EmployeeModel] = relationship(
        "EmployeeModel", default=None, back_populates="records"
    )


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
