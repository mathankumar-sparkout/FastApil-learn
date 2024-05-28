from pydantic import BaseModel,Field # import Field in pydantic 
from fastapi import FastAPI,Body
from typing import Annotated

app=FastAPI()


class user(BaseModel):
    name:str|None =Field(examples=['hii'])  #->name is a string or null ->use example this is automatically defined the value
    age:int |None
    description:str|None =Field(examples=["python"])   



@app.put("/http/{id}")
async def fun(id :int,User:user):
    return{"id":id,"user":User} 


#-----------------------------------------------------------------------------------------------------------------
class model(BaseModel):
    name:str
    tags:str|None
    price:int
    description:str
    
@app.put("/model/{ids}")
async def fun(ids :int,Model:Annotated[
    model,
    Body(
        examples=[{"name":"mathan",#->examples using inside the function
                   "tags":"hii",
                   "price":100,
                   "description":"python"
                   }],),],):
    return {"ids":ids,"models":Model}
    
    
    
   
