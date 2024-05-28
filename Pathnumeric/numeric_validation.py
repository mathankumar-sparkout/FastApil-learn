from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")  # ->using path parameter item_id
async def read_itemss(
    *, item_id: int = Path(title="The ID of the item to get", ge=3), q: str
):
    results = {"item_id": item_id}  # the user defined the value show the result column
    if q:
        results.update({"q": q})  # -> q is a query parameter
    return results


@app.get("/item/{id}")
async def fun(
    q: str, id: int = Path(title="the Id of the item to get", ge=3, le=100)
):  # gether then only above 3
    result = {"id": id}
    if q:
        result.update({"q:": q})
    return result
