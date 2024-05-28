from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user=APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()



@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id ==id)).fetchall()

@user.post("/")
async def post_data(user:User):
    conn.execute(users.insert().values(                                                          
        name=user.name,
        email=user.email,
        password=user.password
    ))
    return conn.execute(users.select()).fetchall()

'''@app.post("/post_college/{college_id}")
async def create_college(college_id: int, request: college):
    if college_id in colleges:
        return {"already exits "}
    result = colleges[college_id] = request
    return result'''

@user.put("/{id}")
async def update_data(id :int,user:User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
        
    )).where(users.c.id ==id)
    return conn.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
    conn.execute(users.delete().where(users.c.id ==id))
    return conn.execute(users.select()).fetchall()