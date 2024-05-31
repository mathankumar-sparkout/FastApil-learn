from sqlmodel import SQLModel,AutoString,Field
from pydantic import BaseModel,EmailStr


class response_student(SQLModel):
    Std_id:int
    Std_name:str
    Std_age:int
    Std_email:EmailStr=Field(sa_type=AutoString)