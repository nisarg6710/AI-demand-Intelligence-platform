from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_chat_endpoint():

    payload = {
        "question": "Which products are selling the fastest?"
    }

    response = client.post("/chat", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["question"] == payload["question"]
    assert "selected_agents" in data
    assert "response" in data

    assert "inventory" in data["selected_agents"]
    assert data["response"]