from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI()
class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"message": f"User {user.name} created successfully", "age": user.age}

#product model
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
@app.post("/product")
def create_product(product: Product):
    return {"message": f"Product {product.name} created successfully", "price": product.price, "in_stock": product.in_stock}    