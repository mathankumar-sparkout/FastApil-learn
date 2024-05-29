from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates


app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.get("/")
async def fun(request:Request):
    items=["item1","item2","item3"]
    
    return templates.TemplateResponse("index.html",{"request":request,"title":"Home page","message":"welcome to website","items":items})