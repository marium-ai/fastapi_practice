from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Student(BaseModel):
    name: str
    age: int
    roll_No: int
    finger_print: str
class StudentResponse(BaseModel):
    name: str
    age: int
    roll_No: int
@app.get("/student",response_model=StudentResponse)        
def get_student():
    return {
        "name": "marium",
        "age": 16,
        "roll_No": 502838,
        "finger_print": "abc124"

    }