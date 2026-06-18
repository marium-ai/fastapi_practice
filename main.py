from fastapi import FastAPI, Path, HTTPException, Query
import json
from typing import List

app = FastAPI()

def load_data():
    try:
        with open("patient.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="patient.json not found on server")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="patient.json is not valid JSON")
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management system API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi", example="height"),
    order: str = Query("asc", description="Sort in asc or desc order", example="asc")
) -> List[dict]:
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field selected. Choose from {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Choose 'asc' or 'desc'")

    data = load_data()  # fixed: call the function
    # data expected as dict {id: {...}}
    patients = []
    for pid, info in data.items():
        rec = dict(info)  # copy
        rec["id"] = pid
        patients.append(rec)

    def parse_num(x):
        try:
            return float(x)
        except (TypeError, ValueError):
            return float("nan")

    # sort by numeric value of the field, placing invalid/missing values at the end
    reverse = (order == "desc")
    patients_sorted = sorted(
        patients,
        key=lambda r: (parse_num(r.get(sort_by)), r.get("id")),
        reverse=reverse
    )
    return patients_sorted