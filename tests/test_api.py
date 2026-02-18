import pytest
from fastapi.testclient import TestClient
from app.main import app  # matches the folder structure now

client = TestClient(app)

def test_ask_endpoint_status():
    response = client.post("/ask", json={"question": "Test question"})
    assert response.status_code == 200

def test_ask_endpoint_response_structure():
    response = client.post("/ask", json={"question": "Test question"})
    data = response.json()
    assert "answer" in data
    assert "sources" in data

def test_ask_endpoint_non_empty_answer():
    response = client.post("/ask", json={"question": "Test question"})
    data = response.json()
    assert len(data["answer"]) > 0
