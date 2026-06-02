import argparse
import asyncio
import os

from dotenv import load_dotenv

from shiny_venipede.configs.team_config import MEGA_ABSOL_TEAM
from shiny_venipede.modes.ladder_mode import LadderMode
from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.strategies.tera.first_turn_tera_strategy import (
    FirstTurnTeraStrategy,
)
from shiny_venipede.utils.player.player_manager import PlayerManager

load_dotenv()


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for running ladder battles.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Run ladder battles")
    parser.add_argument(
        "battles",
        nargs="?",
        default=1,
        type=int,
        help="number of ladder battles to run",
    )
    return parser.parse_args()


def print_stats(player: MetronomePlayer) -> None:
    """
    Print statistics of a player's ladder battles.

    Args:
        player (MetronomePlayer): Player whose stats to print.
    """
    print(f"No. of wins: {player.n_won_battles}")
    print(f"Win rate: {player.win_rate}")
    battles = list(player.battles.values())
    print(f"Rating: {battles[-1].rating}")


def main() -> None:
    """
    Main entry point to run ladder battles using the configured player.
    """
    args = parse_args()
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    DEFUALT_TERA_STRATEGY = FirstTurnTeraStrategy(0)
    DEFAULT_TEAM = MEGA_ABSOL_TEAM.team

    pm = PlayerManager(
        username=USERNAME,
        password=PASSWORD,
        tera_strategy=DEFUALT_TERA_STRATEGY,
        team=DEFAULT_TEAM,
    )
    mode = LadderMode(pm)
    asyncio.run(mode.run_battle(no_of_battle=args.battles))
    print_stats(pm.player)


if __name__ == "__main__":
    main()
