import os

from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, create_engine

load_dotenv()
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
postgres_host = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")


class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    rank: int


postgre_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/postgres"

engine = create_engine(url=postgre_url, echo=True)

# SQLModel.metadata.create_all(engine)
