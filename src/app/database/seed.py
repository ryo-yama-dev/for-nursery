import os
import random

from faker import Faker
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from app.common.config import get_settings
from app.database.models import (
    Base,
    ChildModel,
    ChildRecordModel,
    ClassroomModel,
    EmployeeModel,
    EmployeeRecordModel,
    JobModel,
    SexEnum,
)

postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
user_password = f"{postgres_user}:{postgres_password}"
postgres_host = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")
host_port = f"{postgres_host}:{postgres_port}"

settings = get_settings()


def seed() -> None:
    try:
        engine = create_engine(
            f"postgresql+psycopg://{user_password}@{host_port}/postgres"
        )

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        faker = Faker("ja_JP")

        session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
        )()

        jobs = session.scalars(
            insert(JobModel).returning(JobModel),
            [dict(name=faker.job(), rank=i) for i in range(1, 6)],
        )

        classrooms = session.scalars(
            insert(ClassroomModel).returning(ClassroomModel),
            [dict(name=faker.name(), age=i) for i in range(1, 6)],
        )

        cla_ids = [cla.id for cla in classrooms]

        employees = session.scalars(
            insert(EmployeeModel).returning(EmployeeModel),
            [
                dict(
                    name=faker.name(),
                    belong=True,
                    job_id=job.id,
                    sex=random.choice([SexEnum.MALE, SexEnum.FEMALE]),
                    classroom_id=random.choice(cla_ids),
                )
                for job in jobs
            ],
        )

        children = session.scalars(
            insert(ChildModel).returning(ChildModel),
            [
                dict(
                    name=faker.name(),
                    age=random.randint(1, 6),
                    sex=random.choice([SexEnum.MALE, SexEnum.FEMALE]),
                    phone=faker.phone_number(),
                    address=faker.address(),
                    parent=faker.name(),
                    classroom_id=random.choice(cla_ids),
                )
                for _ in range(1, 20)
            ],
        )

        session.execute(
            insert(EmployeeRecordModel).returning(EmployeeRecordModel),
            [
                dict(
                    employee_id=employee.id,
                    date=faker.date(),
                    attend_time=faker.time(),
                    leave_time=faker.time(),
                )
                for employee in employees
            ],
        )

        session.execute(
            insert(ChildRecordModel).returning(ChildRecordModel),
            [
                dict(
                    child_id=child.id,
                    date=faker.date(),
                    attend_time=faker.time(),
                    leave_time=faker.time(),
                )
                for child in children
            ],
        )

        session.commit()
        print("seeded")

    except Exception as e:
        print(e)


seed()
