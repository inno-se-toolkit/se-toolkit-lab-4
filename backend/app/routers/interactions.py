"""Router for interaction endpoints."""

from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.interactions import read_interactions
from app.models.interaction import InteractionLog, InteractionModel

router = APIRouter()


def _filter_by_item_id(
    interactions: list[InteractionLog], item_id: int | None
) -> list[InteractionLog]:
    if item_id is None:
        return interactions
    return [i for i in interactions if i.learner_id == item_id]


@router.get("/", response_model=list[InteractionModel])
async def get_interactions(
    item_id: int | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all interactions, optionally filtered by item."""
    interactions = await read_interactions(session)
    return _filter_by_item_id(interactions, item_id)
