from sqlmodel import SQLModel,create_engine,Session,Field,select
from fastapi import FastAPI,Depends
app=FastAPI()
   

#TABLE

class Student(SQLModel,table=True):
    __tablename__='students'
    id:int=Field(default=None,primary_key=True)
    first_name:str
    last_name:str |None
    gender:str
    age:int=Field(default=None,index=True)


#DATABASE CONNECTION
engine=create_engine("mysql+pymysql://root:admin@localhost:3306/student",echo=True)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
    

def get_session():
    with Session(engine) as session:
        yield session
   

'''#STARTUP
@app.on_event("startup")
def on_startup():
    create_db_and_table()'''
    
#POST STUDENT DATA  
@app.post("/CreateStudent_data",response_model=Student)
def CreateStudent_data(requestbody:Student,session:Session=Depends(get_session)):
    session.add(requestbody)
    session.commit()
    session.refresh(requestbody)
    return requestbody

#GETALL STUDENT DATA
@app.get("/GetStudent_data")
def GetallStudent_data(session:Session=Depends(get_session)):
    std=session.exec(select(Student)).all
    return std

