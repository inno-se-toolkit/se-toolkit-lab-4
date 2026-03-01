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

def test_filter_excludes_interaction_with_different_item_id() -> None:
    """Test that filtering by item_id excludes interactions with non-matching item_id."""
    
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 2),  # другой item_id - должен быть исключен
    ]
    
    result = _filter_by_item_id(interactions, 1)
    
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_with_item_id_zero() -> None:
    """Test filtering with item_id=0 (boundary value)."""
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 1),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 1
    assert result[0].item_id == 0


def test_filter_with_negative_item_id() -> None:
    """Test filtering with negative item_id (edge case)."""
    interactions = [
        _make_log(1, 1, -1),
        _make_log(2, 2, 1),
    ]
    result = _filter_by_item_id(interactions, -1)
    assert len(result) == 1
    assert result[0].item_id == -1


def test_filter_returns_multiple_matches() -> None:
    """Test that filter returns all interactions with matching item_id."""
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),
        _make_log(3, 3, 2),
        _make_log(4, 4, 1),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 3
    assert all(i.item_id == 1 for i in result)





def test_filter_with_large_item_id() -> None:
    """Test filtering with very large item_id (boundary value)."""
    large_id = 999999
    interactions = [
        _make_log(1, 1, large_id),
        _make_log(2, 2, 1),
    ]
    result = _filter_by_item_id(interactions, large_id)
    assert len(result) == 1
    assert result[0].item_id == large_id