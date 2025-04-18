from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Mock prediction function (replace with your ML model later)
def predict_delay(departure_airport: str, arrival_airport: str, dep_time: str, arr_time: str) -> float:
    # Placeholder: returns a fixed delay for demo purposes
    return 15.5  # Average delay in minutes

@app.get("/")
def read_root():
    return {"message": "API is functional"}

@app.get("/predict/delays")
def predict_delays(departure_airport: str, arrival_airport: str, departure_time: str, arrival_time: str):
    delay = predict_delay(departure_airport, arrival_airport, departure_time, arrival_time)
    return {
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "average_departure_delay_minutes": delay
    }