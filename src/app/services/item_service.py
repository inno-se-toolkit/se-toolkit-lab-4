"""Service for loading and querying course items from JSON data."""

from dataclasses import dataclass

import json
import operator
from typing import List, Optional, final

from pydantic import TypeAdapter
from app.models.order import Order, PostOrder, PreOrder
from app.settings import settings
from app.models.item import Item, Course, Lab, Task, Step

# ===
#
# This module demonstrates the basics of functional programming.
#
# Approaches used here help:
# - improve [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) such as:
#   - [static type checking](https://en.wikipedia.org/wiki/Type_system#Type_checking);
#   - [type inference](https://en.wikipedia.org/wiki/Type_inference).
# - make the code testable and DRY;
# - improve auto-completion based on the information about types.
#
# Approach 1:
# 
# We heavily rely on static typing.
# 
# We provide types almost everywhere to ensure each variable and function 
# has a known type other than `Any` or `Unknown`.
# 
# One can sometimes understand what a function does just by looking at 
# its name, argument names and their types, and the result type.
# 
# Unlike comments that can get obsolete, the documentation based on types 
# is usually always up to date.
# Running a type checker helps ensure that the program is well-typed.
# 
# Running a type checker before running an extensively typed program 
# helps eliminate entire classes of problems that can happen at runtime.
# 
# Approach 2:
#
# This module follows the principles described in the article
# [Functional Core, Imperative Shell](https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html).
#
# We express the main logic using pure, testable functions whose output depends
# only on their arguments. These functions don't cause any side effects such as
# input-output or external state mutation.
#
# After that, we define impure functions that construct arguments for the pure
# functions and cause side effects such as reading a file.
#
# Approach 3:
#
# We use Python [generics](https://typing.python.org/en/latest/reference/generics.html)
# a.k.a. [Parametric polymorphism](https://en.wikipedia.org/wiki/Parametric_polymorphism)
# ([examples](https://rosettacode.org/wiki/Parametric_polymorphism#Python))
# to write [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) reusable code.
#
# We also use generics to tell other developers where a function can
# and where it can't be used with the help of the type checker.
#
# Approach 4:
#
# We use the algebraic data type `Item` (see `src/app/models/item.py` for details)
# to constrain which types a variable of type `Item` can have.
# Hint: it can have any type from the `Item` union, i.e., `Class`, `Lab`, `Task`, `Step`.
#
# We also use the algebraic data type `Order` (see `src/app/models/order.py`)
# to specify the two orders of the depth-first [tree traversal](https://en.wikipedia.org/wiki/Tree_traversal).
# 
# ===

# ===
#
# This is a [generic function](https://typing.python.org/en/latest/reference/generics.html#generic-functions).
# This function works with any subtypes of `Item`.
# That is, it works only with subtypes in the `Item` union.
# There are only four such types: `Class`, `Lab`, `Step`, `Task`.
# The function won't work with any other type such as `int` or `BaseItem`.
#
# The type checker will show an error when people try to write
# code where this functions takes as argument `items` with type `List[int]`.
# People will see an error before running the code.
#
# That's how one can communicate constraints using types.
# 
# ===


def find_by_id[T: Item](items: List[T], item_id: str) -> Optional[T]:
    """
    Searches a list of items for a specific ID.
    Returns the item if found, otherwise None.
    """
    for item in items:
        if item.id == item_id:
            return item
    return None


# ===
#
# Each of these functions uses `find_by_id`.
# In each function, `find_by_id` has `T` replaced with a particular type
# based on the type of its arguments.
#
# When `courses` has type `List[Course]`,
# the argument of `find_by_id` called `items` also has the type `List[Course]`.
# 
# ===


def get_course_by_id(courses: List[Course], course_id: str) -> Optional[Course]:
    return find_by_id(items=courses, item_id=course_id)


def get_lab_by_id(course: Course, lab_id: str) -> Optional[Lab]:
    return find_by_id(items=course.labs, item_id=lab_id)


def get_task_by_id(lab: Lab, task_id: str) -> Optional[Task]:
    return find_by_id(items=lab.tasks, item_id=task_id)


def get_step_by_id(task: Task, step_id: str) -> Optional[Step]:
    return find_by_id(items=task.steps, item_id=step_id)


# ===
# 
# ===


def get_course_by_path(courses: List[Course], course_id: str) -> Optional[Course]:
    return get_course_by_id(courses=courses, course_id=course_id)


