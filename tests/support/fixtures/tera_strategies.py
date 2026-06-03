import pytest

from shiny_venipede.strategies.tera.first_turn_tera_strategy import (
    FirstTurnTeraStrategy,
    TeraSlot,
)


@pytest.fixture
def first_turn_tera_strategy(request: pytest.FixtureRequest) -> FirstTurnTeraStrategy:
    slot: TeraSlot = getattr(request, "param", 0)
    strategy = FirstTurnTeraStrategy(slot)
    return strategy
