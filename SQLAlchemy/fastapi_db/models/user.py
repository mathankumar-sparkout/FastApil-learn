from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,Integer
from config.db import meta

users=Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(20)),
    Column('email',String(20)),
    Column('password',String(20)),
    
    
)