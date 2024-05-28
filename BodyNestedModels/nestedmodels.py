from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Item(BaseModel):  # basemodel
    name: str
    description: str
    price: int | None = None
    tags: list = []  # list method (we can add int ,str values)


@app.put("/Items/{item_id}")  # path
async def fun(item_id: int, items: Item):  # path parameter item_id
    return {"item_id": item_id, "item": items}


# List(str)---------------------------------------------------------------


class Item(BaseModel):  # basemodel
    name: str
    description: str
    price: int | None = None
    tags: list[str] = []  # list method (we can add only str values)


@app.put("/Itemes/{item_id}")  # path
async def fun(item_id: int, items: Item):  # path parameter item_id
    return {"item_id": item_id, "item": items}


# set(str)-------------------------------------------------------------------------


class Item(BaseModel):  # basemodel
    name: str
    description: str
    price: int | None = None
    tags: set[
        str
    ] = ()  # set method (we can add only str values--> doesn't allow duplicate values)


@app.put("/Itemss/{item_id}")  # path
async def fun(item_id: int, items: Item):  # path parameter item_id
    return {"item_id": item_id, "item": items}


# Image--------------------------------------------------------------------------------------------


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):  # basemodel
    name: str
    description: str
    price: int | None = None
    image: Image | None = None  # -> Image basemodel nested


@app.put("/root/{item_id}")  # path
async def fun(item_id: int, items: Item):  # path parameter item_id
    return {"item_id": item_id, "item": items}


# -----------------------------------------------------------------------------------------------


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, int, None] = None
    tags: set[str] = set()
    image: Union[Image, None] = None


@app.put("/user/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
