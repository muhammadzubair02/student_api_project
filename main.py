from fastapi import FastAPI
from pydantic import BaseModel, field_validator
app = FastAPI()

students = []

class Student(BaseModel):
    id : int
    name : str
    age : int
    course : str
    @field_validator("name")
    def name_must_be_letter(cls, value):
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value

@app.get("/")
def home():
    return {"message": "Student Management API Running"}

@app.post("/students")
def add_student(student : Student):
    students.append(student)
    return {"message": "Students Added", "data": student}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted"}
    return {"error": "Student not found"}
