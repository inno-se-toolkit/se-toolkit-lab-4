"""Unit tests for edge cases and boundary values."""

from datetime import datetime

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


# =============================================================================
# Test 1: Empty list (boundary value)
# =============================================================================
def test_filter_by_item_id_with_empty_list():
    """
    Граничный случай: пустой список взаимодействий.
    Ожидается: возвращается пустой список.
    """
    result = _filter_by_item_id([], item_id=1)
    
    assert result == []
    assert len(result) == 0


# =============================================================================
# Test 2: No matches (boundary value)
# =============================================================================
def test_filter_by_item_id_with_no_matches():
    """
    Граничный случай: ни одно взаимодействие не совпадает с item_id.
    Ожидается: возвращается пустой список.
    """
    interactions = [
        InteractionLog(id=1, learner_id=1, item_id=5, kind="view", created_at=datetime.now()),
        InteractionLog(id=2, learner_id=2, item_id=10, kind="click", created_at=datetime.now()),
        InteractionLog(id=3, learner_id=3, item_id=15, kind="attempt", created_at=datetime.now()),
    ]
    
    result = _filter_by_item_id(interactions, item_id=999)
    
    assert result == []
    assert len(result) == 0


# =============================================================================
# Test 3: Zero item_id (boundary value for integer)
# =============================================================================
def test_filter_by_item_id_with_zero_item_id():
    """
    Граничный случай: item_id = 0 (граничное значение для целого числа).
    Ожидается: возвращаются взаимодействия с item_id == 0.
    """
    interactions = [
        InteractionLog(id=1, learner_id=1, item_id=0, kind="view", created_at=datetime.now()),
        InteractionLog(id=2, learner_id=2, item_id=1, kind="click", created_at=datetime.now()),
        InteractionLog(id=3, learner_id=3, item_id=0, kind="attempt", created_at=datetime.now()),
    ]
    
    result = _filter_by_item_id(interactions, item_id=0)
    
    assert len(result) == 2
    assert all(item.item_id == 0 for item in result)