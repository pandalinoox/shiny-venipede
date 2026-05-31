from tests.support.utils.local_test_bot_factory import create_local_test_bot

from shiny_venipede.modes.local_mode import LocalMode
from shiny_venipede.strategies.tera.first_turn_tera_strategy import (
    FirstTurnTeraStrategy,
)


async def test_real_battle_completes():
    bot1 = create_local_test_bot(username="bot1", tera_strategy=FirstTurnTeraStrategy())
    bot2 = create_local_test_bot(username="bot2")

    no_of_battles = 10

    mode = LocalMode(bot1, bot2)

    await mode.run_battle(no_of_battles)

    assert bot1.n_finished_battles == no_of_battles
    assert bot2.n_finished_battles == no_of_battles
