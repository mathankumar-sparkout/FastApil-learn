from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, Annotated

app = FastAPI()

User = {
    1: {
        "user_name": "python",
        "user_age": 18,
        "description": "Fastapi is easy to learn",
    }
}


class post_user(BaseModel):
    user_name: str | None = None
    user_age: int
    description: str


class put_user(BaseModel):
    user_name: str | None = None
    user_age: int | None = None
    description: str | None = None


@app.get("/user_id/{user_id}/user")
async def get_user(
    *,
    user_id: int = Path(title="FastAPI"),
    id: Annotated[int, None] = None,
    user: int  # user is defalut parameter (default argument doesn't follow key&possional argument so use(*) )
):
    return User[user_id]


@app.post("/post_user/{user_id}")
async def post_user(user_id: int, request: post_user):
    if user_id in User:
        return {"already defined"}
    result = User[user_id] = request
    return result


@app.put("/put_user/{user_id}")
async def put_user(user_id: int, request: put_user):
    if user_id not in User:
        return {"User doesnot Exit"}
    result = User[user_id] = request
    return result


@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    if user_id not in User:
        return {"User doesn't Exit"}
    del User[user_id]
    return {"Successfullty deleted"}
