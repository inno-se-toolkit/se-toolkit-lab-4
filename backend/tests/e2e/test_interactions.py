from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    """Test that when item_id is None, all interactions are returned"""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    """Test filtering with empty list returns empty list"""
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    """Test that only interactions with matching item_id are returned"""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1


def test_filter_excludes_interaction_with_different_learner_id() -> None:
    """Test that filtering by item_id=1 returns interactions with item_id=1 
    even if they have different learner_id"""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=1),
        _make_log(id=2, learner_id=2, item_id=1),
        _make_log(id=3, learner_id=1, item_id=2),
    ]
    
    result = _filter_by_item_id(interactions, 1)
    
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2


def test_filter_with_maximum_item_id() -> None:
    """Test filtering with a very large item_id"""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=999999),
        _make_log(id=2, learner_id=2, item_id=999999)
    ]
    result = _filter_by_item_id(interactions, 999999)
    assert len(result) == 2


def test_filter_returns_empty_when_no_match() -> None:
    """Test filtering with non-existent item_id returns empty list"""
    interactions = [
        _make_log(id=1, learner_id=1, item_id=1),
        _make_log(id=2, learner_id=2, item_id=2)
    ]
    result = _filter_by_item_id(interactions, 999)
    assert result == []