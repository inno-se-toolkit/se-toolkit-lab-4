"""AI-generated unit tests covering edge cases and boundary values for interaction filtering logic."""

import pytest
from datetime import datetime, timezone
from app.models.interaction import InteractionLog
from app.routers.interactions import filter_by_max_item_id


def _make_log_with_custom_fields(
    id: int, 
    learner_id: int, 
    item_id: int, 
    kind: str = "attempt",
    created_at: datetime | None = None
) -> InteractionLog:
    """Helper to create InteractionLog with optional custom created_at."""
    if created_at is None:
        created_at = datetime.now(timezone.utc).replace(tzinfo=None)
    return InteractionLog(
        id=id, 
        learner_id=learner_id, 
        item_id=item_id, 
        kind=kind,
        created_at=created_at
    )


def test_filter_with_max_item_id_zero() -> None:
    """Test filtering with max_item_id = 0 (boundary value)."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 0),  # item_id = 0
        _make_log_with_custom_fields(2, 2, 1),
        _make_log_with_custom_fields(3, 3, 5),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == 0


def test_filter_with_negative_item_ids() -> None:
    """Test filtering when item_ids are negative (edge case)."""
    interactions = [
        _make_log_with_custom_fields(1, 1, -5),
        _make_log_with_custom_fields(2, 2, -1),
        _make_log_with_custom_fields(3, 3, 0),
        _make_log_with_custom_fields(4, 4, 10),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-2)
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == -5


def test_filter_with_very_large_max_item_id() -> None:
    """Test filtering with extremely large max_item_id (boundary value)."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 999999),
        _make_log_with_custom_fields(2, 2, 1000000),
        _make_log_with_custom_fields(3, 3, 1000001),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=1000000)
    assert len(result) == 2
    assert all(i.item_id <= 1000000 for i in result)


def test_filter_with_duplicate_item_ids() -> None:
    """Test filtering when multiple interactions have the same item_id."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 5),
        _make_log_with_custom_fields(2, 2, 5),  # Same item_id
        _make_log_with_custom_fields(3, 3, 5),  # Same item_id
        _make_log_with_custom_fields(4, 4, 10),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert len(result) == 3
    assert all(i.item_id == 5 for i in result)


def test_filter_preserves_original_order() -> None:
    """Test that filtering preserves the original order of interactions."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 10),
        _make_log_with_custom_fields(2, 2, 5),
        _make_log_with_custom_fields(3, 3, 8),
        _make_log_with_custom_fields(4, 4, 3),
        _make_log_with_custom_fields(5, 5, 12),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=8)
    expected_ids = [2, 3, 4]  # Items with id 2 (item_id=5), 3 (item_id=8), 4 (item_id=3)
    assert [i.id for i in result] == expected_ids


def test_filter_with_all_items_exceeding_max() -> None:
    """Test when all item_ids are greater than max_item_id."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 10),
        _make_log_with_custom_fields(2, 2, 15),
        _make_log_with_custom_fields(3, 3, 20),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert result == []


def test_filter_with_all_items_equal_to_max() -> None:
    """Test when all item_ids are exactly equal to max_item_id."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 7),
        _make_log_with_custom_fields(2, 2, 7),
        _make_log_with_custom_fields(3, 3, 7),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=7)
    assert len(result) == 3
    assert all(i.item_id == 7 for i in result)


def test_filter_with_mixed_item_types_and_kinds() -> None:
    """Test filtering with different interaction kinds."""
    interactions = [
        _make_log_with_custom_fields(1, 1, 3, kind="attempt"),
        _make_log_with_custom_fields(2, 2, 5, kind="success"),
        _make_log_with_custom_fields(3, 3, 7, kind="hint"),
        _make_log_with_custom_fields(4, 4, 9, kind="attempt"),
        _make_log_with_custom_fields(5, 5, 11, kind="skip"),
    ]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=7)
    assert len(result) == 3
    assert [i.id for i in result] == [1, 2, 3]
    assert [i.kind for i in result] == ["attempt", "success", "hint"]


def test_filter_with_max_int_boundary() -> None:
    """Test filtering with max_item_id set to maximum integer value."""
    import sys
    max_int = sys.maxsize
    
    interactions = [
        _make_log_with_custom_fields(1, 1, max_int - 1),
        _make_log_with_custom_fields(2, 2, max_int),
        _make_log_with_custom_fields(3, 3, max_int + 1),  # This would overflow in some languages
    ]
    # In Python, integers are unbounded, but we can still test the logic
    result = filter_by_max_item_id(interactions=interactions, max_item_id=max_int)
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2


def test_filter_preserves_all_fields() -> None:
    """Test that filtering preserves all fields of the InteractionLog objects."""
    specific_time = datetime(2024, 1, 15, 10, 30, 0)
    interactions = [
        _make_log_with_custom_fields(
            id=1, 
            learner_id=42, 
            item_id=15, 
            kind="test_kind",
            created_at=specific_time
        ),
        _make_log_with_custom_fields(
            id=2, 
            learner_id=99, 
            item_id=25, 
            kind="another_kind",
            created_at=specific_time
        ),
    ]
    
    result = filter_by_max_item_id(interactions=interactions, max_item_id=20)
    
    assert len(result) == 1
    filtered_log = result[0]
    assert filtered_log.id == 1
    assert filtered_log.learner_id == 42
    assert filtered_log.item_id == 15
    assert filtered_log.kind == "test_kind"
    assert filtered_log.created_at == specific_time