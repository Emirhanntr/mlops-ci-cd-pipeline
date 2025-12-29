from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint_works():
    r = client.post("/predict", json={"user_id": "user_123"})
    assert r.status_code == 200
    data = r.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], float)
