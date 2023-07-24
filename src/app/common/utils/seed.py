import os

from faker import Faker
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

from app.common.config import get_settings
from app.common.models import Base, JobModel

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

        print(jobs)

        session.commit()
        print("seeded")

    except Exception as e:
        print(e)


seed()
