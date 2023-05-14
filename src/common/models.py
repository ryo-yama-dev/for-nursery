import datetime
import os

from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, create_engine

load_dotenv()
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
postgres_host = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")

__all__ = [ "Job", "Classroom", "Child", "Employee", "Profile", "ChildRecord", "EmployeeRecord" ]

class Job(SQLModel, table=True):
    """
    職種・職級
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, description="職種名")
    rank: int = Field(unique=True, description="職級")


class Child(SQLModel, table=True):
    """
    園児
    """

    id: int | None = Field(default=None, unique=True, primary_key=True, description="")
    name: str = Field(description="氏名")
    age: int = Field(description="年齢")
    sex: str = Field(description="性別")
    phone: str = Field(description="連絡先電話番号")
    address: str = Field(description="連絡先住所")
    parent: str = Field(description="保護者")


class Employee(SQLModel, table=True):
    """
    従業員
    """

    id: int | None = Field(default=None, primary_key=True, unique=True, description="")
    auth_id: str | None = Field(default=None, description="認証ID")
    name: str = Field(description="氏名")
    belong: bool = Field(description="在職中か否か")
    jobs: list[int] = Field(description="職種")


class Profile(SQLModel, table=True):
    """
    固有プロフィール
    """

    id: int | None = Field(default=None, primary_key=True, unique=True, description="")
    person_id: int = Field(description="紐づけられているEmployeeもしくはChildのID")
    headline: str = Field(description="見出し")
    letter: str | None = Field(description="本文")


class Classroom(SQLModel, table=True):
    """
    クラス
    """

    id: int | None = Field(default=None, primary_key=True, unique=True, description="")
    name: str = Field(unique=True, description="組名")
    age: int = Field(description="年齢")
    employees: list[int] = Field(description="担当従業員")
    children: list[int] = Field(description="所属園児")


class ChildRecord(SQLModel, table=True):
    """
    園児記録
    """

    id: int | None = Field(default=None, primary_key=True, description="")
    child_id: int | None = Field(description="園児", foreign_key="child.id")
    date: datetime.date = Field(description="日付")
    attend_time: datetime.time = Field(description="登園時間")
    leave_time: datetime.time = Field(description="退園時間")
    edited: bool = Field(default=False, description="編集済みか否か")
    note: str | None = Field(description="備考")


class EmployeeRecord(SQLModel, table=True):
    """
    従業員記録
    """

    id: int | None = Field(default=None, primary_key=True, description="")
    employee_id: int | None = Field(description="従業員", foreign_key="employee.id")
    date: datetime.date = Field(description="日付")
    attend_time: datetime.time = Field(description="出勤時間")
    leave_time: datetime.time = Field(description="退勤時間")
    edited: bool = Field(default=False, description="編集済みか否か")
    note: str | None = Field(description="備考")


postgre_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/postgres"

engine = create_engine(url=postgre_url, echo=True)
