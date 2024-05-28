from typing import Annotated
from fastapi import FastAPI,Depends

app=FastAPI()


async def fun(q:str |None=None,skip:int =0,limit:int=100):
    return{"q":q,"skip":skip,"limit":limit}


@app.get("/item")
async def items(commons:Annotated[dict,Depends(fun)]):
    return commons



@app.get("/user")
async def items(commons:Annotated[dict,Depends(fun)]):
    return commons