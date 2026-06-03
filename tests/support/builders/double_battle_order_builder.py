from poke_env.player import (
    DefaultBattleOrder,
    DoubleBattleOrder,
    SingleBattleOrder,
)


class DoubleBattleOrderBuilder:
    def __init__(self):
        self._first: SingleBattleOrder = DefaultBattleOrder()
        self._second: SingleBattleOrder = DefaultBattleOrder()

    def with_first_order(self, order: SingleBattleOrder) -> DoubleBattleOrderBuilder:
        self._first = order
        return self

    def with_second_order(self, order: SingleBattleOrder) -> DoubleBattleOrderBuilder:
        self._second = order
        return self

    def build(self) -> DoubleBattleOrder:
        return DoubleBattleOrder(self._first, self._second)
