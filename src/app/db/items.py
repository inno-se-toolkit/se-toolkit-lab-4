"""Database operations for items."""

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.item import ItemRecord


async def read_items(session: AsyncSession) -> list[ItemRecord]:
    """Read all items from the database."""
    result = await session.exec(select(ItemRecord))
    return list(result.all())


async def read_item(session: AsyncSession, item_id: int) -> ItemRecord | None:
    """Read a single item by id."""
    return await session.get(ItemRecord, item_id)


async def create_item(
    session: AsyncSession, title: str, description: str
) -> ItemRecord:
    """Create a new item in the database."""
    item = ItemRecord(title=title, description=description)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def update_item(
    session: AsyncSession, item_id: int, title: str, description: str
) -> ItemRecord | None:
    """Update an existing item in the database."""
    item = await session.get(ItemRecord, item_id)
    if item is None:
        return None
    item.title = title
    item.description = description
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item
