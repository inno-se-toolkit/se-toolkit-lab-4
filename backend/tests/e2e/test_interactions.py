"""End-to-end tests for the GET /interactions endpoint."""
def test_get_interactions_returns_200():
    """Test that GET /interactions/ returns status code 200"""
    response = client.get("/interactions/")
    assert response.status_code == 200

def test_get_interactions_response_is_a_list():
    """Test that GET /interactions/ returns a JSON array"""
    response = client.get("/interactions/")
    data = response.json()
    assert isinstance(data, list)