from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

colleges = {1: {"name": "kumar", "cls": "A", "mark": 77}}


class college(BaseModel):
    name: str
    cls: str
    mark: int


class Update_college(BaseModel):
    name: str
    cls: str
    mark: int


@app.get("/get_college/{college_id}")
async def get_college(college_id: int):
    result = colleges[college_id]
    return result


@app.post("/post_college/{college_id}")
async def create_college(college_id: int, request: college):
    if college_id in colleges:
        return {"already exits "}
    result = colleges[college_id] = request
    return result


@app.put("/update_colleages/{college_id}")
async def update_colleges(college_id: int, request: Update_college):
    if college_id not in colleges:
        return {"Not in colleages"}
    result = colleges[college_id] = request
    return result


@app.delete("/delete_colleages/{college_id}")
async def delete_colleages(college_id: int):
    if college_id not in colleges:
        return {"ERROR:not in colleages"}
    del colleges[college_id]
    return {"deleted successfully"}
