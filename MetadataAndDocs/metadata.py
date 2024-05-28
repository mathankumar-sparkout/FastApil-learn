from fastapi import FastAPI  # import fastapi


tags_metadata = [  # get/post/put/delete  box
    {
        "name": "fastapi",
        "description": "hii python",
    },
    {"name": "python", "description": "fastapi to sql server"},
]


app = FastAPI(
    title="python Api",  # logo
    description="FastAPI easy to learn  🚀",  # after summary line
    summary="FastApi is good app",  # top of the page
    terms_of_service="http://example.com/terms/",  # link
    openapi_tags=tags_metadata,
)


@app.get("/user", tags=["User"])
async def meta():
    return {"name": "python"}
