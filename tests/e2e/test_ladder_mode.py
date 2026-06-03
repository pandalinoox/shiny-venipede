import pytest
from dotenv import load_dotenv

from shiny_venipede.modes.ladder_mode import LadderMode
from shiny_venipede.strategies.tera.first_turn_tera_strategy import (
    FirstTurnTeraStrategy,
)
from shiny_venipede.utils.player.player_manager import PlayerManager

load_dotenv()


@pytest.mark.e2e
async def test_ladder_battle_completes(
    first_turn_tera_strategy: FirstTurnTeraStrategy, credentials: tuple[str, str]
):

    username, password = credentials

    no_of_battles = 1

    pm = PlayerManager(
        username=username, password=password, tera_strategy=first_turn_tera_strategy
    )

    mode = LadderMode(pm)

    await mode.run_battle(no_of_battles)

    assert pm.player.n_finished_battles == no_of_battles
