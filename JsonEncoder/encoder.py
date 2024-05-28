from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime
import time

app=FastAPI()
fake_db={}
class Item(BaseModel):
    tittle:str
    time:datetime
    description:str|None=None
    
@app.post("/encoder/{id}")
async def encoder(id:int,item:Item):
    json_changer=jsonable_encoder(item)
    #fake_db[id]=json_changer
    print(type(json_changer)) # json format changed->dict
    return json_changer

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
