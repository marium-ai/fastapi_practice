from fastapi import FastAPI
from pydantic import BaseModel
app =FastAPI()
menu=[
    {"id": 1, "name": "Iced Latte", "price": 350},
    {"id": 2, "name": "Cappuccino", "price": 400},
    {"id": 3, "name": "Espresso", "price": 300},
    {"id":4, "name": "Mocha", "price": 450},
]
@app.get("/menu")
def get_menu():
    return{"menu": menu}
class Item(BaseModel):
    Id: int
    name: str
    price: float
@app.post("/menu")
def add_item(item: Item):
    menu.append(item.dict())
    return {"message": "Item added successfully", "item": item}
@app.put("/menu/{item_id}")
def update_item_price(item_id: int, new_price: float):

    for item in menu:
        if item["id"] == item_id:
            
            item["price"] = new_price
            
            return {
                "message": "Price updated successfully", 
                "updated_item": item
            }
            
    return {"message": "Item not found"}