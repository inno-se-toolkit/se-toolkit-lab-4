from datetime import datetime
from app.models.interaction import InteractionModel
from app.routers.interactions import _filter_by_item_id

def _make_log(id: int, learner_id: int, item_id: int) -> InteractionModel:
    """Вспомогательная функция для создания объектов модели"""
    return InteractionModel(
        id=id,
        learner_id=learner_id,
        item_id=item_id,
        kind="attempt",
        created_at=datetime.now()
    )

def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, item_id=None)
    assert len(result) == 2

def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, item_id=1)
    assert len(result) == 1
    assert result[0].item_id == 1

def test_filter_excludes_interaction_with_different_learner_id():
    """Тест для Шага 1.3.2: проверяем граничный случай"""
    # Создаем лог, где learner_id (2) не равен item_id (1)
    interactions = [_make_log(id=1, learner_id=2, item_id=1)]
    result = _filter_by_item_id(interactions, item_id=1)
    
    # Ожидаем 1, но из-за бага в роутере вернется 0
    assert len(result) == 1

def test_filter_empty_interactions_list():
    result = _filter_by_item_id([], item_id=1)
    assert len(result) == 0

def test_filter_no_matching_item_id():
    interactions = [_make_log(1, 1, 2), _make_log(2, 2, 3)]
    result = _filter_by_item_id(interactions, item_id=1)
    assert len(result) == 0

def test_filter_negative_item_id():
    interactions = [_make_log(1, 1, -1)]
    result = _filter_by_item_id(interactions, item_id=-1)
    assert len(result) == 1

def test_filter_multiple_matches():
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 1), _make_log(3, 3, 2)]
    result = _filter_by_item_id(interactions, item_id=1)
    assert len(result) == 2
