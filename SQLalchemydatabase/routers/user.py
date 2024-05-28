from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
import schemas
from typing import List
from sqlalchemy.orm import Session
import hashing
from database import SessionLocal

router = APIRouter(tags=["User"])

get_db = database.get_db


# CREATE NEW USER------------


@router.post("/post_user", response_model=schemas.showUser)
# only we want name and password use this reponse_model
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashing.hash.bcrypt(request.password),
    )
    db.add(new_user) 
    db.commit() 
    db.refresh(new_user)
    return new_user


# GET USER DATA----------------


@router.get("/get_user/{id}", response_model=schemas.get_User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"value {id} not in database"
        )
    return user


# UPDATE USER DATA---------------


@router.put(
    "/update_data/{id}",
    response_class=Response,
    status_code=status.HTTP_202_ACCEPTED,
)
def update_data(id: int, request: schemas.User, db: Session = Depends(get_db)):
    update_user = db.query(models.User).filter(models.User.id == id)
    update_user.update(
        {"name": request.name, "email": request.email, "password": request.password}
    )

    if not update_user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    db.commit()


# DELETE USER DATA-----------------


@router.delete("/items/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_item(id: int):
    db = SessionLocal()
    db_item = db.query(models.User).filter(models.User.id == id).first()
    db.delete(db_item)
    db.commit()
    return {f"message:data deleted {id} successfully"}
