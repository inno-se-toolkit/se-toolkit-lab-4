"""Database operations for interactions."""

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.interaction import InteractionLog


async def read_interactions(session: AsyncSession) -> list[InteractionLog]:
    """Read all interactions from the database."""
    result = await session.exec(select(InteractionLog))
    return list(result.all())
