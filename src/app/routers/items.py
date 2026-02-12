"""Router for course items endpoints."""

from typing import List
from fastapi import APIRouter, HTTPException

from app.models.item import Course, Lab, Step
from app.models.order import PreOrder, parse_order_default
from app.services.item_service import (
    FoundItem,
    get_course_by_path,
    get_lab_by_path,
    get_item_by_id,
    read_courses,
    get_step_by_path,
    get_task_by_path,
)

router = APIRouter()


@router.get("/courses", response_model=List[Course])
def get_all_courses():
    """Get all courses.

    Returns:
        A list of all courses.
    """
    return read_courses()


@router.get("/course/{course_id}", response_model=Course)
def get_course(course_id: str):
    courses = read_courses()
    course = get_course_by_path(courses=courses, course_id=course_id)

    if course is not None:
        return course

    raise HTTPException(status_code=404, detail="Course not found")


@router.get("/course/{course_id}/lab/{lab_id}", response_model=Lab)
def get_lab(course_id: str, lab_id: str):
    courses = read_courses()
    lab = get_lab_by_path(courses=courses, course_id=course_id, lab_id=lab_id)

    if lab is not None:
        return lab

    raise HTTPException(status_code=404, detail="Lab not found")


@router.get("/course/{course_id}/lab/{lab_id}/task/{task_id}", response_model=Step)
def get_task(course_id: str, lab_id: str, task_id: str):
    courses = read_courses()
    task = get_task_by_path(
        courses=courses, course_id=course_id, lab_id=lab_id, task_id=task_id
    )

    if task is not None:
        return task

    raise HTTPException(status_code=404, detail="Task not found")


@router.get(
    "/course/{course_id}/lab/{lab_id}/task/{task_id}/step/{step_id}",
    response_model=Step,
)
def get_step(course_id: str, lab_id: str, task_id: str, step_id: str):
    courses = read_courses()
    step = get_step_by_path(
        courses=courses,
        course_id=course_id,
        lab_id=lab_id,
        task_id=task_id,
        step_id=step_id,
    )

    if step is not None:
        return step

    raise HTTPException(status_code=404, detail="Step not found")


@router.get("/item/{item_id}", response_model=FoundItem)
def get_item(item_id: str, order: str = PreOrder.short_name):
    """Get a specific item by its id.

    Searches through all courses and their nested items to find
    the item with the matching id.
    Traverses the course tree in a specified order.

    Args:
        item_id: The unique identifier of the item.

    Returns:
        The matching item.

    Raises:
        HTTPException: 404 if the item is not found.
    """

    order_parsed = parse_order_default(order=order, default=PreOrder())

    item = get_item_by_id(item_id, order=order_parsed)

    if item is not None:
        return item

    raise HTTPException(status_code=404, detail="Item not found")
