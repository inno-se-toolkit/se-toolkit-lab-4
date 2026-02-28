"""End-to-end tests for the GET /interactions endpoint."""

import httpx


def test_get_interactions_returns_200(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_interactions_filters_by_item_id(client: httpx.Client) -> None:
    response = client.get("/interactions/?item_id=1")
    assert response.status_code == 200
    interactions = response.json()
    assert isinstance(interactions, list)
    # Verify that all returned interactions have item_id=1
    for interaction in interactions:
        assert interaction["item_id"] == 1
