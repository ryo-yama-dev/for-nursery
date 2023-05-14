from sqlmodel import Session

from common.models import SQLModel, engine, Job


def seed():
    SQLModel.metadata.drop_all(engine)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(Job(name="職種A", rank=1))
        session.add(Job(name="職種B", rank=2))
        session.add(Job(name="職種C", rank=3))
        session.add(Job(name="職種D", rank=4))
        session.add(Job(name="職種E", rank=5))
        session.add(Job(name="職種F", rank=6))

        session.commit()

seed()
