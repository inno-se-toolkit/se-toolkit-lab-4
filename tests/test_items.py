from fastapi.testclient import TestClient
from pydantic import TypeAdapter

from app.models.item import Course, Task, Step
from app.services.item_service import FoundItem

# ===


def get_course_at_index(client: TestClient, course_id: str, lab_id: str):
    response = client.get(f"/items/course/{course_id}")

    assert response.status_code == 200
    course = Course.model_validate(response.json())
    assert course.id == course_id
    assert course.labs is not None
    assert course.labs[0].id == lab_id


def test_get_course_1(client: TestClient):
    get_course_at_index(
        client=client, course_id="software_engineering_toolkit", lab_id="lab-02"
    )


# ===


FoundItemAdapter: TypeAdapter[FoundItem] = TypeAdapter(type=FoundItem)


def get_task_by_id(client: TestClient, task_id: str, step_id: str, order: str):
    response = client.get(f"/items/item/{task_id}?order={order}")

    assert response.status_code == 200

    foundItem = FoundItemAdapter.validate_python(response.json())
    task = Task.model_validate(foundItem.item)

    assert task.id == task_id
    assert task.steps is not None
    assert task.steps[0].id == step_id

    assert foundItem.visited_nodes == 8


def test_get_item_1(client: TestClient):
    get_task_by_id(
        client=client,
        task_id="lab-02-run-local",
        step_id="lab-02-run-local-venv",
        order="pre",
    )


# ===


def get_step_by_path(
    client: TestClient, course_id: str, lab_id: str, task_id: str, step_id: str
):
    response = client.get(
        f"/items/course/{course_id}/lab/{lab_id}/task/{task_id}/step/{step_id}"
    )

    assert response.status_code == 200
    step = Step.model_validate(response.json())
    assert step.id == step_id


def test_get_step_by_path_1(client: TestClient):
    get_step_by_path(
        client=client,
        course_id="software_engineering_toolkit",
        lab_id="lab-02",
        task_id="lab-02-document-bug",
        step_id="lab-02-document-bug-reproduce",
    )
