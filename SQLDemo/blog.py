from sqlmodel import SQLModel, Field,create_engine,Session,select

#Create a Table with SQL----
class Blog(SQLModel,table=True):
    __tablename__='blogs'
    id:int|None=Field(default=None,primary_key=True)
    name:str|None = Field(index=True)
    age:int |None

class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    #team_id: int | None = Field(default=None, foreign_key="team.id")
# Create a Table with SQLModel - Use the Engine---- 
engine = create_engine("mysql+pymysql://root:admin@localhost:3306/demosql",echo=True)

#Create Rows - Use the Session - INSERT-------
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    statement = select(Blog)

def create_blogs():
    blog_1 =Blog(name="Deadpond")
    blog_2 =Blog(name="Spider-Boy",age=12)
    blog_3 =Blog(name="Rusty-Man", age=48)

    session = Session(engine)
    
    session.add(blog_1)
    session.add(blog_2)
    session.add(blog_3)
    session.commit()
    
  
#Filter Data - WHERE  -----Read Data - SELECT  ---Read One Row
def select_blogs():
    with Session(engine) as session: # engine as session
        statement = select(Blog).where(Blog.name == "Deadpond").offset(3).limit(3) # select the blog(class).useing where condition # limit the value  3 rows
        results = session.exec(statement)  
    
        blog= results.first()#-->.first()-> first or one() single data only showed     -->. all()print all data in database
        print(blog)
        blog.age=20  # update the age
        session.add(blog)
        session.commit()
        session.refresh(blog)
        print("updated ",blog)



#Update Data - UPDATE-------------

def update_blogs():
    with Session(engine) as session:
        statement = select(Blog).where(Blog.name == "Spider-Boy")
        results = session.exec(statement)
        blog_1 = results.first()
        print("Hero 1:", blog_1)


        blog_1.age = 16
        blog_1.name = "Spider-Youngster"
        session.add(blog_1)

        

        session.commit()
        session.refresh(blog_1)
       

        print("Updated hero 1:", blog_1)
   
# Delete Data - DELETE -------------
def delete_blogs():
    with Session(engine) as session:
        statement = select(Blog).where(Blog.name == "Spider-Youngster")
        results = session.exec(statement)
        blog = results.first()
        print("Hero: ", blog)

        session.delete(blog)
        session.commit()

        print("Deleted hero:",blog)
   
def main():  
    create_db_and_tables()  
    create_blogs()  
    select_blogs()
    update_blogs()
    delete_blogs()


if __name__ == "__main__":  
    main()  

