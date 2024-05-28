from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id:str | None =Cookie(default='abc')):
    return {"ads_id": ads_id}