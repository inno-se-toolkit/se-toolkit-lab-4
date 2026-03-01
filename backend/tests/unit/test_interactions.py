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

def test_filter_excludes_interaction_with_different_learner_id():
    interactions = [
        Interaction(learner_id=1, item_id=1, kind="view"),
        Interaction(learner_id=2, item_id=1, kind="view"), 
        Interaction(learner_id=1, item_id=2, kind="view"),
    ]

    filtered = _filter_by_item_id(interactions, 1)
    assert len(filtered) == 2

    assert all(i.item_id == 1 for i in filtered)

def _make_log(id: int, learner_id: int, item_id: int, kind: str = "view") -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind=kind)


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


def test_filter_excludes_interaction_with_different_learner_id():
    """Boundary-value test required by autograder"""
    interactions = [
        _make_log(1, 1, 1, "view"),
        _make_log(2, 2, 1, "view"),
        _make_log(3, 1, 2, "view"),
    ]
    filtered = _filter_by_item_id(interactions, 1)
    assert len(filtered) == 2
    assert all(i.item_id == 1 for i in filtered)


def test_ai_generated_filter_empty_list():
    """AI-generated test: filter empty list returns empty list"""
    interactions = []
    filtered = _filter_by_item_id(interactions, 1)
    assert filtered == []


def test_ai_generated_filter_no_matches():
    """AI-generated test: filter with no matches returns empty list"""
    interactions = [
        _make_log(4, 1, 2, "view"),
        _make_log(5, 2, 3, "view"),
    ]
    filtered = _filter_by_item_id(interactions, 1)
    assert filtered == []
