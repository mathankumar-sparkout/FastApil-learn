from sql_alchemy import alchemy, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Session=sessionmaker(bind=engine)
session=Session()
'''use=alchemy(id=1,name="john",age=24)  #use is a primary key 
use_2=alchemy(id=2,name="Arun",age=50)
use_3=alchemy(id=3,name="Kumar",age=60)
use_4=alchemy(id=4,name="Raj",age=24)
use_5=alchemy(id=5,name="Tamil",age=14)
#session.add(user)
session.add(use_2)
session.add_all([use_3,use_4,use_5])
session.commit()'''

#Read the data in database------------
user=session.query(alchemy).all()
print(user)  #->print all user table data
print(user[1]) # index num{1]
#print(user.id)
use=user[0]
print(use)
print(use.id)
print(use.name)
print(use.age)
for use in user:
    print(f"id:{use.id},name:{use.name},age:{use.age}")
#update the data-----------------
'''user=session.query(alchemy).filter_by(id=2).one_or_none()
print(use.name)
use.name="A different name"
print(use.name)
session.commit()'''

#delete the data--------------------
user=session.query(alchemy).filter_by(id=2).one_or_none()
session.delete(user)
session.commit()


