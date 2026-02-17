"""Router for interaction endpoints."""

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.interactions import read_interactions
from app.models.interaction import InteractionModel

router = APIRouter()


@router.get("/", response_model=list[InteractionModel])
async def get_interactions(
    item_id: int | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all interactions, optionally filtered by item."""
    interactions = await read_interactions(session)
    if item_id is not None:
        interactions = [
            i for i in interactions if i.learner_id == item_id
        ]  # BUG: should filter by i.item_id
    return interactions
