from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..models.interaction import InteractionLog


async def read_interactions(session: AsyncSession) -> list[InteractionLog]:
    result = await session.exec(select(InteractionLog))
    return list(result.scalars().all())


async def create_interaction(
    session: AsyncSession,
    learner_id: int,
    item_id: int,
    kind: str,
) -> InteractionLog:
    interaction = InteractionLog(
        learner_id=learner_id,
        item_id=item_id,
        kind=kind,
    )
    session.add(interaction)
    await session.commit()
    await session.refresh(interaction)
    return interaction
