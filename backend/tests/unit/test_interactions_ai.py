"""Unit tests for interaction filtering edge cases and boundary values."""

from app.models.interaction import InteractionLog
from app.routers.interactions import filter_by_max_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


# KEPT: tests filtering with negative max_item_id
def test_filter_with_negative_max_item_id() -> None:
    """Test filtering when max_item_id is negative."""
    interactions = [_make_log(1, 1, -5), _make_log(2, 2, -1), _make_log(3, 3, 0)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-2)
    assert len(result) == 1
    assert result[0].id == 1


# KEPT: tests boundary value zero
def test_filter_with_zero_max_item_id() -> None:
    """Test filtering when max_item_id is zero."""
    interactions = [
        _make_log(1, 1, -1),
        _make_log(2, 2, 0),
        _make_log(3, 3, 1),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2


# KEPT: tests very large max_item_id
def test_filter_with_very_large_max_item_id() -> None:
    """Test filtering with a very large max_item_id value."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 1000), _make_log(3, 3, 999999)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=10**9)
    assert result == interactions


# KEPT: tests mixed positive and negative
def test_filter_with_mixed_positive_and_negative_item_ids() -> None:
    """Test filtering with a mix of positive and negative item_ids."""
    interactions = [
        _make_log(1, 1, -10),
        _make_log(2, 2, 5),
        _make_log(3, 3, -3),
        _make_log(4, 4, 10),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 3


# KEPT: tests empty result case
def test_filter_returns_empty_when_all_above_threshold() -> None:
    """Test filtering returns empty list when all item_ids exceed max_item_id."""
    interactions = [_make_log(1, 1, 10), _make_log(2, 2, 20), _make_log(3, 3, 30)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert result == []


# DISCARDED: duplicates existing test_filter_includes_interaction_at_boundary
# def test_filter_with_multiple_at_exact_boundary() -> None:
#     """Test filtering includes all interactions at exact boundary value."""
#     interactions = [
#         _make_log(1, 1, 5),
#         _make_log(2, 2, 5),
#         _make_log(3, 3, 5),
#         _make_log(4, 4, 6),
#     ]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
#     assert len(result) == 3
#     assert all(log.item_id == 5 for log in result)


# KEPT: tests order preservation
def test_filter_preserves_original_order() -> None:
    """Test that filtering preserves the original order of interactions."""
    interactions = [
        _make_log(1, 1, 3),
        _make_log(2, 2, 1),
        _make_log(3, 3, 5),
        _make_log(4, 4, 2),
        _make_log(5, 5, 4),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=3)
    assert len(result) == 3
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 4


# DISCARDED: doesn't add value beyond existing tests
# def test_filter_with_same_item_id_different_learners() -> None:
#     """Test filtering with same item_id across different learners."""
#     interactions = [
#         _make_log(1, 1, 5),
#         _make_log(2, 2, 5),
#         _make_log(3, 3, 5),
#     ]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
#     assert len(result) == 3
#     assert all(log.item_id == 5 for log in result)
#     assert [log.learner_id for log in result] == [1, 2, 3]


# DISCARDED: tests invalid input (None), function expects int
# def test_filter_with_none_max_and_empty_list() -> None:
#     """Test filtering with None max_item_id on empty list."""
#     result = filter_by_max_item_id(interactions=[], max_item_id=None)
#     assert result == []


# KEPT: tests all negative item_ids included
def test_filter_with_negative_item_ids_all_included() -> None:
    """Test filtering when all item_ids are negative and within range."""
    interactions = [
        _make_log(1, 1, -100),
        _make_log(2, 2, -50),
        _make_log(3, 3, -1),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-1)
    assert result == interactions