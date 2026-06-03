from poke_env.ps_client import ShowdownServerConfiguration

from shiny_venipede.configs.team_config import MEGA_ABSOL_TEAM
from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.strategies.tera.null_tera_strategy import (
    NULL_TERA_STRATEGY,
)
from shiny_venipede.strategies.tera.tera_strategy import TeraStrategy
from shiny_venipede.utils.player.player_factory import create_player


class PlayerNotSetError(RuntimeError):
    """Raised when a player is requested before being initialized."""


class PlayerManager:
    """
    Manages the lifecycle and configuration of the primary player.

    Attributes:
        _username (str): Username used to authenticate with Showdown.
        _password (str): Password used to authenticate with Showdown.
        _tera_strategy (TeraStrategy): Current tera strategy used by the player.
        _team (str): Current team used by the player.
        _player (MetronomePlayer | None): Managed player instance.
    """

    def __init__(
        self,
        username: str,
        password: str,
        tera_strategy: TeraStrategy = NULL_TERA_STRATEGY,
        team: str = MEGA_ABSOL_TEAM.team,
    ):
        self._username = username
        self._password = password
        self._tera_strategy = tera_strategy
        self._team = team
        self._player: MetronomePlayer | None = None
        self.change_primary_player_with_config(tera_strategy=tera_strategy, team=team)

    @property
    def tera_strategy(self) -> TeraStrategy:
        """
        Returns the currently configured tera strategy.

        Returns:
            TeraStrategy: Active tera strategy.
        """
        return self._tera_strategy

    @property
    def team(self) -> str:
        """
        Returns the currently configured team.

        Returns:
            str: Active team.
        """
        return self._team

    @property
    def player(self) -> MetronomePlayer:
        """
        Returns the managed player.

        Returns:
            MetronomePlayer: Managed player instance.
        """
        return self._request_player()

    def _request_player(self) -> MetronomePlayer:
        """
        Retrieves the managed player.

        Returns:
            MetronomePlayer: Managed player instance.

        Raises:
            PlayerNotSetError: If no player has been initialized.
        """
        if self._player is None:
            raise PlayerNotSetError("Player has not been initialized. ")

        return self._player

    def change_primary_player_with_config(
        self,
        tera_strategy: TeraStrategy | None = None,
        team: str | None = None,
    ) -> None:
        """
        Updates the primary player's configuration and recreates the
        player if required.

        Args:
            tera_strategy (TeraStrategy | None): New tera strategy to
                apply. If None, the current strategy is retained.
            team (str | None): New team to apply. If None, the current
                team is retained.

        Returns:
            None
        """
        new_tera_strategy = (
            tera_strategy if tera_strategy is not None else self._tera_strategy
        )
        new_team = team if team is not None else self._team

        if (
            self._player is not None
            and new_tera_strategy == self._tera_strategy
            and new_team == self._team
        ):
            return  # None when configuration is same.

        self._tera_strategy = new_tera_strategy
        self._team = new_team

        self._player = create_player(
            username=self._username,
            password=self._password,
            team=self._team,
            server_config=ShowdownServerConfiguration,
            tera_strategy=self._tera_strategy,
        )

    async def change_avatar(self, avatar: str) -> None:
        """
        Changes the avatar of the managed player.

        Args:
            avatar (str): Name of the avatar to apply.

        Returns:
            None
        """
        player = self._request_player()
        await player.ps_client.change_avatar(avatar_name=avatar)
