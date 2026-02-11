from fastapi.testclient import TestClient


def test_status(client: TestClient):
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "course-material"}
