from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

# from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(String(200))
    # user_id=Column(Integer,ForeignKey("users.id"))

    # items=relationship("User",back_populates="owner")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(200))
    password = Column(String(200))

    # owner=relationship("Blog",back_populates="items")
