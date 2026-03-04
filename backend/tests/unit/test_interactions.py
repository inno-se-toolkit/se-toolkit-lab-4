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

def test_filter_returns_empty_for_nonexistent_item_id() -> None:
    """Test that filtering by non-existent learner_id returns empty list."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 999)  # фильтр по learner_id
    assert result == []


def test_filter_handles_multiple_matching_interactions() -> None:
    """Test that filtering returns all interactions with matching learner_id."""
    interactions = [
        _make_log(1, 1, 1),    # learner_id=1
        _make_log(2, 2, 1),    # learner_id=2
        _make_log(3, 1, 2),    # learner_id=1
        _make_log(4, 3, 1)     # learner_id=3
    ]
    result = _filter_by_item_id(interactions, 1)  # фильтр по learner_id=1
    assert len(result) == 2  # должны найтись logs с learner_id=1: id=1 и id=3
    assert all(log.learner_id == 1 for log in result)
    assert {log.id for log in result} == {1, 3}


def test_filter_handles_large_item_id() -> None:
    """Test that filtering works with large learner_id values."""
    interactions = [_make_log(1, 1000000, 1)]
    result = _filter_by_item_id(interactions, 1000000)  # фильтр по learner_id
    assert len(result) == 1
    assert result[0].learner_id == 1000000


def test_filter_preserves_interaction_order() -> None:
    """Test that filtering preserves the original order of interactions."""
    interactions = [
        _make_log(1, 1, 2),    # learner_id=1, item_id=2
        _make_log(2, 2, 1),    # learner_id=2, item_id=1
        _make_log(3, 1, 1),    # learner_id=1, item_id=1
        _make_log(4, 4, 2),    # learner_id=4, item_id=2
        _make_log(5, 1, 1)     # learner_id=1, item_id=1
    ]
    result = _filter_by_item_id(interactions, 1)  # фильтр по learner_id=1
    assert len(result) == 3  # learner_id=1: id=1, id=3, id=5
    assert result[0].id == 1
    assert result[1].id == 3
    assert result[2].id == 5
    assert all(log.learner_id == 1 for log in result)
