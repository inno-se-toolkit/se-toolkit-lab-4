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


def test_filter_excludes_interaction_with_different_learner_id():
    interactions = [_make_log(id=1, learner_id=2, item_id=1)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1


# 1. Тест на несколько совпадений (multiple matches)
def test_filter_returns_multiple_matches():
    interactions = [_make_log(1, 1, 5), _make_log(2, 2, 5), _make_log(3, 3, 1)]
    result = _filter_by_item_id(interactions, 5)
    assert len(result) == 2


# 2. Тест на несовпадение ID (no match case)
def test_filter_returns_nothing_when_no_item_matches():
    interactions = [_make_log(1, 1, 1)]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


# 3. Тест на использование очень больших чисел (boundary value)
def test_filter_with_large_integer_ids():
    large_id = 10**18
    interactions = [_make_log(1, 1, large_id)]
    result = _filter_by_item_id(interactions, large_id)
    assert len(result) == 1


# 4. Тест на поведение при None значении в списке данных
def test_filter_handles_logs_with_none_item_id():
    interactions = [InteractionLog(id=1, learner_id=1, item_id=None, kind="test")]
    result = _filter_by_item_id(interactions, 1)
    assert result == []


# 5. Тест на передачу item_id как отрицательного числа
def test_filter_with_negative_item_id():
    interactions = [_make_log(1, 1, -5)]
    result = _filter_by_item_id(interactions, -5)
    assert len(result) == 1
