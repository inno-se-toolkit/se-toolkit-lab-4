"""Unit tests for interaction filtering logic - edge cases and boundary values."""

from datetime import datetime, timezone

from app.models.interaction import InteractionLog, InteractionLogCreate, InteractionModel
from app.routers.interactions import filter_by_max_item_id


def _make_log(
    id: int | None = None,
    learner_id: int = 1,
    item_id: int = 1,
    kind: str = "attempt",
    created_at: datetime | None = None,
) -> InteractionLog:
    """Helper to create an InteractionLog instance for testing."""
    return InteractionLog(
        id=id,
        learner_id=learner_id,
        item_id=item_id,
        kind=kind,
        created_at=created_at or datetime.now(timezone.utc).replace(tzinfo=None),
    )


class TestFilterByMaxItemIdEdgeCases:
    """Edge case tests for filter_by_max_item_id function."""

    # KEPT: covers the case when all item_ids exceed max_item_id, not tested elsewhere
    def test_filter_returns_empty_when_all_item_ids_exceed_max(self) -> None:
        """Test that empty list is returned when all interactions have item_id > max_item_id."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=5),
            _make_log(id=2, learner_id=1, item_id=10),
            _make_log(id=3, learner_id=1, item_id=15),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=3)
        assert result == []

    # KEPT: covers boundary case with max_item_id=0, not tested elsewhere
    def test_filter_with_max_item_id_zero(self) -> None:
        """Test filtering with max_item_id=0 includes only item_id=0."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=0),
            _make_log(id=2, learner_id=1, item_id=1),
            _make_log(id=3, learner_id=1, item_id=-1),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=0)
        assert len(result) == 2
        assert all(i.item_id <= 0 for i in result)

    # KEPT: covers negative max_item_id boundary case, not tested elsewhere
    def test_filter_with_negative_max_item_id(self) -> None:
        """Test filtering with negative max_item_id value."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=-5),
            _make_log(id=2, learner_id=1, item_id=-3),
            _make_log(id=3, learner_id=1, item_id=-1),
            _make_log(id=4, learner_id=1, item_id=0),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=-2)
        assert len(result) == 2
        assert all(i.item_id <= -2 for i in result)

    # KEPT: covers negative item_id values edge case
    def test_filter_with_negative_item_ids(self) -> None:
        """Test filtering handles negative item_id values correctly."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=-10),
            _make_log(id=2, learner_id=1, item_id=-5),
            _make_log(id=3, learner_id=1, item_id=5),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=-3)
        assert len(result) == 2  # -10 and -5 are both <= -3
        assert all(i.item_id <= -3 for i in result)

    # KEPT: covers duplicate item_ids edge case, not tested elsewhere
    def test_filter_with_duplicate_item_ids(self) -> None:
        """Test filtering preserves all interactions with duplicate item_ids."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=5),
            _make_log(id=2, learner_id=2, item_id=5),
            _make_log(id=3, learner_id=3, item_id=5),
            _make_log(id=4, learner_id=1, item_id=3),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
        assert len(result) == 4
        assert all(i.item_id <= 5 for i in result)

    # KEPT: covers single interaction at boundary, complements existing boundary test
    def test_filter_with_single_interaction_at_max_boundary(self) -> None:
        """Test filtering with single interaction exactly at max_item_id boundary."""
        interactions = [_make_log(id=1, learner_id=1, item_id=100)]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=100)
        assert len(result) == 1
        assert result[0].id == 1

    # KEPT: covers single interaction above boundary edge case
    def test_filter_with_single_interaction_above_max_boundary(self) -> None:
        """Test filtering with single interaction above max_item_id returns empty."""
        interactions = [_make_log(id=1, learner_id=1, item_id=101)]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=100)
        assert result == []

    # KEPT: covers large integer values edge case for item_id
    def test_filter_with_large_item_id_values(self) -> None:
        """Test filtering with large integer item_id values."""
        large_value = 2_147_483_647  # Max 32-bit signed int
        interactions = [
            _make_log(id=1, learner_id=1, item_id=large_value),
            _make_log(id=2, learner_id=1, item_id=large_value - 1),
            _make_log(id=3, learner_id=1, item_id=large_value + 1),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=large_value)
        assert len(result) == 2
        assert all(i.item_id <= large_value for i in result)

    # KEPT: covers order preservation property, not tested elsewhere
    def test_filter_preserves_original_order(self) -> None:
        """Test that filtering preserves the original order of interactions."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=3),
            _make_log(id=2, learner_id=1, item_id=1),
            _make_log(id=3, learner_id=1, item_id=5),
            _make_log(id=4, learner_id=1, item_id=2),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=3)
        assert len(result) == 3
        assert [i.id for i in result] == [1, 2, 4]

    # KEPT: covers mixed learner_ids to verify filter only uses item_id
    def test_filter_with_mixed_learner_ids(self) -> None:
        """Test filtering only considers item_id, not learner_id."""
        interactions = [
            _make_log(id=1, learner_id=1, item_id=5),
            _make_log(id=2, learner_id=2, item_id=3),
            _make_log(id=3, learner_id=3, item_id=7),
            _make_log(id=4, learner_id=1, item_id=2),
        ]
        result = filter_by_max_item_id(interactions=interactions, max_item_id=4)
        assert len(result) == 2  # Only item_id 3 and 2 are <= 4
        assert set(i.id for i in result) == {2, 4}


