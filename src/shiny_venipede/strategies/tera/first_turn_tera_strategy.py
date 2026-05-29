from typing import Literal, override

from poke_env.battle.double_battle import DoubleBattle
from poke_env.player import DoubleBattleOrder

from shiny_venipede.strategies.tera.tera_strategy import TeraStrategy

type TeraSlot = Literal[0, 1]


class FirstTurnTeraStrategy(TeraStrategy):
    """
    TeraStrategy that allows Terastallization on first turn of the battle.

    Attributes:
        _slot (TeraSlot): Determines which Pokemon slot (0 or 1) is allowed to Terastallize.
        Defaults to slot 0.
    """

    def __init__(self, slot: TeraSlot = 0) -> None:
        self._slot = slot

    @override
    def filter_orders(
        self, battle: DoubleBattle, orders: list[DoubleBattleOrder]
    ) -> list[DoubleBattleOrder] | None:
        """
        Filters orders to only include those that Terastallize on the first turn
        for the configured slot.

        Args:
            battle (DoubleBattle): Current double battle state.
            orders (list[DoubleBattleOrder]): All combined valid orders collection.

        Returns:
            list[DoubleBattle] | None:
                - Filtered list of valid Terastallizing orders if turn is 1.
                - None if not turn 1 or no valid orders exist.
        """
        if battle.turn != 1:
            return None
        tera_orders = [
            o
            for o in orders
            if (
                (self._slot == 0 and o.first_order and o.first_order.terastallize)
                or (self._slot == 1 and o.second_order and o.second_order.terastallize)
            )
        ]
        return tera_orders or None
