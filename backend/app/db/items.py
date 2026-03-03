from typing import Sequence

from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..models.item import ItemRecord


async def read_items(session: AsyncSession) -> list[ItemRecord]:
    result = await session.exec(select(ItemRecord))
    return list(result.scalars().all())


async def read_item(session: AsyncSession, item_id: int) -> ItemRecord | None:
    result = await session.exec(
        select(ItemRecord).where(ItemRecord.id == item_id)
    )
    return result.scalar_one_or_none()


async def create_item(
    session: AsyncSession,
    type: str,
    parent_id: int | None,
    title: str,
    description: str,
) -> ItemRecord:
    item = ItemRecord(
        type=type,
        parent_id=parent_id,
        title=title,
        description=description,
    )
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def update_item(
    session: AsyncSession,
    item_id: int,
    title: str | None,
    description: str | None,
) -> ItemRecord | None:
    item = await read_item(session, item_id)
    if item is None:
        return None

    if title is not None:
        item.title = title
    if description is not None:
        item.description = description

    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item
