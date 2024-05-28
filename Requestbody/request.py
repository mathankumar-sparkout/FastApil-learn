from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class a(BaseModel):  # datavalidation
    name: str
    description: str | None = None  # optional
    price: float
    tax: float | None = None


@app.post("/")  # ->request to api response result
async def fun(a: a):
    return a


# ----------------------------------------------------------
class b(BaseModel):
    id: int
    name: str
    gender: str | None = None
    age: int | None = None
    location: str | None = None


@app.post("/")
async def funs(b: b):
    return b
