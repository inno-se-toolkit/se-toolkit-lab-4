def test_get_interactions_returns_200(client, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    response = client.get("/interactions/", headers=headers)
    assert response.status_code == 200

def test_get_interactions_response_is_a_list(client, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    response = client.get("/interactions/", headers=headers)
    assert isinstance(response.json(), list)
