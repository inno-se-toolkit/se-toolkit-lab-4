from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..database import get_session
from ..models.learner import Learner, LearnerCreate, LearnerRead


router = APIRouter()


@router.get("/", response_model=list[LearnerRead])
async def get_learners(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Learner))
    return list(result.scalars().all())


@router.get("/{learner_id}", response_model=LearnerRead)
async def get_learner(
    learner_id: int,
    session: AsyncSession = Depends(get_session),
):
    result = await session.exec(
        select(Learner).where(Learner.id == learner_id)
    )
    learner = result.scalar_one_or_none()
    if learner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Learner not found",
        )
    return learner


@router.post("/", response_model=LearnerRead, status_code=201)
async def create_learner(
    body: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    learner = Learner(name=body.name, email=body.email)
    session.add(learner)
    await session.commit()
    await session.refresh(learner)
    return learner