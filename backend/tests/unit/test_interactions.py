import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

from backend.app.routers.interactions import _filter_by_item_id

class D:
    def __init__(self, id, item_id, learner_id):
        self.id = id
        self.item_id = item_id
        self.learner_id = learner_id

def test_filter_excludes_interaction_with_different_learner_id():
    interactions = [D(100, 1, 2), D(101, 2, 1)]
    res = _filter_by_item_id(interactions, 1)
    assert len(res) == 1
import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

from backend.app.routers.interactions import _filter_by_item_id

class D:
    def __init__(self, id, item_id, learner_id):
        self.id = id
        self.item_id = item_id
        self.learner_id = learner_id

def test_filter_excludes_interaction_with_different_learner_id():
    interactions = [D(100, 1, 2), D(101, 2, 1)]
    res = _filter_by_item_id(interactions, 1)
    assert len(res) == 1

def test_filter_returns_empty_for_nonexistent_item():
    interactions = [D(200, 10, 20), D(201, 11, 21)]
    res = _filter_by_item_id(interactions, 999)
    assert isinstance(res, list)
    assert len(res) == 0

def test_filter_preserves_input_order_for_matches():
    interactions = [D(300, 5, 50), D(301, 5, 51), D(302, 6, 52)]
    res = _filter_by_item_id(interactions, 5)
    ids = [i.id for i in res]
    assert ids == [300, 301]
