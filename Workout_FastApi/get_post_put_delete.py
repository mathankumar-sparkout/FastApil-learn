from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel  # import pdantic not import in fastapi

app = FastAPI()

students = {1: {"name": "Arun", "age": 23, "year": 1998}}  # ->dictionary of students


class Student(BaseModel):  # ->basemodel using post method
    name: str
    age: int
    year: int


class updateStudent(BaseModel):
    name: str
    age: int
    year: int


@app.get(
    "/get_student/{student_id}"
)  # -> root(/get_student)-->path parameter (student_id)
async def get_student(
    student_id: int = Path(
        description="stduent details", ge=0
    )  # ->path of the student value column (description is above the student value column)#->greater the value set ,lessthen value set
):
    return students[student_id]  # -> return correct student_id of stdudent column


@app.get(
    "/get_student_name/{student_id}"
)  # -> student_id pathparameter(1,2,3,4)->dictionary id
async def student_name(
    *, name: Optional[str] = None, student_id: int
):  # -> get the student name in student dictionary #->optional method (str:none)
    for (
        student_id
    ) in students:  # -> searching the correct student_id in student dictionary
        if (
            students[student_id]["name"] == name
        ):  # ->if student dictionary[1]["name"]==Arun
            return students[student_id]  # -> return correct student dictionary
    return {"this name not in student list"}  # -> otherwise return message showed


@app.post("/create_student/{student_id}")  # ->student_id path parameter
async def create_student(
    student_id: int, student_submit: Student
):  # ->student_submit(sumbit the new dictionary )
    if student_id in students:  # _ dont repeated in student_id so use if statement
        return {"student already exits"}  # throw error mesaage
    students[student_id] = (
        student_submit  # stusent dictionary[student_id ex(2)]=student_submit(new)
    )
    return students[student_id]  # return new dictionary students


@app.put("/update-students/{student_id}")
async def update_students(
    student_id: int, student_submit: updateStudent
):  # ->updateStudent another basemodel use for put method
    if student_id not in students:  # -> stduent_id not in students dictionary
        return {"Error:student doesnot exits"}  # ->error message
    students[student_id] = (
        student_submit  # ->students(dictionary)[student_id]=update submit
    )
    return students[
        student_id
    ]  # ->return updated student_dictionary->go get method cheack
@app.delete("/delete_student/{student_id}")
async def delete_student(student_id : int):
    if student_id not in students:
        return{"Error:student doesnot exits"}
    del students[student_id]  # using del method
    return{"successfully Deleted "}