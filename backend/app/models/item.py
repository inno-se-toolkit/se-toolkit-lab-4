from datetime import datetime
from typing import Any

from sqlalchemy import JSON
from sqlmodel import Field, SQLModel


class ItemRecord(SQLModel, table=True):
    __tablename__ = "item"

    id: int | None = Field(default=None, primary_key=True)
    type: str = Field(default="step")
    parent_id: int | None = Field(default=None, foreign_key="item.id")
    title: str
    description: str = Field(default="")
    attributes: dict[str, Any] = Field(
        default_factory=dict,
        sa_type=JSON,
    )
    created_at: datetime | None = None


class ItemCreate(SQLModel):
    type: str = "step"
    parent_id: int | None = None
    title: str
    description: str = ""


class ItemUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
