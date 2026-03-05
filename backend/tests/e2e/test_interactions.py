import httpx

def test_get_interactions_returns_200(client: httpx.Client) -> None:
    """Test that GET /interactions/ returns 200 OK."""
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_items_have_expected_fields(client: httpx.Client) -> None:
    """Test that response items contain expected fields."""
    response = client.get("/interactions/")
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "item_id" in data[0]
    assert "created_at" in data[0]  # Должно быть created_at, не timestamp


def test_get_interactions_filter_includes_boundary(client: httpx.Client) -> None:
    """Test that filter with max_item_id includes boundary value."""
    response = client.get("/interactions/?max_item_id=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert all(item["item_id"] <= 1 for item in data)