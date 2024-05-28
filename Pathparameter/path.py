from fastapi import FastAPI

app = FastAPI()


# ->single path parameter
@app.get("/id/{user_id}")
async def fun(user_id: int):  # ->fix datatype in parameter
    return {"id": user_id}  # -> return value


# multiple path parameter---------------------------------


@app.get("/{id}/{user_name}/{user_age}/{user_status}")
async def user(id: int, user_name: str, user_age: int, user_status: str):
    return {"id": id, "name": user_name, "age": user_age, "user_status": user_status}


# dictionary --------------------------

user = {  # -> craete dictionary user
    1: {
        "name": "arun",
        "age": 20,
    },
    2: {
        "name": "raj",
        "age": 18,
    },
    3: {
        "name": "kumar",
        "age": 50,
    },
}


@app.get("/use/{ids}")  # -> create root use {ids 1,2,3}
async def fun(ids: int):  # -> type int
    return user[ids]  # -> return dictionary id



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.2", port=7000)