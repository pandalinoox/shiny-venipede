import random
from typing import Any, override

from poke_env.battle.abstract_battle import AbstractBattle
from poke_env.battle.double_battle import DoubleBattle
from poke_env.player import (
    BattleOrder,
    DefaultBattleOrder,
    DoubleBattleOrder,
    Player,
    SingleBattleOrder,
)
from poke_env.ps_client import (
    AccountConfiguration,
    LocalhostServerConfiguration,
    ServerConfiguration,
)
from poke_env.teambuilder.teambuilder import Teambuilder

from shiny_venipede.strategies.tera.null_tera_strategy import NULL_TERA_STRATEGY
from shiny_venipede.strategies.tera.tera_strategy import TeraStrategy
from shiny_venipede.utils.logger import error_logger


class MetronomePlayer(Player):
    """
    Player for Metronome Battle.

    Randomly selects from all valid combined orders in a DoubleBattle.
    If Terastallization is available, orders may be filtered by the configured tera strategy.
    Falls back to a default DoubleBattleOrder if no valid orders are available.

    Attributes:
        _tera_strategy (TeraStrategy): Strategy to determine which orders may Terastallize.
        Defaults to NULL_TERA_STRATEGY.

    Constants:
        BATTLE_FORMAT: set to gen9metronomebattle
    """

    BATTLE_FORMAT = "gen9metronomebattle"

    def __init__(
        self,
        *args: Any,
        account_configuration: AccountConfiguration | None = None,
        avatar: str | None = None,
        server_configuration: ServerConfiguration = LocalhostServerConfiguration,
        start_listening: bool = True,
        team: str | Teambuilder | None = None,
        tera_strategy: TeraStrategy = NULL_TERA_STRATEGY,
        **kwargs: Any,
    ):
        super().__init__(
            *args,
            account_configuration=account_configuration,
            avatar=avatar,
            battle_format=self.BATTLE_FORMAT,
            server_configuration=server_configuration,
            start_listening=start_listening,
            team=team,
            **kwargs,
        )
        self._tera_strategy = tera_strategy

    def _filter_non_tera_orders(
        self, orders: list[DoubleBattleOrder]
    ) -> list[DoubleBattleOrder]:
        """
        Filters DoubleBattleOrder instances to return only orders without Terastallization.

        Args:
            orders (list[DoubleBattleOrder]): All possible combined orders.

        Returns:
            list[DoubleBattleOrder]: Orders without Terastallization.
        """

        def is_non_tera(order: SingleBattleOrder | None) -> bool:
            return order is not None and not order.terastallize

        non_tera_orders = [
            o
            for o in orders
            if (is_non_tera(o.first_order)) and (is_non_tera(o.second_order))
        ]

        return non_tera_orders

    def _get_orders(self, battle: DoubleBattle) -> list[DoubleBattleOrder]:
        """
        Generates combined DoubleBattle orders, optionally filtered by the configured tera strategy.
        Falls back to non-Terastallized orders if no tera orders are returned.

        Args:
            battle (DoubleBattle): Current battle state containing valid orders.

        Returns:
            list[DoubleBattleOrder]: All possible combined orders, optionally filtered when
            Terastallization is available. Returns an empty list if generation fails.

        Behavior:
            - Returns all orders if Terastallization is unavailable.
            - Filters orders using the configured tera strategy when available.
            - Falls back to non-Terastallized orders if no tera orders are returned.
            - Returns an empty list if generation fails.
        """
        try:
            orders = DoubleBattleOrder.join_orders(*battle.valid_orders)

            if not battle.can_tera:
                return orders

            tera_orders = self._tera_strategy.filter_orders(battle, orders)
            if tera_orders:
                return tera_orders

            non_tera_orders = self._filter_non_tera_orders(orders)
            return non_tera_orders
        except Exception as e:
            error_logger.exception(f"Failed while generating orders: {e}.")
            return []

    @override
    async def choose_move(self, battle: AbstractBattle) -> BattleOrder:
        """
        Selects a move for a DoubleBattle using a random valid combined order.

        Args:
            battle (AbstractBattle): Current battle state.

        Returns:
            BattleOrder: Selected battle order.

        Raises:
            TypeError: If battle is not DoubleBattle.

        Behavior:
            - Generates valid orders using _get_orders.
            - Randomly selects an order if any are available.
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