class TestInteractionLogModelEdgeCases:
    """Edge case tests for InteractionLog model."""

    # KEPT: covers None id (unset primary key) edge case
    def test_interaction_log_with_none_id(self) -> None:
        """Test InteractionLog creation with None id (unset primary key)."""
        log = InteractionLog(
            id=None,
            learner_id=1,
            item_id=1,
            kind="attempt",
        )
        assert log.id is None
        assert log.learner_id == 1
        assert log.item_id == 1

    # KEPT: covers zero ids edge case for database model
    def test_interaction_log_with_zero_ids(self) -> None:
        """Test InteractionLog creation with zero values for ids."""
        log = InteractionLog(
            id=0,
            learner_id=0,
            item_id=0,
            kind="attempt",
        )
        assert log.id == 0
        assert log.learner_id == 0
        assert log.item_id == 0

    # KEPT: covers negative ids edge case
    def test_interaction_log_with_negative_ids(self) -> None:
        """Test InteractionLog creation with negative id values."""
        log = InteractionLog(
            id=-1,
            learner_id=-1,
            item_id=-1,
            kind="attempt",
        )
        assert log.id == -1
        assert log.learner_id == -1
        assert log.item_id == -1

    # KEPT: covers empty string kind edge case
    def test_interaction_log_with_empty_kind(self) -> None:
        """Test InteractionLog creation with empty string kind."""
        log = InteractionLog(
            id=1,
            learner_id=1,
            item_id=1,
            kind="",
        )
        assert log.kind == ""

    # KEPT: covers special characters in kind field
    def test_interaction_log_with_special_characters_in_kind(self) -> None:
        """Test InteractionLog creation with special characters in kind."""
        special_kinds = [
            "attempt-123",
            "view_page",
            "click.button",
            "submit:form",
            "navigate/path",
        ]
        for kind in special_kinds:
            log = InteractionLog(
                id=1,
                learner_id=1,
                item_id=1,
                kind=kind,
            )
            assert log.kind == kind

    # KEPT: covers very long kind string edge case
    def test_interaction_log_with_very_long_kind(self) -> None:
        """Test InteractionLog creation with very long kind string."""
        long_kind = "a" * 10000
        log = InteractionLog(
            id=1,
            learner_id=1,
            item_id=1,
            kind=long_kind,
        )
        assert log.kind == long_kind
        assert len(log.kind) == 10000

    # KEPT: covers unicode characters in kind field
    def test_interaction_log_with_unicode_kind(self) -> None:
        """Test InteractionLog creation with unicode characters in kind."""
        log = InteractionLog(
            id=1,
            learner_id=1,
            item_id=1,
            kind="попытка_просмотр_клик",
        )
        assert log.kind == "попытка_просмотр_клик"


