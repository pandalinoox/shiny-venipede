import pytest
from src.shiny_venipede.players.metronome_player import MetronomePlayer


@pytest.fixture
def metronome_player() -> MetronomePlayer:
    player = MetronomePlayer(battle_format="gen9metronomebattle", start_listening=False)
    return player
