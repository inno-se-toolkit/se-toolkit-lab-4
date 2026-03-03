"""End-to-end tests for interactions endpoints."""

import httpx
import pytest

# Mark all tests in this module as e2e
pytestmark = pytest.mark.e2e


def test_get_interactions_returns_200(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns status code 200"""
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns a JSON array"""
    response = client.get("/interactions/")
    data = response.json()
    assert isinstance(data, list)
