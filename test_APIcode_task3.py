from fastapi.testclient import TestClient
from APIcode_task3 import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is functional"}

def test_predict_delays_valid():
    response = client.get("/predict/delays", params={
        "departure_airport": "ATL",
        "arrival_airport": "LAX",
        "departure_time": "2025-03-07T08:00",
        "arrival_time": "2025-03-07T11:00"
    })
    assert response.status_code == 200
    json_response = response.json()
    assert "average_departure_delay_minutes" in json_response
    assert json_response["average_departure_delay_minutes"] == 15.5

def test_predict_delays_missing_params():
    response = client.get("/predict/delays", params={"departure_airport": "ATL"})
    assert response.status_code == 422
    assert "detail" in response.json()