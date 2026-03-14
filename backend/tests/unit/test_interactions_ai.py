"""Unit tests for interaction filtering logic - edge cases and boundary values."""

from app.models.interaction import InteractionLog
from app.routers.interactions import filter_by_max_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


# KEPT: covers negative max_item_id filtering all positive item_ids
def test_filter_negative_max_item_id_filters_all_positive() -> None:
    """When max_item_id is negative, all positive item_ids should be filtered out."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 5), _make_log(3, 3, 10)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-1)
    assert result == []


# KEPT: covers zero boundary with mixed positive, zero, and negative item_ids
def test_filter_zero_max_item_id_boundary() -> None:
    """When max_item_id is 0, only item_id <= 0 should be included."""
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 1),
        _make_log(3, 3, -1),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 3


# KEPT: covers item_id=0 boundary case
def test_filter_zero_item_id_included() -> None:
    """Interaction with item_id=0 should be included when max_item_id >= 0."""
    interactions = [_make_log(1, 1, 0)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 1
    assert result[0].item_id == 0


# KEPT: covers negative item_id values
def test_filter_negative_item_id_included() -> None:
    """Interaction with negative item_id should be included when max_item_id allows."""
    interactions = [_make_log(1, 1, -5)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-3)
    assert len(result) == 1
    assert result[0].item_id == -5


# KEPT: covers empty result when all interactions are above max
def test_filter_all_above_max_returns_empty() -> None:
    """When all interactions have item_id > max_item_id, result should be empty."""
    interactions = [_make_log(1, 1, 10), _make_log(2, 2, 20), _make_log(3, 3, 30)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert result == []


# KEPT: covers duplicate item_ids at boundary
def test_filter_duplicate_item_ids_at_boundary() -> None:
    """Multiple interactions with same item_id at boundary should all be included."""
    interactions = [
        _make_log(1, 1, 5),
        _make_log(2, 2, 5),
        _make_log(3, 3, 5),
        _make_log(4, 4, 6),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert len(result) == 3
    assert all(i.item_id == 5 for i in result)


# KEPT: covers order preservation in filtered results
def test_filter_unsorted_input_preserves_order() -> None:
    """Filtering should preserve the original order of interactions."""
    interactions = [
        _make_log(1, 1, 10),
        _make_log(2, 2, 1),
        _make_log(3, 3, 5),
        _make_log(4, 4, 3),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert len(result) == 3
    assert result[0].id == 2
    assert result[1].id == 3
    assert result[2].id == 4


# KEPT: covers large integer boundary values (2^31 - 1)
def test_filter_large_integer_values() -> None:
    """Filtering should work correctly with large integer values."""
    large_value = 2**31 - 1  # Max 32-bit signed integer
    interactions = [
        _make_log(1, 1, large_value),
        _make_log(2, 2, large_value - 1),
        _make_log(3, 3, large_value + 1),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=large_value)
    assert len(result) == 2
    assert result[0].item_id == large_value
    assert result[1].item_id == large_value - 1


# KEPT: covers mixed negative, zero, and positive item_ids
def test_filter_mixed_negative_and_positive_item_ids() -> None:
    """Filtering should correctly handle mix of negative and positive item_ids."""
    interactions = [
        _make_log(1, 1, -100),
        _make_log(2, 2, -1),
        _make_log(3, 3, 0),
        _make_log(4, 4, 1),
        _make_log(5, 5, 100),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 3
    assert result[0].item_id == -100
    assert result[1].item_id == -1
    assert result[2].item_id == 0


# DISCARDED: similar to test_filter_all_above_max_returns_empty, just with different values
# def test_filter_single_interaction_far_above_max() -> None:
#     """Single interaction with item_id far above max_item_id should be filtered out."""
#     interactions = [_make_log(1, 1, 1000000)]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=1)
#     assert result == []
