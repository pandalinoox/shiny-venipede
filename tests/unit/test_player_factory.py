from unittest.mock import patch

from shiny_venipede.players.metronome_player import MetronomePlayer
from shiny_venipede.utils.player.player_factory import create_player


def test_create_player_returns_player_instance():
    with patch("poke_env.player.Player.__init__", return_value=None) as mock_init:
        player = create_player(username="u", password=None, team="team")

        assert isinstance(player, MetronomePlayer)
        mock_init.assert_called()
