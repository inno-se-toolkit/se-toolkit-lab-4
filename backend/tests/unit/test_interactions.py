"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id
from app.models.interaction import InteractionModel


from datetime import datetime
from app.models.interaction import InteractionModel 


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


def test_filter_excludes_interaction_with_different_learner_id() -> None:
    interaction = _make_log(id=1, learner_id=2, item_id=1)
    interactions = [interaction]

    result = _filter_by_item_id(interactions, 1)
    
    assert len(result) == 1


def test_filter_returns_empty_when_item_id_not_found() -> None:
    interactions = [_make_log(1, 1, 100), _make_log(2, 2, 200)]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


def test_filter_works_with_zero_item_id() -> None:
    interactions = [_make_log(1, 1, 0), _make_log(2, 2, 1)]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 1
    assert result[0].item_id == 0