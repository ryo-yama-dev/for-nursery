from fastapi import FastAPI

from .common.models import SQLModel, engine

SQLModel.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
