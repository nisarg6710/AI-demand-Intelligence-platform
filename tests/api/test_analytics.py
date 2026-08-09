from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_analytics_endpoint():

    payload = {
        "question": "Show me the monthly sales trend."
    }

    response = client.post("/analytics", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["question"] == payload["question"]
    assert "response" in data
    assert data["response"]