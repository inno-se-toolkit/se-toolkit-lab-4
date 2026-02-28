"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id

def test_filter_excludes_interaction_with_different_learner_id():
    class MockInteraction:
        def __init__(self, item_id, learner_id):
            self.item_id = item_id
            self.learner_id = learner_id

    test_interactions = [
        MockInteraction(item_id=1, learner_id=1),
        MockInteraction(item_id=1, learner_id=2),
        MockInteraction(item_id=2, learner_id=1),
        MockInteraction(item_id=2, learner_id=2),
    ]

    result = _filter_by_item_id(test_interactions, item_id=1)

    assert len(result) == 2
    for interaction in result:
        assert interaction.item_id == 1
    found_learner_ids = [i.learner_id for i in result]
    assert 1 in found_learner_ids
    assert 2 in found_learner_ids

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

def test_filter_with_large_item_id() -> None:
    interactions = [
        _make_log(1, 1, 999999),
        _make_log(2, 2, 1),
        _make_log(3, 3, 999999),
    ]
    result = _filter_by_item_id(interactions, 999999)
    assert len(result) == 2
    assert all(i.item_id == 999999 for i in result)


def test_filter_preserves_order() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),
        _make_log(3, 3, 1),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 3
    assert [i.id for i in result] == [1, 2, 3]