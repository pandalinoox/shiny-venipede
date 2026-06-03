from unittest.mock import Mock

from poke_env.player import DefaultBattleOrder, SingleBattleOrder


class SingleBattleOrderBuilder:
    def __init__(self):
        self._order: SingleBattleOrder = Mock(spec=DefaultBattleOrder)

    def with_terastallize(self, tera: bool = True) -> SingleBattleOrderBuilder:
        type(self._order).terastallize = tera
        return self

    def build(self) -> SingleBattleOrder:
        return self._order
