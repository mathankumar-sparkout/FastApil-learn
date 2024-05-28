from fastapi import APIRouter, Depends, status, HTTPException, Response
import database, models
import schemas
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["blogs"],
    # prefix='/blogs'-> change the names
)

get_db = database.get_db 


@router.get("/get_blog", response_model=List[schemas.show_Blog])
# collection of blogs we want so we use List
async def get(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# post all data -----


@router.post(
    "/blog", status_code=status.HTTP_201_CREATED, response_model=schemas.show_Blog
)
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# single data return----


@router.get("/get_singledata/{id}", response_model=schemas.show_Blog)
# response_model work if we want which title or body basemodel(pydantic)
# choose the model(schemas->show_blog)
def singledata(id, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {f"Blog with the id{id}is not available"}
    return blogs


@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, response_class=Response)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    blog.update({"title": request.title, "body": request.body})
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    db.commit()


# delete data in database----


@router.delete("/delete_data/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blogs(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {f"not avalaiable{id}"}
