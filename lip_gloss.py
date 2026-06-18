import json
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def load_data():
    with open("lip_gloss.json", "r") as f:
        data = json.load(f)
    return data["brands"] 
class LipGloss(BaseModel):
    id: int
    brand: str
    shades: list  
    price: float
    in_stock: bool
    description: str

@app.get("/lip_gloss")
def get_lip_gloss():
    return load_data()

@app.get("/lip_gloss/{lip_gloss_brand}")
def get_lip_gloss_by_brand(lip_gloss_brand: str, shade: Optional[str] = None):
    data = load_data()
    for item in data:
        if item["brand"].lower() == lip_gloss_brand.lower():
            if shade is None:
                return item
            elif shade.lower() in [s.lower() for s in item["shades"]]:
                return item
    return {"message": "Lip gloss not found"}