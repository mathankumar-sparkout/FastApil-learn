from sqlmodel import SQLModel,Field,create_engine,Session,select
from fastapi import FastAPI,HTTPException,Query,Depends

app=FastAPI()

class Hero(SQLModel,table=True):  #->table
    __tablename__='heros'
    id:int|None=Field(default=None,primary_key=True)
    name:str|None
    age:int=Field(default=None,index=True)
    
    
class Hero_Update(SQLModel): #-> basemodel
    #id:int
    name:str
    age:int
    
engine=create_engine("mysql+pymysql://root:admin@localhost:3306/modelhero",echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    

def get_session():
    with Session(engine) as session:
        yield session




@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#post data-------

@app.post("/create_hero",response_model=Hero)
def create_hero(*,session:Session = Depends(get_session),hero:Hero):
   # with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero
        
# get all data----
       
@app.get("/get_all_hero")
def get_hero(*,session:Session = Depends(get_session),offset: int = 0, limit: int = Query(default=100, le=100)):
    hero=session.exec(select(Hero).offset(offset).limit(limit)).all()
    return hero
# get single data----
  
@app.get("/single_data/{hero_id}")
def single_hero(hero_id :int):
    with Session(engine) as session:
        hero=session.get(Hero,hero_id)
        if not hero:
            raise HTTPException(status_code=404,detail="hero is not found")
        return hero
    
# update data---
   
@app.put("/update_data/{hero_id}",response_model=Hero)
def update_hero(*,session:Session = Depends(get_session),hero_id :int,hero:Hero_Update):
    #with Session(engine)as session:
        db_hero=session.get(Hero,hero_id)
        if not db_hero:
             raise HTTPException(status_code=404,detail="hero is not found")
        hero_data=hero.model_dump(exclude_unset=True)
        db_hero.sqlmodel_update(hero_data)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero
    
# delete data----
   
@app.delete("/delte_data/{hero_id}")
def delete_hero(*,session:Session = Depends(get_session),hero_id:int):
    #with Session(engine)as session:
        del_hero=session.get(Hero,hero_id)
        if not del_hero:
            raise HTTPException(status_code=404,detail="hero is not found")
        session.delete(del_hero)
        session.commit()
        return {"successfully deleted"}