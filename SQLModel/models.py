from sqlmodel import SQLModel,Field, AutoString,Column,String
from typing import Optional
from pydantic import EmailStr



class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(None, primary_key=True)
    name: str 
    email: EmailStr  = Field(unique=True, index=True, sa_type=AutoString,nullable=False)
    #email:str = Field(sa_column=Column("email", AutoString, nullable=False))
    #email:str
    password: str
    
class get_User(SQLModel):
    id:int
    name: str 
    email: str
    password: str
    
class create_User(SQLModel):
    id:int
    name:str
    email:str
    password:str
        
    
