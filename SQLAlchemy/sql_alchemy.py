from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String

engine =create_engine("mysql+pymysql://root:admin@localhost:3306/alchemy")

Base=declarative_base()
class alchemy(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)     
    name=Column(String(50))
    age=Column(Integer)
        
Base.metadata.create_all(engine)
    
connection = engine.connect()

if(connection):
    print("connected")













