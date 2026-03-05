from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id

def test_ai_filter_with_non_existent_item_id():
    # Edge case: item_id that doesn't exist in the list
    interactions = [InteractionLog(id=1, learner_id=1, item_id=1, kind="view")]
    result = _filter_by_item_id(interactions, item_id=999)
    assert len(result) == 0

def test_ai_filter_with_multiple_matches():
    # Boundary value: multiple interactions for the same item
    interactions = [
        InteractionLog(id=1, learner_id=1, item_id=5, kind="view"),
        InteractionLog(id=2, learner_id=2, item_id=5, kind="attempt")
    ]
    result = _filter_by_item_id(interactions, item_id=5)
    assert len(result) == 2