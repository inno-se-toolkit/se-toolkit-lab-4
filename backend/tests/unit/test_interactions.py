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
    interactions = [_make_log(1, learner_id=2, item_id=1)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_returns_multiple_interactions_with_same_item_id() -> None:
    """When multiple logs have the same item_id, all should be returned."""
    interactions = [
        _make_log(1, learner_id=1, item_id=42),
        _make_log(2, learner_id=2, item_id=99),
        _make_log(3, learner_id=3, item_id=42),
        _make_log(4, learner_id=4, item_id=42),
    ]
    result = _filter_by_item_id(interactions, 42)
    assert len(result) == 3
    assert {log.id for log in result} == {1, 3, 4}


def test_filter_excludes_interactions_with_item_id_none() -> None:
    """Interactions where item_id is None should be excluded when filtering for a specific ID."""
    interactions = [
        _make_log(1, learner_id=1, item_id=1),
        _make_log(2, learner_id=2, item_id=None),   # item_id can be nullable
        _make_log(3, learner_id=3, item_id=1),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 2
    assert {log.id for log in result} == {1, 3}


def test_filter_returns_empty_list_when_item_id_not_found() -> None:
    """Filtering with an item_id that does not appear in any interaction returns an empty list."""
    interactions = [
        _make_log(1, learner_id=1, item_id=10),
        _make_log(2, learner_id=2, item_id=20),
    ]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


def test_filter_does_not_mutate_original_list() -> None:
    """The filtering function should return a new list and leave the original unchanged."""
    original = [
        _make_log(1, learner_id=1, item_id=1),
        _make_log(2, learner_id=2, item_id=2),
    ]
    original_copy = original.copy()  # keep a reference to compare later
    result = _filter_by_item_id(original, 1)
    # Original list should still have both items
    assert original == original_copy
    assert len(original) == 2
    # Result should be a new list, not the same object
    assert result is not original


def test_filter_handles_zero_as_item_id() -> None:
    """If item_id can be zero (e.g., database ID starts at 0), filtering should work correctly."""
    interactions = [
        _make_log(1, learner_id=1, item_id=0),
        _make_log(2, learner_id=2, item_id=1),
        _make_log(3, learner_id=3, item_id=0),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 2
    assert {log.id for log in result} == {1, 3}