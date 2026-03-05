"""End-to-end tests for the GET /interactions endpoint."""

import os

import httpx
import pytest

BASE_URL = os.environ.get("API_BASE_URL", "http://127.0.0.1:42001")
API_TOKEN = os.environ.get("API_TOKEN", "my-secret-api-key")


@pytest.fixture
def client() -> httpx.Client:
    """Create an HTTP client for testing."""
    return httpx.Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_TOKEN}"})


def test_get_interactions_returns_200(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns HTTP status code 200."""
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    """Test that GET /interactions/ response body is a JSON array."""
    response = client.get("/interactions/")
    data = response.json()
    assert isinstance(data, list)
