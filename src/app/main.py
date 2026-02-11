"""Course Materials Service - FastAPI application.

A read-only service that serves course-related items (courses, labs, tasks, steps)
from JSON data files.
"""

from fastapi import FastAPI
from app.settings import settings
from app.routers import items, status

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    description="A read-only API for accessing course structure and learning materials.",
    version="0.1.0",
)

app.include_router(status.router, tags=["status"])
app.include_router(items.router, prefix="/items", tags=["items"])
