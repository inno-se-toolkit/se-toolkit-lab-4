"""Pydantic models for interactions."""

from datetime import datetime

from sqlmodel import Field, SQLModel


class InteractionLog(SQLModel, table=True):
    """An interaction log entry in the database."""

    __tablename__ = "interaction_logs"

    id: int | None = Field(default=None, primary_key=True)
    learner_id: int
    item_id: int
    kind: str
    created_at: datetime | None = Field(default=None)


class InteractionModel(SQLModel):
    """Response schema for an interaction."""

    id: int
    learner_id: int
    item_id: int
    kind: str
    timestamp: datetime  # BUG: should be 'created_at' to match the database column
