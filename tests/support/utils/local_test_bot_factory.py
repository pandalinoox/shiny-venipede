from shiny_venipede.configs.team_config import MEGA_ABSOL_TEAM
from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.strategies.tera.null_tera_strategy import NULL_TERA_STRATEGY
from shiny_venipede.strategies.tera.tera_strategy import TeraStrategy
from shiny_venipede.utils.player.player_factory import create_player


def create_local_test_bot(
    username: str,
    team: str = MEGA_ABSOL_TEAM.team,
    tera_strategy: TeraStrategy = NULL_TERA_STRATEGY,
) -> MetronomePlayer:
    return create_player(
        username=username, password=None, team=team, tera_strategy=tera_strategy
    )
