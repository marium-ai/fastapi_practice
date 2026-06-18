from fastapi import FastAPI

app = FastAPI()
@app.get("/about")
def aboutt():
    return{"message":"Hello from Day 2!"}