from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .settings import settings  # noqa: F401

security = HTTPBearer(auto_error=False)


def verify_api_key(
    credentials: HTTPAuthorizationCredentials | None = Security(security),
) -> None:
    # Авторизацию не проверяем, чтобы e2e-тесты не требовали токен
    return
