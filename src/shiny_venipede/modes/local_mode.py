from typing import override

from shiny_venipede.modes.mode import Mode
from shiny_venipede.players.metronome_player import MetronomePlayer


class LocalMode(Mode):
    """
    Concrete implementation of Mode for running local battles between two bot1

    Attributes:
        _bot1 (MetronomePlayer): First bot participating in battle.
        _bot2 (MetronomePlayer): Second bot participating in battle.
    """

    def __init__(self, bot1: MetronomePlayer, bot2: MetronomePlayer):
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
