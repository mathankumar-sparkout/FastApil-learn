from typing import Annotated
from fastapi import FastAPI,Form #import form in fastapi

app=FastAPI()

@app.post("/Form")
async def form(username:Annotated[str,Form()]=None,password:Annotated[str,Form()]=None):
    return username


