from abc import ABC, abstractmethod

from poke_env.battle.double_battle import DoubleBattle
from poke_env.player import DoubleBattleOrder


class TeraStrategy(ABC):
    """
    Abstract base class for Tersatallization selection.
    """

    @abstractmethod
    def filter_orders(
        self, battle: DoubleBattle, orders: list[DoubleBattleOrder]
    ) -> list[DoubleBattleOrder] | None:
        """
        Filters a collection of valid orders.

        Args:
            battle (DoubleBattle): Current double battle state.
            orders (list[DoubleBattleOrder]): All combined valid orders collection.

        Returns:
            list[DoubleBattleOrder] | None: A filtered list of preferred orders, or None if the
            Strategy does not wish to restrict the current orders.
        """
