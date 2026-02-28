"""Unit tests for edge cases and boundary values."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_multiple_matches_for_same_item_id() -> None:
    """Edge case: multiple interactions with the same item_id should all be returned."""
    interactions = [
        _make_log(1, 1, 5),
        _make_log(2, 2, 5),
        _make_log(3, 3, 5),
        _make_log(4, 1, 6),
    ]
    result = _filter_by_item_id(interactions, 5)
    assert len(result) == 3
    assert all(i.item_id == 5 for i in result)


def test_filter_with_zero_as_item_id() -> None:
    """Boundary value: zero is a valid item_id and should be filtered correctly."""
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 1),
        _make_log(3, 3, 0),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 2
    assert all(i.item_id == 0 for i in result)


def test_filter_with_negative_item_id() -> None:
    """Boundary value: negative item_id should be handled correctly."""
    interactions = [
        _make_log(1, 1, -1),
        _make_log(2, 2, 1),
        _make_log(3, 3, -1),
    ]
    result = _filter_by_item_id(interactions, -1)
    assert len(result) == 2
    assert all(i.item_id == -1 for i in result)


def test_filter_returns_empty_when_no_matches() -> None:
    """Edge case: filtering for item_id that doesn't exist should return empty list."""
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 2),
        _make_log(3, 3, 3),
    ]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


def test_filter_preserves_original_order() -> None:
    """Edge case: filtered results should maintain the original list order."""
    interactions = [
        _make_log(1, 1, 10),
        _make_log(2, 2, 20),
        _make_log(3, 3, 10),
        _make_log(4, 4, 30),
        _make_log(5, 5, 10),
    ]
    result = _filter_by_item_id(interactions, 10)
    assert len(result) == 3
    assert [i.id for i in result] == [1, 3, 5]
