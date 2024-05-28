from fastapi import FastAPI,status

app=FastAPI()

@app.get("/root",status_code=201) #->status code
async def fun(name:str):
    return name







@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}