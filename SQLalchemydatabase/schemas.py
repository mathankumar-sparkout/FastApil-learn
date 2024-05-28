from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class show_Blog(BaseModel):
    title: str
    body: str
    id: int


class User(BaseModel):
    name: str
    email: str
    password: str


class showUser(BaseModel):
    name: str
    password: str
    id: int


class get_User(BaseModel):
    name: str
    email: str
    password: str
    id: int
