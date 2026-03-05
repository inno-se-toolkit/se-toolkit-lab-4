"""Shared fixtures for end-to-end tests."""

import httpx
import pytest
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_base_url: str = Field(..., alias="API_BASE_URL")
    api_key: str = Field(..., alias="API_KEY")

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow"
    )


@pytest.fixture(scope="session")
def client() -> httpx.Client:
    try:
        s = Settings.model_validate({})
    except ValidationError:
        pytest.skip(".env.tests.secret is missing or incomplete")
    return httpx.Client(
        base_url=s.api_base_url.rstrip("/"),
        headers={"Authorization": f"Bearer {s.api_key}"},
    )
