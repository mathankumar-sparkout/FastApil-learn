from app.Database.database import engine,Session
from app.routes import student
from app.models import models
from app.schemas import schema
from fastapi import FastAPI
from sqlmodel import SQLModel
from fastapi_pagination import Page, add_pagination, paginate
app=FastAPI()
add_pagination(app)

SQLModel.metadata.create_all(engine)
db = Session(engine)

app.include_router(student.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

 