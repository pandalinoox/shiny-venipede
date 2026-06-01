import pytest

from shiny_venipede.players.metronome_player import MetronomePlayer


@pytest.fixture
def offline_metronome_player() -> MetronomePlayer:
    player = MetronomePlayer(start_listening=False)
    return player
