from poke_env.ps_client import (
    AccountConfiguration,
    LocalhostServerConfiguration,
    ServerConfiguration,
)

from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.strategies.tera.null_tera_strategy import NULL_TERA_STRATEGY
from shiny_venipede.strategies.tera.tera_strategy import TeraStrategy


def create_player(
    username: str,
    password: None | str,
    team: str,
    server_config: ServerConfiguration = LocalhostServerConfiguration,
    avatar: str = "erika-gen1rb",
    tera_strategy: TeraStrategy = NULL_TERA_STRATEGY,
) -> MetronomePlayer:
    """
    Factory functions for creating a configured Shodown Player instance.
    The Function creates a `MetronomePlayer` which is configured to play gen9metronomebattle format.

    Args:
        username (str): Account username for the player.
        password (None | str): Account password (None for local or guest servers).
        team (str): Pokémon team definition in Showdown format.
        server_config (ServerConfiguration): Server configuration to connect to.
        Defaults to LocalhostServerConfiguration.
        avatar (str): Player avatar identifier used in Pokémon Showdown.
        Defaults to "erika-gen1rb".
        tera_strategy (TeraStrategy): Strategy used for Terastallization decisions.
        Defaults to NULL_TERA_STRATEGY.

    Returns:
        Configured MetronomePlayer object.
    """
    account_config = AccountConfiguration(username, password)
    player = MetronomePlayer(
        account_configuration=account_config,
        avatar=avatar,
        server_configuration=server_config,
        team=team,
        tera_strategy=tera_strategy,
    )
    return player
