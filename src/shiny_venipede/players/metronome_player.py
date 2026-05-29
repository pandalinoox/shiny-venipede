import random
from typing import override

from poke_env.battle.abstract_battle import AbstractBattle
from poke_env.battle.double_battle import DoubleBattle
from poke_env.player import BattleOrder, DefaultBattleOrder, DoubleBattleOrder, Player

from shiny_venipede.utils.logger import error_logger


class MetronomePlayer(Player):
    """
    Player for Metronome Battle.

    Randomly selects from all valid combined orders in a DoubleBattle.
    Falls back to a default DoubleBattleOrder if no valid orders are available.
    """

    def _get_orders(self, battle: DoubleBattle) -> list[DoubleBattleOrder]:
        """
        Generates all possible combined DoubleBattle orders.

        Args:
            battle (DoubleBattle): Current battle state containing valid orders.

        Returns:
            list[DoubleBattle]: All possible combined orders.
            Returns an empty list if generation fails.
        """
        try:
            orders = DoubleBattleOrder.join_orders(*battle.valid_orders)
            return orders
        except Exception as e:
            error_logger.exception(f"Failed while generating orders: {e}.")
            return []

    @override
    async def choose_move(self, battle: AbstractBattle) -> BattleOrder:
        """
        Selects a move for DoubleBattle using random valid combined order.

        Args:
            battle (AbstractBattle): Current battle state.

        Returns:
            BattleOrder: Selected battle order.

        Raises:
            TypeError: If battle is not DoubleBattle.

        Behavior:
            - Generates valid orders using _get_orders.
            - Randomly selects one if available.
            - Falls back to default DoubleBattleOrder if no valid orders exist.
        """
        if not isinstance(battle, DoubleBattle):
            raise TypeError("MetronomePlayer only supports DoubleBattle instances")
        try:
            orders = self._get_orders(battle)
            if orders:
                return random.choice(orders)
        except Exception as e:
            error_logger.exception(f"Failed while selecting move: {e}.")
        return DoubleBattleOrder(DefaultBattleOrder(), DefaultBattleOrder())
