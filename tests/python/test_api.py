from fastapi.testclient import TestClient

from endpointops.api import app


def test_dashboard_returns_summary():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "EndpointOps 365" in response.text
    assert "Synthetic" in response.text


def test_patch_risk_endpoint_returns_rows():
    client = TestClient(app)
    response = client.get("/api/patch-risk")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] > 0
    assert data["items"][0]["risk_score"].isdigit()
