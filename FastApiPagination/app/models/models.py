from sqlmodel import SQLModel,Field,AutoString
from pydantic import BaseModel,EmailStr


class Student(SQLModel,table=True):
    __tablename__="students"
    Std_id:int=Field(primary_key=True)
    Std_name:str=Field(index=True)
    Std_age:int
    Std_email:EmailStr=Field(sa_type=AutoString)
    Std_address:str
        
    