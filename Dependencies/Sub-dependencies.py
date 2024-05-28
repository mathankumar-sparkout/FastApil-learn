from typing import Union
from fastapi import FastAPI, Cookie, Depends
from typing_extensions import Annotated

app = FastAPI()


async def fun(q: str | None = None):
    return q


def fun(
    q: Annotated[str, Depends(fun)],
    query: Annotated[Union[str, None], Cookie()] = None,
):
    if not q:
        return query
    return q


@app.get("/items/")
async def read_query(
    default: Annotated[str, Depends(fun)],
):
    return {"q_or_cookie": default}
