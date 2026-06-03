from unittest.mock import AsyncMock, Mock, patch

from shiny_venipede.modes.local_mode import LocalMode
from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.utils.logger import ERROR_LOGGER


async def test_local_mode_run_battle_handles_exception_and_logs():
    bot1 = Mock(spec=MetronomePlayer)
    bot2 = Mock(spec=MetronomePlayer)
    mode = LocalMode(bot1=bot1, bot2=bot2)

    with patch.object(
        bot1, "battle_against", new_callable=AsyncMock
    ) as battle_against_mock:
        battle_against_mock.side_effect = Exception("test_error")

        with patch.object(ERROR_LOGGER, "exception") as logger_mock:
            await mode.run_battle(no_of_battle=5)

            battle_against_mock.assert_called_once_with(bot2, n_battles=5)
            logger_mock.assert_called_once()

            args, _ = logger_mock.call_args
            assert "test_error" in str(args[0])
