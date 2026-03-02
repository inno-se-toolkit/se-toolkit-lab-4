"""Learning Management Service — FastAPI application."""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import verify_api_key
from app.routers import interactions, items, learners
from app.settings import settings

from fastapi.responses import Response

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    description="A learning management service API.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  # разрешаем все заголовки
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

@app.options("/{rest_of_path:path}")
async def preflight_handler(rest_of_path: str):
    return Response(
        content="",
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "authorization, x-kl-ajax-request, content-type",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Max-Age": "600",
        },
    )
