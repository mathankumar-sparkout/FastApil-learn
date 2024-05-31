from fastapi import APIRouter, Depends, HTTPException, status
from app.Database import database
from app.models import models
from app.schemas import schema
from sqlmodel import SQLModel, Session, select
import logging
from fastapi_pagination import Page, paginate


router = APIRouter()
get_db = database.get_db

logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="w",
    format="%(asctime)s-%(levelname)s-%(message)s",
)

# GET_ALL_STUDENT----


@router.get(
    "/Get_All_Student",
    tags=["STUDENT"],
    summary="Get All Process Student",
    response_description="File Get All processed to Student successfully.",
    status_code=status.HTTP_200_OK,
)
async def Get_All_Student(page: int = 1, limit: int = 3, db: Session = Depends(get_db)):
    """
    Endpoint for processing  Get_All_Student get the All data into Database.
    \f
    :db: Database session.
    :return: JSONResponse with status code and message.
    """

    logging.info("get all the Student triggered.")
    # student = db.exec(select(models.Student)).all()
    # return paginate(student,page=page, page_size=limit)
    offset = (page - 1) * limit
    query = select(models.Student).offset(offset).limit(limit)
    students = db.exec(query).all()

    return students


# GET_STUDENT----


@router.get(
    "/Get_Student",
    tags=["STUDENT"],
    response_model=schema.response_student,
    summary="Get Process Student",
    response_description="File Get processed to Student successfully.",
    status_code=status.HTTP_200_OK,
)
async def Get_Student(id: int, db: Session = Depends(get_db)):
    """
    Endpoint for processing  Get_Student get the data into Database.
    - **id**:get the Student in Database
    \f
    :db: Database session.
    :return: JSONResponse with status code and message.
    """
    logging.info("get all the Student triggered.")
    get_student = db.exec(
        select(models.Student).where(models.Student.Std_id == id)
    ).first()
    if get_student is None:
        logging.warning("Student Not in database")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"not in {id} database"
        )
    logging.info("Get the Student Successfully!")
    return get_student


# POST_STUDENT----
@router.post(
    "/Post_Student",
    tags=["STUDENT"],
    response_model=schema.response_student,
    summary="Process Student Upload",
    response_description="File processed to Student successfully.",
    status_code=status.HTTP_202_ACCEPTED,
)
async def Create_Student(request: models.Student, db: Session = Depends(get_db)):
    """
      Endpoint for processing Create_Student Upload data in database
    \f
    :request:Show the request Body of sql model
    :db: Database session.
    :return: JSONResponse with status code and message.
    """
    logging.info("Create Student upload triggered.")
    post_student = db.exec(
        select(models.Student).where(models.Student.Std_id == request.Std_id)
    ).first()
    if post_student:
        logging.warning("student id already in database")
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail=f"already in {request.Std_id} database",
        )
    logging.info("Student Successfully Upload !")

    db.add(request)
    db.commit()
    db.refresh(request)
    return request


# PUT_STUDENT----


@router.put(
    "/Update_Student",
    tags=["STUDENT"],
    response_model=schema.response_student,
    summary="Process Student Upload",
    response_description="File processed to Student successfully.",
    status_code=status.HTTP_202_ACCEPTED,
)
async def Update_Student(request: models.Student, db: Session = Depends(get_db)):
    """
      Endpoint for processing Update_Student Upload data in database
    \f
    :request:Show the request Body of sql model
    :db: Database session.
    :return: JSONResponse with status code and message.
    """
    student = db.exec(
        select(models.Student).where(models.Student.Std_id == request.Std_id)
    ).first()
    logging.info("Update Student triggered.")
    if student is None:
        logging.warning("Student Not in database")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"not in {request.Std_id} database",
        )
    logging.info("Student successfully Updated")
    update = request.model_dump(exclude_unset=True)
    student.sqlmodel_update(update)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


# DELETE_STUDENT----


@router.delete(
    "/Delete_Student",
    tags=["STUDENT"],
    summary="Delete Process Student",
    response_description="File Delete processed to Student successfully.",
    status_code=status.HTTP_200_OK,
)
async def Delete_Student(id: int, db: Session = Depends(get_db)):
    """
    Endpoint for processing Delete_Student Delete the data into Database.
    - **id**:get the Student in User Database
    \f
    :db: Database session.
    :return: JSONResponse with status code and message.
    """
    student = db.exec(select(models.Student).where(models.Student.Std_id == id)).first()
    logging.info("Delete Student triggered.")
    if student is None:
        logging.warning("Student Not in database")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"not in{id} database"
        )
    logging.info("Student successfully Deleted")
    db.delete(student)
    db.commit()
    return student
