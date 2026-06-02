from typing import override

from shiny_venipede.modes.mode import Mode
from shiny_venipede.utils.logger import ERROR_LOGGER
from shiny_venipede.utils.player.player_manager import PlayerManager


class LadderMode(Mode):
    """
    Concrete implementation of Mode for running ladder battles.

    Attributes:
        _pm (PlayerManager): Manager used to provide the player
        participating in ladder battle.
    """

    def __init__(self, pm: PlayerManager):
        self._pm = pm

    @override
    async def run_battle(self, no_of_battle: int = 1) -> None:
        """
        Runs a specified number of ladder battles using the configured player.

        Args:
            no_of_battle (int): Number of ladder battles to execute.
            Defaults to 1.

        Returns:
            None
        """
        try:
            await self._pm.player.ladder(n_games=no_of_battle)
        except Exception as e:
            ERROR_LOGGER.exception(f"Error in LadderMode: {e}")
