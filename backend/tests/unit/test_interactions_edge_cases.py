"""Edge case and boundary value tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_by_item_id_zero() -> None:
    """Test filtering by item_id=0 (boundary: zero is falsy but valid)."""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=0),
        _make_log(id=2, learner_id=2, item_id=1),
        _make_log(id=3, learner_id=3, item_id=0),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 2
    assert all(i.item_id == 0 for i in result)
    assert {i.id for i in result} == {1, 3}


def test_filter_by_negative_item_id() -> None:
    """Test filtering by negative item_id (boundary: negative values)."""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=-1),
        _make_log(id=2, learner_id=2, item_id=1),
        _make_log(id=3, learner_id=3, item_id=-5),
    ]
    result = _filter_by_item_id(interactions, -1)
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == -1


def test_filter_no_matches() -> None:
    """Test filtering when no interactions match the item_id."""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=1),
        _make_log(id=2, learner_id=2, item_id=2),
        _make_log(id=3, learner_id=3, item_id=3),
    ]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


def test_filter_all_match() -> None:
    """Test filtering when all interactions have the same item_id."""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=5),
        _make_log(id=2, learner_id=2, item_id=5),
        _make_log(id=3, learner_id=3, item_id=5),
    ]
    result = _filter_by_item_id(interactions, 5)
    assert result == interactions


def test_filter_multiple_matches() -> None:
    """Test filtering returns all matching interactions (not just first)."""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=10),
        _make_log(id=2, learner_id=2, item_id=20),
        _make_log(id=3, learner_id=3, item_id=10),
        _make_log(id=4, learner_id=4, item_id=10),
        _make_log(id=5, learner_id=5, item_id=30),
    ]
    result = _filter_by_item_id(interactions, 10)
    assert len(result) == 3
    assert {i.id for i in result} == {1, 3, 4}
    assert all(i.item_id == 10 for i in result)
