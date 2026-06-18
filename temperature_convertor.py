from fastapi import FastAPI
app = FastAPI()

@app.get("/temperature")
def convert_temperature(temperature: float, unit: str):
    if unit == "C":
        converted_temp = (temperature * 9/5) + 32
        return {"result": converted_temp, "unit": "F"}
    elif unit == "F":
        converted_temp = (temperature - 32) * 5/9
        return {"result": converted_temp, "unit": "C"}
    else:
        return {"error": "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."}