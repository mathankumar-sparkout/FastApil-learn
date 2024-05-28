from fastapi import FastAPI, Body
from pydantic import BaseModel  # -> imported basemodel
from typing import Annotated

from fastapi import Body, FastAPI

app = FastAPI()


class item(BaseModel):  # -> add the first basemodel
    id: int
    name: str
    status: str | None


class user(BaseModel):  # ->add the second basemodel
    user_id: int
    user_name: str
    user_status: str | None


@app.put("/root/{item_id}")  # -> path parameter add {item_id}
async def fun(item_id: int, item: item, user: user, importance: Annotated[int, Body()]):
    return {"item_id": item_id, "user": user, "item": item, "importance": importance}


# Body-----------


class Item(BaseModel):  # basemodel Item
    name: str
    description: str
    price: int
    tax: int


class User(BaseModel):  # basemodel User
    username: str
    full_name: str


@app.put("/items/{item_id}")  # path parameter
async def fun(
    item_id: int,
    user: User,
    item: Item,
    importance: Annotated[int, Body(ge=1)],
    q: str | None = None,
):  # impotance boby field greathan 0 +
    results = {
        "item_id": item_id,
        "user": user,
        "item": item,
        "importance": importance,
    }  # return the result
    if q:
        results.update(
            {"q": q}
        )  # if Q (Query field add some value return that value otherwise return the None)
    return results


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/itemss/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
