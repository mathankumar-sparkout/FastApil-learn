# return string
# get


from fastapi import FastAPI  # -> import fastApi
from pydantic import BaseModel


app = FastAPI()  # -> app is fastapi


@app.get("/")  # -> dec the get op
async def root():
    return {"message": "Hello World"}


class a(BaseModel):
    id: int
    name: str
    age: int
    address: str | None


@app.post("/")
def fun(a: a):
    return a






