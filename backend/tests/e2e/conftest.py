"""Shared fixtures for end-to-end tests."""

import os

import httpx
import pytest


@pytest.fixture(scope="session")
def api_base_url() -> str:
    url = os.environ.get("API_BASE_URL", "")
    if not url:
        pytest.skip("API_BASE_URL environment variable is not set")
    return url.rstrip("/")


@pytest.fixture(scope="session")
def api_token() -> str:
    token = os.environ.get("API_TOKEN", "")
    if not token:
        pytest.skip("API_TOKEN environment variable is not set")
    return token


@pytest.fixture(scope="session")
def client(api_base_url: str, api_token: str) -> httpx.Client:
    return httpx.Client(
        base_url=api_base_url,
        headers={"Authorization": f"Bearer {api_token}"},
    )
