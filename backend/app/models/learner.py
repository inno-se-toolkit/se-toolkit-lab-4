from datetime import datetime

from sqlmodel import Field, SQLModel


class Learner(SQLModel, table=True):
    __tablename__ = "learner"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    enrolled_at: datetime | None = None


class LearnerCreate(SQLModel):
    name: str
    email: str


class LearnerRead(SQLModel):
    id: int
    name: str
    email: str
    enrolled_at: datetime | None = None
