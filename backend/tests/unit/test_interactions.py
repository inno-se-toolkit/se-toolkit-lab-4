"""Unit tests for interaction filtering logic."""

from datetime import datetime
from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    """Helper function to create an InteractionLog for testing."""
    return InteractionLog(
        id=id, 
        learner_id=learner_id, 
        item_id=item_id, 
        kind="attempt",
        created_at=datetime.now()
    )


def test_filter_returns_all_when_item_id_is_none() -> None:
    """Test that filter returns all interactions when no item_id filter is applied."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    """Test that filter returns empty list when input is empty."""
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    """Test that filter returns only interactions with matching item_id."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == 1


def test_filter_with_multiple_matching_items() -> None:
    """Test that filter returns ALL interactions with matching item_id when multiple exist."""
    now = datetime.now()
    test_interactions = [
        InteractionLog(id=1, learner_id=1, item_id=1, kind="attempt", created_at=now),
        InteractionLog(id=2, learner_id=2, item_id=1, kind="hint", created_at=now),
        InteractionLog(id=4, learner_id=1, item_id=1, kind="correct", created_at=now),
    ]
    
    filtered = _filter_by_item_id(test_interactions, item_id=1)
    
    assert len(filtered) == 3
    assert {i.id for i in filtered} == {1, 2, 4}
    assert all(i.item_id == 1 for i in filtered)


def test_filter_excludes_interaction_with_different_item_id() -> None:
    """Test that filter excludes interactions where item_id doesn't match."""
    now = datetime.now()
    
    test_interactions = [
        InteractionLog(id=1, learner_id=1, item_id=1, kind="attempt", created_at=now),
        InteractionLog(id=2, learner_id=1, item_id=2, kind="attempt", created_at=now),
        InteractionLog(id=3, learner_id=2, item_id=1, kind="attempt", created_at=now),
    ]
    
    filtered = _filter_by_item_id(test_interactions, item_id=1)
    
    assert len(filtered) == 2  
    assert filtered[0].id == 1
    assert filtered[1].id == 3
    assert all(i.item_id == 1 for i in filtered)


def test_filter_with_different_kind_values() -> None:
    """Test that filter works correctly with all possible kind values."""
    now = datetime.now()
    test_interactions = [
        InteractionLog(id=1, learner_id=1, item_id=1, kind="attempt", created_at=now),
        InteractionLog(id=2, learner_id=1, item_id=1, kind="hint", created_at=now),
        InteractionLog(id=3, learner_id=1, item_id=1, kind="correct", created_at=now),
        InteractionLog(id=4, learner_id=1, item_id=1, kind="wrong", created_at=now),
        InteractionLog(id=5, learner_id=2, item_id=2, kind="attempt", created_at=now),
    ]
    
    filtered = _filter_by_item_id(test_interactions, item_id=1)
    
    assert len(filtered) == 4
    assert all(i.item_id == 1 for i in filtered)
    kinds = [i.kind for i in filtered]
    assert "attempt" in kinds
    assert "hint" in kinds
    assert "correct" in kinds
    assert "wrong" in kinds
