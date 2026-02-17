"""Router for item endpoints — reference implementation."""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.items import create_item, read_item, read_items, update_item
from app.models.item import ItemCreate, ItemRecord, ItemUpdate

router = APIRouter()


@router.get("/", response_model=list[ItemRecord])
async def get_items(session: AsyncSession = Depends(get_session)):
    """Get all items."""
    return await read_items(session)


@router.get("/{item_id}", response_model=ItemRecord)
async def get_item(item_id: int, session: AsyncSession = Depends(get_session)):
    """Get a specific item by its id."""
    item = await read_item(session, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemRecord, status_code=201)
async def post_item(body: ItemCreate, session: AsyncSession = Depends(get_session)):
    """Create a new item."""
    return await create_item(session, title=body.title, description=body.description)


@router.put("/{item_id}", response_model=ItemRecord)
async def put_item(
    item_id: int, body: ItemUpdate, session: AsyncSession = Depends(get_session)
):
    """Update an existing item."""
    item = await update_item(
        session, item_id=item_id, title=body.title, description=body.description
    )
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
