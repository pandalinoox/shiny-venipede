import os

import pytest
from dotenv import load_dotenv

from tests.support.fixtures.battles import default_double_battle, empty_double_battle
from tests.support.fixtures.players import (
    offline_metronome_player,
)
from tests.support.fixtures.tera_strategies import first_turn_tera_strategy

__all__ = [
    "default_double_battle",
    "empty_double_battle",
    "offline_metronome_player",
    "first_turn_tera_strategy",
]

load_dotenv()


@pytest.fixture(scope="session")
def credentials():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    assert username is not None, "USERNAME env var is required"
    assert password is not None, "PASSWORD env var is required"

    return username, password
