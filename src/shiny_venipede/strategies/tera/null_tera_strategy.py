from typing import override

from poke_env.battle.double_battle import DoubleBattle
from poke_env.player import DoubleBattleOrder

from shiny_venipede.strategies.tera.tera_strategy import TeraStrategy


class NullTeraStrategy(TeraStrategy):
    """
    Default no-op TeraStrategy
    """

    @override
    def filter_orders(
        self, battle: DoubleBattle, orders: list[DoubleBattleOrder]
    ) -> list[DoubleBattleOrder] | None:
        """
        No-op filter that disables Terastallization filtering.

        Args:
            battle (DoubleBattle): Current double battle state.
            orders (list[DoubleBattleOrder]): All combined valid orders collection.

        Returns:
            None: Always returns None to indicate no filtering is applied.
        """
        return None


NULL_TERA_STRATEGY = NullTeraStrategy()
