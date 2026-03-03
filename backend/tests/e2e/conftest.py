"""Shared fixtures for end-to-end tests."""

import httpx
import pytest


@pytest.fixture(scope="session")
def api_base_url() -> str:
    # Локально backend крутится на http://127.0.0.1:8000
    return "http://127.0.0.1:8000"


@pytest.fixture(scope="session")
def api_token() -> str:
    # Для этой лабораторной авторизация выключена
    return ""


@pytest.fixture(scope="session")
def client(api_base_url: str, api_token: str) -> httpx.Client:
    headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}
    return httpx.Client(
        base_url=api_base_url,
        headers=headers,
    )
