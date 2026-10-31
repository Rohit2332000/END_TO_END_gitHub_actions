from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_addition():
    response = client.post("/add", json={"a": 10, "b": 20})
    assert response.status_code == 200
    assert response.json()["result"] == 30


def test_multiplication():
    response = client.post("/multiply", json={"a": 5, "b": 4})
    assert response.status_code == 200
    assert response.json()["result"] == 20


def test_invalid_input():
    response = client.post("/add", json={"a": "invalid", "b": 10})
    assert response.status_code == 422
