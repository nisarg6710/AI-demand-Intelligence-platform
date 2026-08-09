from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_forecast_endpoint():

    payload = {
        "question": "What is the best forecasting model?"
    }

    response = client.post("/forecast", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["question"] == payload["question"]
    assert data["selected_action"] == "get_best_model"
    assert "response" in data
    assert data["response"]