from fastapi import FastAPI, HTTPException
from enum import Enum  # specfic type choose

app = FastAPI()


class user(str, Enum):  # class
    vegetables = "vegetables"
    fruits = "fruits"
    dairy = "dairy"


@app.get("/food/{food_name}")
async def fun(food_name: str):
    if food_name == user.vegetables:  # -> user type ==user class same
        return {"you are choose vegetables": food_name}  # -> return user class value
    # elif(food_name ==user).fruits:
    # return {"you are choose fruits":food_name}
    elif food_name == user.fruits:  # -> same thing
        return {"your are choose fruits": food_name}
    elif food_name == user.dairy:
        return {"you are choose dairy": food_name}
    elif food_name != user:
        raise HTTPException(status_code=404)
