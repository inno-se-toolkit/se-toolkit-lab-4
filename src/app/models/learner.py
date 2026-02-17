"""Pydantic models for learners."""

from datetime import datetime

from sqlmodel import Field, SQLModel


class Learner(SQLModel, table=True):
    """A learner in the learning management system."""

    __tablename__ = "learners"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    enrolled_at: datetime | None = Field(default=None)


class LearnerCreate(SQLModel):
    """Schema for creating a learner."""

    name: str
    email: str
