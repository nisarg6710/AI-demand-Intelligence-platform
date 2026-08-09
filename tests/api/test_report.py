from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_report_endpoint():

    payload = {
        "question": "Give me an executive report."
    }

    response = client.post("/report", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["question"] == payload["question"]

    assert "selected_agents" in data
    assert "report" in data

    assert "forecast" in data["selected_agents"]
    assert "analytics" in data["selected_agents"]
    assert "inventory" in data["selected_agents"]

    assert data["report"]