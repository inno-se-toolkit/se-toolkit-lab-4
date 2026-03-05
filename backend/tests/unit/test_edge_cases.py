"""Unit tests for edge cases and boundary values."""

from app.models.interaction import InteractionLog
from app.models.item import ItemCreate
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    """Helper to create InteractionLog instances for testing."""
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


class TestFilterByItemIdBoundaryValues:
    """Boundary value tests for the _filter_by_item_id function."""

    def test_filter_with_zero_item_id(self) -> None:
        """Test filtering with item_id=0 (boundary value)."""
        interactions = [
            _make_log(1, 1, 0),
            _make_log(2, 2, 1),
            _make_log(3, 3, 0),
        ]
        result = _filter_by_item_id(interactions, 0)
        assert len(result) == 2
        assert all(i.item_id == 0 for i in result)

    def test_filter_with_negative_item_id(self) -> None:
        """Test filtering with negative item_id (boundary value)."""
        interactions = [
            _make_log(1, 1, -1),
            _make_log(2, 2, 1),
        ]
        result = _filter_by_item_id(interactions, -1)
        assert len(result) == 1
        assert result[0].item_id == -1

    def test_filter_no_matches_returns_empty(self) -> None:
        """Test that no matching item_id returns empty list."""
        interactions = [
            _make_log(1, 1, 1),
            _make_log(2, 2, 2),
            _make_log(3, 3, 3),
        ]
        result = _filter_by_item_id(interactions, 999)
        assert result == []


class TestItemCreateEdgeCases:
    """Edge case tests for ItemCreate model."""

    def test_item_create_with_very_long_title(self) -> None:
        """Test creating an item with a very long title (boundary value)."""
        long_title = "a" * 10000
        item = ItemCreate(title=long_title, description="Short description")
        assert len(item.title) == 10000
        assert item.title == long_title

    def test_item_create_with_none_parent_id(self) -> None:
        """Test creating an item with parent_id=None (root-level item)."""
        item = ItemCreate(title="Root Item", parent_id=None)
        assert item.parent_id is None
        assert item.type == "step"  # default value
