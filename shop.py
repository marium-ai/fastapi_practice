from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    name: str
    price: int
    stock: int

item_availble= [
    Item(item_id=1, name="Wireless Mouse", price=500, stock=3),
    Item(item_id=2, name="Mechanical Keyboard", price=1500, stock=0),
    Item(item_id=3, name="HD Monitor", price=8000, stock=2),
]


cart = {}
app = FastAPI()
@app.get("/item")
def get_items():
  return {
    "message": "List of available items",
    "items": item_availble

}
@app.post("/cart/add/{item_id}")
def add_to_cart(item_id: int, quantity: int):
   selected_item =None
   for item in item_availble:
       if item.item_id == item_id:
           selected_item = item
           break
   
   if not selected_item:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
   if selected_item.stock < quantity:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient stock")
   cart[item_id]=quantity
   selected_item.stock -= quantity
   return {
     "message": f"Added {quantity} of {selected_item.name} to cart",
     "cart": cart
    }
