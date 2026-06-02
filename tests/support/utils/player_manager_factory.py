from collections.abc import Iterable
from unittest.mock import MagicMock, Mock

from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.utils.player.player_manager import PlayerManager


def create_manager_with_mock_player(
    create_player_mock: MagicMock,
    player_return_value: Mock | None = None,
    player_side_effect: Iterable[Mock] | None = None,
) -> PlayerManager:

    create_player_mock.side_effect = player_side_effect
    if not player_side_effect:
        create_player_mock.return_value = player_return_value or Mock(
            spec=MetronomePlayer
        )

    return PlayerManager(username="user", password="pass")
