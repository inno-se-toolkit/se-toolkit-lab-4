
import pytest
from app.routers.interactions import filter_by_max_item_id
from app.models.interaction import InteractionLog

from datetime import datetime

def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="view", created_at=datetime.now())

# KEPT: Тестирует случай, когда список взаимодействий пуст (edge case)
def test_filter_empty_list() -> None:
    assert filter_by_max_item_id([], 10) == []

# KEPT: Проверяет, что фильтр работает корректно с очень большими ID
def test_filter_large_ids() -> None:
    logs = [_make_log(1, 1, 999999)]
    assert len(filter_by_max_item_id(logs, 1000000)) == 1