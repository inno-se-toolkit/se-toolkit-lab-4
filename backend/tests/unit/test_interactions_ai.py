"""Unit tests for interaction filtering logic - edge cases and boundary values."""

from app.models.interaction import InteractionLog
from app.routers.interactions import filter_by_max_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


# KEPT: tests max_item_id=0 edge case, not covered by existing tests
def test_filter_with_zero_max_item_id() -> None:
    """Test filtering with max_item_id=0 - should only include item_id=0."""
    interactions = [_make_log(1, 1, 0), _make_log(2, 2, 1)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == 0


# KEPT: tests negative max_item_id values, unique edge case
def test_filter_with_negative_max_item_id() -> None:
    """Test filtering with negative max_item_id."""
    interactions = [_make_log(1, 1, -5), _make_log(2, 2, -1), _make_log(3, 3, 0)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-2)
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == -5


# KEPT: tests when all interactions are above the boundary, returns empty
def test_filter_all_above_max_item_id() -> None:
    """Test when all interactions have item_id greater than max_item_id."""
    interactions = [_make_log(1, 1, 10), _make_log(2, 2, 20)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert result == []


# KEPT: tests all elements exactly at boundary, different from single-element boundary test
def test_filter_all_at_exact_max_item_id() -> None:
    """Test when all interactions have item_id exactly equal to max_item_id."""
    interactions = [_make_log(1, 1, 5), _make_log(2, 2, 5), _make_log(3, 3, 5)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert len(result) == 3
    assert all(i.item_id == 5 for i in result)


# DISCARDED: duplicates test_filter_includes_interaction_at_boundary in test_interactions.py
# def test_filter_with_single_element_at_max() -> None:
#     """Test with single interaction exactly at max_item_id boundary."""
#     interactions = [_make_log(1, 1, 100)]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=100)
#     assert len(result) == 1
#     assert result[0].id == 1


# KEPT: tests single element above boundary, not covered elsewhere
def test_filter_with_single_element_above_max() -> None:
    """Test with single interaction above max_item_id."""
    interactions = [_make_log(1, 1, 50)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=49)
    assert result == []


# KEPT: tests filtering with mixed learner_ids, verifies no unintended filtering
def test_filter_mixed_learner_ids() -> None:
    """Test filtering preserves interactions from multiple learners correctly."""
    interactions = [
        _make_log(1, 1, 5),
        _make_log(2, 2, 10),
        _make_log(3, 1, 15),
        _make_log(4, 3, 3),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=7)
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 4


# KEPT: tests with large integer values, verifies no overflow issues
def test_filter_with_large_item_id_values() -> None:
    """Test filtering with large integer item_id values."""
    interactions = [
        _make_log(1, 1, 999_999_999),
        _make_log(2, 2, 1_000_000_000),
        _make_log(3, 3, 1_000_000_001),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=1_000_000_000)
    assert len(result) == 2
    assert result[0].item_id == 999_999_999
    assert result[1].item_id == 1_000_000_000


# KEPT: tests that original order is preserved after filtering
def test_filter_preserves_original_order() -> None:
    """Test that filtering preserves the original order of interactions."""
    interactions = [
        _make_log(1, 1, 3),
        _make_log(2, 2, 1),
        _make_log(3, 3, 5),
        _make_log(4, 4, 2),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=3)
    assert len(result) == 3
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 4


# KEPT: tests consecutive values around boundary for precise filtering
def test_filter_with_consecutive_item_ids() -> None:
    """Test filtering with consecutive item_id values around boundary."""
    interactions = [
        _make_log(1, 1, 8),
        _make_log(2, 2, 9),
        _make_log(3, 3, 10),
        _make_log(4, 4, 11),
        _make_log(5, 5, 12),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=10)
    assert len(result) == 3
    assert [i.item_id for i in result] == [8, 9, 10]
