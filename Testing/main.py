from fastapi import FastAPI,Header,HTTPException,status
from typing import Annotated
from pydantic import BaseModel

app=FastAPI()

fake_secret_token = "coneofsilence"

fake_db={
    "foo":{"id":"foo","tittle":"Fooo","description":"this is foo"},
    "boo":{"id":"boo","tittle":"Booo","description":"this is boo"}
}

class Item(BaseModel):
    id:str
    tittle:str
    description:str|None
    
@app.get("/items/{item_id}",response_model=Item)
async def token(item_id:str,x_token:Annotated[str,Header()]):
    if x_token != fake_secret_token:
        return HTTPException(status_code=404,detail="X-token not found")
    if item_id not in fake_db:
        return HTTPException(status_code=400,detail="not found")
    return fake_db[item_id]

@app.post("/items/{item_id}",response_model=Item)
async def Create(item_id:str,item:Item,x_token:Annotated[str,Header()]):
    if x_token != fake_secret_token:
        return HTTPException(status_code=404,detail="X-token not found")
    if item_id  in fake_db:
        return HTTPException(status_code=400,detail="Already Exits")
    fake_db[item_id]=item
    return item