from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
students = []
class Student(BaseModel):
    name: str = Field(..., min_length=1, description="Student's name must be at least 1 character long")
    age: int = Field(..., description="Student's age")
    marks: float = Field(..., ge=0, le=100, description="Student's marks must be between 0 and 100")
@app.post("/students")
def create_student(student: Student):
    if not student.name.strip():
        return {"message": "Student's name cannot be empty"}
    students.append(student)
    position = len(students) - 1
    return {
        "message": "Student created successfully",
        "student": student,
        "position": position

    }
@app.get("/students")
def get_all_students():
    return {
        "message": "List of all students",
        "total_students": len(students),
        "all_students": students

    }
@app.get("/students/{position}")
def get_student_by_position(position: int):
    if 0 <= position < len(students):
        return {
            "message": "Student found",
            "student": students[position]
        }
    return {"message": "Student not found"}
@app.put("/students/{position}")
def update_student(position: int, updated_student: Student):
    if 0 <= position < len(students):
        if not updated_student.name.strip():
            return {"message": "Student's name cannot be empty"}
        students[position] = updated_student
        return {
            "message": "Student updated successfully",
            "student": updated_student
        }
    return {"message": "Student not found"}
@app.delete("/students/{position}")
def delete_student(position: int):
    if 0 <= position < len(students):
        deleted_student = students.pop(position)
        return {
            "message": "Student deleted successfully",
            "student": deleted_student
        }
    return {"message": "Student not found"}
1