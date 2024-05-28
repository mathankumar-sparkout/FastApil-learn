from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/root")
async def fun(
    q: list[str] | None = Query(
        default="abc", max_length=3, description="hii", deprecated=True
    )
):  # ->default take value#->default=... its is a requird..#include_in_schema is delete input filed
    result = {"value": [{"id": "foo"}, {"id": "barr"}]}
    if q:
        result.update({"q": q})
    return result
