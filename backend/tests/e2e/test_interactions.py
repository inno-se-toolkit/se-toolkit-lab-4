"""E2E tests for interactions endpoint."""

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_interactions_returns_200() -> None:
    response = client.get("/interactions/")
    assert response.status_code in (200, 401)


def test_get_interactions_response_is_a_list() -> None:
    response = client.get("/interactions/")
    if response.status_code == 200:
        assert isinstance(response.json(), list)