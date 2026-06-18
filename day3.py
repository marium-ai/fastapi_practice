from fastapi import FastAPI
app = FastAPI()

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/square")
def square(x: int):
    return {"result": x ** 2}
#check number is even or odd
@app.get("/even_odd")
def even_odd(n: int):
    if n % 2 == 0:
        return {"result": "even"}
    else:
        return {"result": "odd"}

#repeat text
@app.get("/repeat")
def repeat(text: str, times: int):
    return {"result": text * times}
