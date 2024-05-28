from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app=FastAPI()

class Item(BaseModel):
    name:str|None=None
    tax:float=10.8
    descriptrion:str|None=None
    price:int|None=None
    
items={
    "foo":{"name":"foo","tax":10.8,"descriptrion":"python","price":None},
    "boo":{"name":"boo","tax":10.8,"descriptrion":"python"},
    "hoo":{"name":"hoo","descriptrion":"python"}
    
}

@app.put("/post_method/{id}")
async def Crete(id:str,item:Item):
    json_changer=jsonable_encoder(item)
    items[id]=json_changer
    return json_changer

@app.get("/get_method/{id}")
async def fun(id:str):
    return items[id]


@app.patch("/patch_method/{id}")
async def Update(id:str,item:Item):
    if id not in items:
        return {"error": "Item not found"}
    
    item_data = items[id]
    for field_name, value in item.dict().items():
        if value is not None:
            item_data[field_name] = value
    
    return {"message": "Item updated successfully", "item_id":id, "updated_item": item_data}
    #json_changer=jsonable_encoder(item)
    #items[id]=json_changer
    #return json_changer
    
