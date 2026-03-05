"""Edge cases and boundary value tests for interactions."""

import pytest
from datetime import datetime, timedelta
from app.models.interaction import InteractionLog


def test_create_interaction_with_minimum_values():
    """Test creating interaction with minimum valid values - just test the model creation."""
    # Test only the model creation without DB
    interaction = InteractionLog(
        learner_id=1,
        item_id=1,
        kind="a"  # minimum length string
    )
    
    assert interaction.learner_id == 1
    assert interaction.item_id == 1
    assert interaction.kind == "a"
    assert interaction.kind == "a"


def test_create_interaction_with_maximum_kind_length():
    """Test creating interaction with maximum kind length (50 chars) - model creation only."""
    long_kind = "x" * 50
    interaction = InteractionLog(
        learner_id=1,
        item_id=1,
        kind=long_kind
    )
    
    assert interaction.learner_id == 1
    assert interaction.item_id == 1
    assert len(interaction.kind) == 50
    assert interaction.kind == long_kind


def test_create_interaction_with_future_timestamp():
    """Test creating interaction with future timestamp - model creation only."""
    future_time = datetime.utcnow() + timedelta(days=365)
    interaction = InteractionLog(
        learner_id=1,
        item_id=1,
        kind="test",
        created_at=future_time
    )
    
    assert interaction.learner_id == 1
    assert interaction.item_id == 1
    assert interaction.kind == "test"
    assert interaction.created_at == future_time