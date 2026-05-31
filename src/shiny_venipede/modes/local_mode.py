from typing import override

from poke_env.player import Player

from shiny_venipede.modes.mode import Mode


class LocalMode(Mode):
    """
    Concrete implementation of Mode for running local battles between two bot1

    Attributes:
        _bot1 (Player): First bot participating in battle.
        _bot2 (Player): Second bot participating in battle.
    """

    def __init__(self, bot1: Player, bot2: Player):
        self._bot1 = bot1
        self._bot2 = bot2

    @override
    async def run_battle(self, no_of_battle: int = 1) -> None:
        """
        Runs a specified number of battles between the two configured bots.

        Args:
            no_of_battle (int): Number of battles to execute.
            Defaults to 1.

        Returns:
            None
        """
        await self._bot1.battle_against(self._bot2, n_battles=no_of_battle)
