from unittest.mock import AsyncMock, Mock, patch

from shiny_venipede.modes.ladder_mode import LadderMode
from shiny_venipede.utils.logger import ERROR_LOGGER
from shiny_venipede.utils.player.player_manager import PlayerManager


async def test_ladder_mode_run_battle_handles_exception_and_logs():
    pm = Mock(spec=PlayerManager)
    mode = LadderMode(pm=pm)

    with patch.object(
        pm.player,
        "ladder",
        new_callable=AsyncMock,
    ) as ladder_mock:
        ladder_mock.side_effect = Exception("test_error")

        with patch.object(ERROR_LOGGER, "exception") as logger_mock:
            await mode.run_battle(no_of_battle=5)

            ladder_mock.assert_called_once_with(n_games=5)
            logger_mock.assert_called_once()

            args, _ = logger_mock.call_args
            assert "test_error" in str(args[0])
