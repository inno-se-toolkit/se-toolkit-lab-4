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

def test_filter_excludes_interaction_with_different_learner_id() -> None:
    """Boundary-value test: filter by item_id should ignore learner_id differences.
    
    An interaction with item_id=1 and learner_id=2 should appear when filtering
    by item_id=1, confirming the filter operates on item_id only.
    """
    interactions = [
        _make_log(id=1, learner_id=2, item_id=1),  # Different learner_id, matching item_id
        _make_log(id=2, learner_id=1, item_id=2),  # Different item_id, should be excluded
    ]
    result = _filter_by_item_id(interactions, item_id=1)
    
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].item_id == 1
    assert result[0].learner_id == 2

def test_get_interactions_returns_200(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    response = client.get("/interactions/")
    assert isinstance(response.json(), list)
