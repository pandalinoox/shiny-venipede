import pytest
from poke_env.battle import DoubleBattle

from tests.support.builders.double_battle_builder import (
    DoubleBattleBuilder,
)
from tests.support.builders.double_battle_order_builder import DoubleBattleOrderBuilder


@pytest.fixture
def empty_double_battle() -> DoubleBattle:
    battle = DoubleBattleBuilder().with_valid_orders([]).build()
    return battle


@pytest.fixture
def default_double_battle() -> DoubleBattle:
    orders = [DoubleBattleOrderBuilder().build()]
    battle = DoubleBattleBuilder().with_valid_orders(orders).build()
    return battle
