import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

import httpx

def test_get_interactions_returns_200():
    base = os.environ.get("API_BASE_URL", "http://127.0.0.1:8000")
    token = os.environ.get("API_TOKEN", "")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    r = httpx.get(f"{base}/interactions/", headers=headers, timeout=10.0)
    assert r.status_code == 200

def test_get_interactions_response_is_a_list():
    base = os.environ.get("API_BASE_URL", "http://127.0.0.1:8000")
    token = os.environ.get("API_TOKEN", "")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    r = httpx.get(f"{base}/interactions/", headers=headers, timeout=10.0)
    assert isinstance(r.json(), list)
