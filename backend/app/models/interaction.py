from datetime import datetime

from sqlalchemy import func
from sqlmodel import Field, SQLModel


class InteractionLog(SQLModel, table=True):
    __tablename__ = "interacts"

    id: int | None = Field(default=None, primary_key=True)
    learner_id: int = Field(foreign_key="learner.id")
    item_id: int = Field(foreign_key="item.id")
    kind: str
    created_at: datetime | None = Field(
        default=None,
        sa_column_kwargs={"server_default": func.now()},
    )



class InteractionLogCreate(SQLModel):
    learner_id: int
    item_id: int
    kind: str


class InteractionModel(SQLModel):
    id: int
    learner_id: int
    item_id: int
    kind: str
    created_at: datetime | None = None
