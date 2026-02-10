from fastapi.testclient import TestClient

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.main import app
import pytest


class Settings(BaseSettings):
    address: str = Field(default="127.0.0.1", alias="ADDRESS")
    port: int = Field(default=8000, alias="PORT")

    @property
    def base_url(self) -> str:
        return f"http://{self.address}:{self.port}"

    model_config = SettingsConfigDict(
        env_file=".env.secret", env_file_encoding="utf-8", case_sensitive=True, extra="allow"
    )


@pytest.fixture
def settings():
    return Settings()


@pytest.fixture
def client(settings: Settings):
    return TestClient(app=app, base_url=settings.base_url)
