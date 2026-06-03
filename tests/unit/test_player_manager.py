from typing import Final
from unittest.mock import AsyncMock, Mock, patch

import pytest
from tests.support.utils.player_manager_factory import create_manager_with_mock_player

from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.utils.player.player_manager import (
    PlayerManager,
    PlayerNotSetError,
)

PM_CREATE_PLAYER_PATCH_PATH: Final = (
    "shiny_venipede.utils.player.player_manager.create_player"
)


def test_player_property_raises_if_not_initialized() -> None:
    manager = PlayerManager.__new__(PlayerManager)
    manager._player = None

    with pytest.raises(PlayerNotSetError):
        _ = manager.player


def test_change_primary_player_creates_player() -> None:
    with patch.object(PlayerManager, "_player", new_callable=Mock, create=True):
        with patch(PM_CREATE_PLAYER_PATCH_PATH) as create_player_mock:
            fake_player = Mock(spec=MetronomePlayer)
            manager = create_manager_with_mock_player(
                create_player_mock=create_player_mock, player_return_value=fake_player
            )

            assert manager.player == fake_player
            create_player_mock.assert_called_once()


def test_change_primary_player_updates_when_config_changes() -> None:
    with patch(PM_CREATE_PLAYER_PATCH_PATH) as create_player_mock:
        first_player = Mock(spec=MetronomePlayer)
        second_player = Mock(spec=MetronomePlayer)

        manager = create_manager_with_mock_player(
            create_player_mock=create_player_mock,
            player_side_effect=[first_player, second_player],
        )

        manager.change_primary_player_with_config(team="new_team")

        assert manager.player == second_player
        assert create_player_mock.call_count == 2


def test_change_primary_player_no_op_if_same_config() -> None:
    with patch(PM_CREATE_PLAYER_PATCH_PATH) as create_player_mock:
        manager = create_manager_with_mock_player(create_player_mock=create_player_mock)
        create_player_mock.reset_mock()

        manager.change_primary_player_with_config(
            tera_strategy=manager.tera_strategy,
            team=manager.team,
        )

        create_player_mock.assert_not_called()


async def test_change_avatar_calls_ps_client() -> None:
    with patch(PM_CREATE_PLAYER_PATCH_PATH) as create_player_mock:
        ps_client = Mock()
        ps_client.change_avatar = AsyncMock()

        player = Mock(spec=MetronomePlayer)
        player.ps_client = ps_client

        manager = create_manager_with_mock_player(
            create_player_mock=create_player_mock, player_return_value=player
        )

        await manager.change_avatar("test_avatar")

        ps_client.change_avatar.assert_called_once_with(avatar_name="test_avatar")


def test_request_player_direct_access_works() -> None:
    with patch(PM_CREATE_PLAYER_PATCH_PATH) as create_player_mock:
        player = Mock(spec=MetronomePlayer)
        manager = create_manager_with_mock_player(
            create_player_mock=create_player_mock, player_return_value=player
        )

        assert manager.player is player
