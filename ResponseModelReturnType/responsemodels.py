from fastapi import FastAPI
from pydantic import BaseModel,EmailStr #import Emailstr from pydantic
from typing import Any



app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item: #-> return value is Item
    return item


'''@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]'''
    
#-------------------------------------------------------------------------------------------------------------------------
class items(BaseModel): #->pydantic basemodel
    username:str
    password:int 
    email:EmailStr
    full_name:str |None
    full_name:str |None =None
    
@app.post("/root")        
async def fun(Items:items)->items:
    return Items
    
    
