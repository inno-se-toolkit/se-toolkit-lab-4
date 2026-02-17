"""Models for course items."""

from datetime import datetime
from typing import Any, final

from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


# ===
# Database models
# ===
#
# These [`SQLModel`](https://sqlmodel.tiangolo.com/) classes map to the `items`
# PostgreSQL table. `SQLModel` combines SQLAlchemy (database ORM) with
# Pydantic (data validation) in a single class hierarchy.
#
# Items form a tree: course → labs → tasks → steps.
# The tree structure is stored using the
# [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list) pattern (`parent_id`).
# Type-specific attributes are stored in a
# [`JSONB`](https://www.postgresql.org/docs/current/datatype-json.html) column.


class ItemRecord(SQLModel, table=True):
    """A row in the items table."""

    __tablename__ = "items"

    id: int | None = Field(default=None, primary_key=True)
    type: str = "step"
    parent_id: int | None = Field(default=None, foreign_key="items.id")
    title: str
    description: str = ""
    attributes: dict[str, Any] = Field(
        default_factory=dict, sa_column=Column(JSONB, nullable=False)
    )
    created_at: datetime | None = Field(default=None)


class ItemCreate(SQLModel):
    """Schema for creating an item."""

    type: str = "step"
    parent_id: int | None = None
    title: str
    description: str = ""


class ItemUpdate(SQLModel):
    """Schema for updating an item."""

    title: str
    description: str = ""


# ===
# Domain hierarchy
# ===
#
# The classes below model the same items as the database table above,
# but as a **domain model** — a rich Python class hierarchy.
#
# The database stores all items in one flat table (with a `type` discriminator
# and a `parent_id` foreign key). The domain model expresses the same structure
# using inheritance, where each item kind is its own class with kind-specific fields.
#
# This separation is common in real applications and is known as the
# [object-relational impedance mismatch](https://en.wikipedia.org/wiki/Object%E2%80%93relational_impedance_mismatch).

# ===

# This is an example of [inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance).
# Inheritance is a [mechanism in object-oriented programming](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
# that lets you create a class (child) based on another class (parent)
# and modify some implementation details.
#
# Here, `BaseItem` inherits properties of `BaseModel`,
# a fundamental class in [`pydantic`](https://docs.pydantic.dev/latest/concepts/models/)


class BaseItem(BaseModel):
    """A node in the course tree structure.

    Nodes form a tree hierarchy representing course content:
    course -> labs -> tasks -> steps.

    Attributes:
        id: Unique identifier for this item.
        type: The kind of item (e.g., 'course', 'lab', 'task', 'step').
        parent_id: The id of the parent item, or None for root items.
        title: Title of the item.
        description: A longer description of the item.
        created_at: When the item was created.
    """

    id: int
    type: str
    parent_id: int | None = None
    title: str
    description: str = ""
    created_at: datetime | None = None


# It should be possible to use (objects) of the child class
# where objects of its parent class can so that the properties
# of the program that hold when using objects of the parent class
# also hold when using the objects of the child class.
#
# This is called LSP or [Liskov Substitution Principle](https://yakhyo.github.io/solid-python/solid_python/lsp/).
# It's one of the [SOLID](https://en.wikipedia.org/wiki/SOLID) principles.
#
# `pydantic`'s `BaseModel` provides multiple functions that work with objects
# of the class `BaseModel`. `BaseItem` follows the LSP and therefore can be
# used with all those functions and so that these functions work correctly.

# ===

# Here is another example of inheritance.
#
# Here, we inherit from the `BaseItem` class.
# We keep the common fields of the `BaseItem` class such as `id` and `type`.
# We also add new fields such as `steps` in the `Task`.
#
# We can add different fields in different classes
# although they all inherit from the same `BaseItem`.


@final
class Step(BaseItem):
    pass


@final
class Task(BaseItem):
    steps: list[Step] = []


@final
class Lab(BaseItem):
    start: datetime | None = None
    finish: datetime | None = None
    tasks: list[Task] = []


@final
class Course(BaseItem):
    instructors: list[str] | None = None
    start: datetime | None = None
    finish: datetime | None = None
    labs: list[Lab] = []


# ===

# This is an ADT - an [algebraic data type](https://en.wikipedia.org/wiki/Algebraic_data_type).
#
# It's implemented here as a union of four other types (classes).
#
# These classes are decorated with [`@final`](https://docs.python.org/3/library/typing.html#typing.final)
# to disallow further inheritance.
#
# If there was no `@final` at `Step`, we could do like this:
#
# ```python
# class SmallerStep(Step): pass
# item: Item = SmallerStep(id=0, type="smaller-step", title="...")
# ```
#
# However, since these classes are marked as `@final`, no other classes
# can inherit from these classes.
#
# Therefore, no other variants can be added to the `Item` union.
#
# When we later use the `Item` as a variable type, the typechecker will understand
# that the variable must have a value of one of these four types included into the union.
#
# Additional examples of ADTs:
# https://japiirainen.xyz/posts/tips-for-excelling.html#use-sum-and-product-types-for-everything
# https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html#algebraic-data-types
# https://wickstrom.tech/2024-05-23-statically-typed-functional-programming-python-312.html
# https://discuss.python.org/t/encapsulation-of-variants-in-union-s/99630/2

type Item = Step | Task | Lab | Course
