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
    """Test that filter by item_id works even when learner_id is different."""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=1),
        _make_log(id=2, learner_id=2, item_id=1)
    ]
    
    result = _filter_by_item_id(interactions, 1)
    
    assert len(result) == 2
    assert {i.id for i in result} == {1, 2}

def test_filter_returns_multiple_interactions_with_same_item_id() -> None:
    """Test that filter returns all interactions with the same item_id."""
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),  # другой learner, тот же item_id
        _make_log(3, 3, 2)   # другой item_id
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 2
    assert {i.id for i in result} == {1, 2}

def test_filter_with_item_id_zero() -> None:
    """Test filtering with item_id = 0 (граничное значение)."""
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 1)
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_with_negative_item_id() -> None:
    """Test filtering with negative item_id."""
    interactions = [
        _make_log(1, 1, -1),
        _make_log(2, 2, 1)
    ]
    result = _filter_by_item_id(interactions, -1)
    assert len(result) == 1
    assert result[0].id == 1
