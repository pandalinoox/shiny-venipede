import pytest
from src.shiny_venipede.players.metronome_player import MetronomePlayer


@pytest.fixture
def metronome_player() -> MetronomePlayer:
    player = MetronomePlayer(start_listening=False)
    return player
