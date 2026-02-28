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
    
def test_filter_by_item_id_uses_correct_field() -> None:
    """Test that filter uses item_id field, not learner_id."""
    # Создаем записи, где learner_id и item_id РАЗНЫЕ
    interactions = [
        _make_log(id=1, learner_id=10, item_id=20),
        _make_log(id=2, learner_id=20, item_id=10),
        _make_log(id=3, learner_id=30, item_id=30)
    ]
    
    # Фильтруем по item_id=20
    filtered = _filter_by_item_id(interactions, 20)
    
    # Должна вернуться только запись с item_id=20 (первая)
    assert len(filtered) == 1
    assert filtered[0].id == 1
    assert filtered[0].item_id == 20
    assert filtered[0].learner_id == 10  # learner_id может быть другим
    
    # Фильтруем по item_id=30
    filtered2 = _filter_by_item_id(interactions, 30)
    
    # Должна вернуться только запись с item_id=30 (третья)
    assert len(filtered2) == 1
    assert filtered2[0].id == 3
    assert filtered2[0].item_id == 30
    assert filtered2[0].learner_id == 30