from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field  # -> fileds only imported pydantic

app = FastAPI()


class Items(BaseModel):
    name: str |None
    description: str | None = Field(  # -> create fileds add some values
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Items, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}  # -> return the result
    return results
