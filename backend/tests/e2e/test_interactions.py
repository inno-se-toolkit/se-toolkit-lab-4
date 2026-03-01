"""End-to-end tests for the GET /interactions endpoint."""
def test_get_interactions_returns_200(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns HTTP 200 OK."""
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns a JSON array."""
    response = client.get("/interactions/")
    data = response.json()
    assert isinstance(data, list)