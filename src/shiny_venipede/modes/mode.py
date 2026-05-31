from abc import ABC, abstractmethod


class Mode(ABC):
    """
    Abstract base class representing a battle execution mode.
    """

    @abstractmethod
    async def run_battle(self, no_of_battle: int = 1) -> None:
        """
        Runs one or more battles according to the mode's execution logic.

        Args:
            no_of_battle (int): Number of battles to execute.
            Defaults to 1.

        Returns:
            None
        """
