import pytest
from poke_env.battle import DoubleBattle

from tests.support.builders.double_battle_builder import (
    DoubleBattleBuilder,
)
from tests.support.utils.orders import create_default_double_battle_order


@pytest.fixture
def empty_double_battle() -> DoubleBattle:
    battle = DoubleBattleBuilder().with_valid_orders([]).build()
    return battle


@pytest.fixture
def default_double_battle() -> DoubleBattle:
    orders = [create_default_double_battle_order()]
    battle = DoubleBattleBuilder().with_valid_orders(orders).build()
    return battle
