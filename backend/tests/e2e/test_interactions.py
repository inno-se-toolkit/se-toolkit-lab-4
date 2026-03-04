"""End-to-end tests for the /interactions endpoint."""

import httpx


def test_post_interaction_returns_201(client: httpx.Client) -> None:
    response = client.post(
        "/interactions/",
        json={"learner_id": 1, "item_id": 1, "kind": "attempt"},
    )
    assert response.status_code == 201



def test_get_interactions_returns_200(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert isinstance(response.json(), list)
