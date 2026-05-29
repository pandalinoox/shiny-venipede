from unittest.mock import MagicMock, PropertyMock

from poke_env.battle.double_battle import DoubleBattle
from poke_env.player import DoubleBattleOrder


class DoubleBattleBuilder:
    def __init__(self) -> None:
        self._battle: DoubleBattle = MagicMock(spec=DoubleBattle)

    def with_turn(self, turn: int) -> DoubleBattleBuilder:
        type(self._battle).turn = PropertyMock(return_value=turn)
        return self

    def with_can_tera(self, can_tera: bool = True) -> DoubleBattleBuilder:
        type(self._battle).can_tera = PropertyMock(return_value=can_tera)
        return self

    def with_valid_orders(self, orders: list[DoubleBattleOrder]) -> DoubleBattleBuilder:
        type(self._battle).valid_orders = PropertyMock(orders)
        return self

    def build(self) -> DoubleBattle:
        return self._battle
