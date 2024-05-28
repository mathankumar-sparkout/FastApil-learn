from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
from typing import List,Union
from sqlmodel import Session,select
from models import User
#from database import engine 

router = APIRouter(tags=["User"])

get_db = database.get_db



@router.get("/get_all_user",response_model=List[User],status_code=status.HTTP_200_OK)
def get_user(session: Session = Depends(get_db)):
    user=session.exec(select(User)).all()
    return user
    
    
# get single user data------

@router.get("/get_user/{user_id}",response_model=models.User,status_code=status.HTTP_200_OK)
def get_single_user(user_id :int,session: Session = Depends(get_db)):
        user=session.get(models.User, user_id)
        if user is None:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"USER with the id {user_id} is not available"
            )
        return user
    

#post 
@router.post("/post_user",response_model=models.User,status_code=201)
# only we want name and password use this reponse_model
def create_user(request: models.User, session: Session = Depends(get_db)):
   
    
    session.add(request) 
    session.commit() 
    session.refresh(request)
    return request

@router.put("/update_user/{user_id}",response_model=models.User)
def update_user(user_id:int,update_user:models.get_User,session:Session=Depends(get_db)):
    user=session.get(models.User,user_id)
  
    if user is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"USER with id {id} not found"
        )
    update_data=update_user.model_dump(exclude_unset=True)
    user.sqlmodel_update(update_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
    

@router.delete("/delete user/{user_id}",status_code=status.HTTP_202_ACCEPTED,)
def delete_user(user_id:int,session:Session=Depends(get_db)):
    user=session.get(models.User,user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="hero is not found")
    session.delete(user)
    session.commit()
    return {"successfully deleted"}
        
      
    
    
    


