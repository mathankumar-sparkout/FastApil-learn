from fastapi import FastAPI
import models
from database import engine
from sqlmodel import SQLModel, Session
from routers import user

app = FastAPI()

# models.Base.metadata.create_all(engine)
SQLModel.metadata.create_all(engine)
session = Session(engine)

app.include_router(user.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.2", port=7000)