def get_lab_by_path(
    courses: List[Course], course_id: str, lab_id: str
) -> Optional[Lab]:
    course = get_course_by_path(courses=courses, course_id=course_id)
    if course is not None:
        return get_lab_by_id(course=course, lab_id=lab_id)
    return None


def get_task_by_path(
    courses: List[Course], course_id: str, lab_id: str, task_id: str
) -> Optional[Task]:
    lab = get_lab_by_path(courses=courses, course_id=course_id, lab_id=lab_id)
    if lab is not None:
        return get_task_by_id(lab=lab, task_id=task_id)
    return None


def get_step_by_path(
    courses: List[Course], course_id: str, lab_id: str, task_id: str, step_id: str
) -> Optional[Step]:
    task = get_task_by_path(
        courses=courses, course_id=course_id, lab_id=lab_id, task_id=task_id
    )
    if task is not None:
        return get_step_by_id(task=task, step_id=step_id)
    return None


# ===
# 
# ===


@final
@dataclass
class FoundItem:
    """
    Helper type for search results
    """

    item: Item
    visited_nodes: int


def get_item_by_id_dfs_iterative(
    courses: List[Course], item_id: str, order: Order
) -> Optional[FoundItem]:
    """Find an item by its id.

    Searches through all courses and their nested items.

    Uses depth-first search (DFS) in a specific order.

    See:
    - [Depth-first search](https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search)
    - [Depth-first search example](https://en.wikipedia.org/wiki/Depth-first_search#Example)

    Args:
        courses: a list of course info objects
        item_id: The unique identifier of the item to find.
        order: order in which to search

    Returns:
        The FoundItem if found, None otherwise.
    """
    counter = 0
    match order:
        case PreOrder():
            for course in courses:
                counter += 1
                if course.id == item_id:
                    return FoundItem(course, counter)

                for lab in course.labs:
                    counter += 1
                    if lab.id == item_id:
                        return FoundItem(lab, counter)

                    for task in lab.tasks:
                        counter += 1
                        if lab.id == item_id:
                            return FoundItem(task, counter)

                        for step in task.steps:
                            counter += 1
                            if step.id == item_id:
                                return FoundItem(step, counter)
        case PostOrder():
            # TODO implement
            pass
    return None


# ===
# 
# ===


def get_item_by_id_dfs_recursive[T: Item](
    items: List[T], item_id: str, order: Order
) -> Optional[FoundItem]:
    visited_nodes: int = 0

    def get_item_by_id_dfs_recursive_[P: Item](
        items: List[P], item_id: str, order: Order
    ) -> Optional[FoundItem]:
        nonlocal visited_nodes

        for item in items:
            match order:
                case PreOrder():
                    visited_nodes += 1
                    if item.id == item_id:
                        return FoundItem(item=item, visited_nodes=visited_nodes)
                case _:
                    pass

            @operator.call
            def go_items() -> Optional[FoundItem]:
                def go[S: Item](items: List[S]):
                    return get_item_by_id_dfs_recursive_(
                        items=items,
                        item_id=item_id,
                        order=order,
                    )

                match item:
                    case Course():
                        return go(items=item.labs)
                    case Lab():
                        return go(items=item.tasks)
                    case Task():
                        return go(items=item.steps)
                    case Step():
                        return

            if go_items is not None:
                return go_items

            match order:
                case PostOrder():
                    visited_nodes += 1
                    if item.id == item_id:
                        return FoundItem(item=item, visited_nodes=visited_nodes)
                case _:
                    pass
        return None

    return get_item_by_id_dfs_recursive_(items=items, item_id=item_id, order=order)


# ===
# 
# `TypeAdapter` wraps another type and makes it look like `BaseModel`.
# See [docs](https://docs.pydantic.dev/latest/concepts/type_adapter/)
# 
# ===

CoursesAdapter = TypeAdapter(type=List[Course])

# ===
# 
# These are impure functions that cause side effects such as reading a file.
# 
# ===


def read_courses() -> List[Course]:
    with open(settings.course_items_path, "r", encoding="utf-8") as handle:
        raw = json.load(handle)

    return CoursesAdapter.validate_python(raw)


def get_item_by_id(item_id: str, order: Order) -> Optional[FoundItem]:
    courses: list[Course] = read_courses()
    return get_item_by_id_dfs_iterative(courses=courses, item_id=item_id, order=order)
