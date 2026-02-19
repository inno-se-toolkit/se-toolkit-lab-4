"""Learning Management Service — FastAPI application."""

from fastapi import Depends, FastAPI

from app.auth import verify_api_key
from app.routers import interactions, items, learners
from app.settings import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    description="A learning management service API.",
    version="0.1.0",
)

app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(verify_api_key)],
)

if settings.enable_interactions:
    app.include_router(
        interactions.router,
        prefix="/interactions",
        tags=["interactions"],
        dependencies=[Depends(verify_api_key)],
    )

if settings.enable_learners:
    app.include_router(
        learners.router,
        prefix="/learners",
        tags=["learners"],
        dependencies=[Depends(verify_api_key)],
    )