class TestInteractionLogCreateModelEdgeCases:
    """Edge case tests for InteractionLogCreate model."""

    # KEPT: covers zero ids in request model
    def test_interaction_create_with_zero_ids(self) -> None:
        """Test InteractionLogCreate with zero values for ids."""
        create = InteractionLogCreate(
            learner_id=0,
            item_id=0,
            kind="attempt",
        )
        assert create.learner_id == 0
        assert create.item_id == 0

    # KEPT: covers negative ids in request model
    def test_interaction_create_with_negative_ids(self) -> None:
        """Test InteractionLogCreate with negative id values."""
        create = InteractionLogCreate(
            learner_id=-1,
            item_id=-1,
            kind="attempt",
        )
        assert create.learner_id == -1
        assert create.item_id == -1

    # KEPT: covers empty kind in request model
    def test_interaction_create_with_empty_kind(self) -> None:
        """Test InteractionLogCreate with empty string kind."""
        create = InteractionLogCreate(
            learner_id=1,
            item_id=1,
            kind="",
        )
        assert create.kind == ""

    # KEPT: covers large integer ids in request model
    def test_interaction_create_with_large_ids(self) -> None:
        """Test InteractionLogCreate with large integer id values."""
        large_value = 2_147_483_647
        create = InteractionLogCreate(
            learner_id=large_value,
            item_id=large_value,
            kind="attempt",
        )
        assert create.learner_id == large_value
        assert create.item_id == large_value


class TestInteractionModelEdgeCases:
    """Edge case tests for InteractionModel response schema."""

    # KEPT: covers epoch timestamp (1970) edge case
    def test_interaction_model_with_zero_timestamp(self) -> None:
        """Test InteractionModel with epoch timestamp."""
        model = InteractionModel(
            id=1,
            learner_id=1,
            item_id=1,
            kind="attempt",
            created_at=datetime(1970, 1, 1, 0, 0, 0),
        )
        assert model.created_at == datetime(1970, 1, 1, 0, 0, 0)

    # KEPT: covers future timestamp edge case
    def test_interaction_model_with_future_timestamp(self) -> None:
        """Test InteractionModel with future timestamp."""
        future_date = datetime(2099, 12, 31, 23, 59, 59)
        model = InteractionModel(
            id=1,
            learner_id=1,
            item_id=1,
            kind="attempt",
            created_at=future_date,
        )
        assert model.created_at == future_date

    # KEPT: covers zero ids in response model
    def test_interaction_model_with_zero_ids(self) -> None:
        """Test InteractionModel with zero values for all ids."""
        model = InteractionModel(
            id=0,
            learner_id=0,
            item_id=0,
            kind="attempt",
            created_at=datetime.now(timezone.utc).replace(tzinfo=None),
        )
        assert model.id == 0
        assert model.learner_id == 0
        assert model.item_id == 0


# DISCARDED: duplicates test_filter_includes_interaction_at_boundary from test_interactions.py
# def test_filter_boundary_duplicate() -> None:
#     """Duplicate test - already covered in test_interactions.py."""
#     interactions = [_make_log(id=1, learner_id=1, item_id=2)]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=2)
#     assert len(result) == 1

# DISCARDED: tests behavior outside module scope (database constraints)
# def test_interaction_log_database_constraints() -> None:
#     """This would require database integration testing."""
#     pass

# DISCARDED: tests pydantic validation which is already handled by the framework
# def test_interaction_model_validation() -> None:
#     """Pydantic handles validation automatically."""
#     pass
