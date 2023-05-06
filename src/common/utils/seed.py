from common.models import SQLModel, engine


def seed():
    SQLModel.metadata.drop_all(engine)

    SQLModel.metadata.create_all(engine)


seed()
