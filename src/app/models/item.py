"""Models for course items."""

from datetime import datetime
from typing import Dict, List, Optional, final

from pydantic import BaseModel


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
        type: The type of item (e.g., 'course', 'lab', 'task', 'step').
        icon: An icon of the item.
        titles: Localized titles (e.g., {'en': 'Lab 01'}).
        descriptions: Localized descriptions.
    """

    id: str
    type: str
    icon: Optional[str] = None
    titles: Optional[Dict[str, str]] = None
    descriptions: Optional[Dict[str, str]] = None


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
# We keep the common fields of the `BaseItem` class such as `id` and `date`.
# We also add new fields such as `steps` in the `Task`.
#
# We can add different fields in different classes
# although they all inherit from the same `BaseItem`.


@final
class Step(BaseItem):
    pass


@final
class Task(BaseItem):
    steps: List[Step] = []


@final
class Lab(BaseItem):
    start: Optional[datetime] = None
    finish: Optional[datetime] = None
    tasks: List[Task] = []


@final
class Course(BaseItem):
    instructors: Optional[List[str]] = None
    start: Optional[datetime] = None
    finish: Optional[datetime] = None
    labs: List[Lab] = []


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
# item: Item = SmallerStep(id="some-id", type="smaller-step")
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
