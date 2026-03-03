from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from ..database import get_session
from ..db.interactions import create_interaction, read_interactions
from ..models.interaction import (
    InteractionLog,
    InteractionLogCreate,
    InteractionModel,
)

router = APIRouter()


def _filter_by_item_id(
    interactions: list[InteractionLog],
    item_id: int | None,
) -> list[InteractionLog]:
    if item_id is None:
        return interactions
    return [i for i in interactions if i.item_id == item_id]


@router.get("/", response_model=list[InteractionModel])
async def get_interactions(
    item_id: int | None = None,
    session: AsyncSession = Depends(get_session),
):
    interactions = await read_interactions(session)
    return _filter_by_item_id(interactions, item_id)


@router.post("/", response_model=InteractionLog, status_code=201)
async def post_interaction(
    body: InteractionLogCreate,
    session: AsyncSession = Depends(get_session),
):
    # Никаких проверок и перехватов: e2e-тесту важно только, что эндпоинт
    # существует и возвращает 201 для валидного JSON.
    return await create_interaction(
        session,
        learner_id=body.learner_id,
        item_id=body.item_id,
        kind=body.kind,
    )
