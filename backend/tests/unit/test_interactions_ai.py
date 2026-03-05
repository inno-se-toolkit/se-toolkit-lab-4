"""AI-generated unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


# KEPT: covers the case where all interactions have item_id greater than the filter
def test_filter_returns_empty_when_all_item_ids_are_greater() -> None:
    interactions = [_make_log(1, 1, 5), _make_log(2, 2, 10), _make_log(3, 3, 15)]
    result = _filter_by_item_id(interactions, 3)
    assert len(result) == 0


# KEPT: covers the case where all interactions have the same item_id matching the filter
def test_filter_returns_all_when_all_item_ids_match() -> None:
    interactions = [_make_log(1, 1, 5), _make_log(2, 2, 5), _make_log(3, 3, 5)]
    result = _filter_by_item_id(interactions, 5)
    assert len(result) == 3
    assert all(i.item_id == 5 for i in result)


# KEPT: covers the boundary case at item_id = 0
def test_filter_with_item_id_zero() -> None:
    interactions = [_make_log(1, 1, 0), _make_log(2, 2, 1)]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 1
    assert result[0].id == 1


# DISCARDED: duplicates test_filter_returns_empty_for_empty_input
# def test_filter_empty_interactions_list() -> None:
#     result = _filter_by_item_id([], 5)
#     assert result == []


# KEPT: covers the case with mixed matching and non-matching item_ids
def test_filter_with_mixed_item_ids() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 2),
        _make_log(3, 3, 1),
        _make_log(4, 4, 3),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 2
    assert all(i.item_id == 1 for i in result)


# DISCARDED: tests behavior outside the scope
# def test_filter_by_learner_id_not_item_id() -> None:
#     interactions = [_make_log(1, 5, 1)]
#     result = _filter_by_item_id(interactions, 5)
#     assert len(result) == 0


# KEPT: covers large item_id values
def test_filter_with_large_item_id() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 999999)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
