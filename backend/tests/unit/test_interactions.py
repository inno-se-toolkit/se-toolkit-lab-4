"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1
def test_filter_excludes_interaction_with_different_learner_id() -> None:
    interactions = [
        _make_log(id=1, learner_id=2, item_id=1),
        _make_log(id=2, learner_id=2, item_id=2)
    ]
    
    result = _filter_by_item_id(interactions, 1)
    
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == 1
    assert result[0].learner_id == 2
from datetime import datetime
from app.models.interaction import InteractionModel
from app.routers.interactions import _filter_by_item_id

def test_filter_interactions_empty_list():
    """AI Test 1: Проверка работы фильтра с пустым списком"""
    assert _filter_by_item_id([], 1) == []

def test_filter_interactions_item_id_zero():
    """AI Test 2: Проверка фильтрации для ID равного 0"""
    data = [InteractionModel(id=1, learner_id=1, item_id=0, kind="view", created_at=datetime.now())]
    assert len(_filter_by_item_id(data, 0)) == 1

def test_filter_interactions_no_results():
    """AI Test 3: Случай, когда в списке нет нужного item_id"""
    data = [InteractionModel(id=1, learner_id=1, item_id=2, kind="view", created_at=datetime.now())]
    assert _filter_by_item_id(data, 1) == []