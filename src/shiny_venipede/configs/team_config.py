from dataclasses import dataclass


@dataclass(frozen=True)
class TeamConfig:
    """
    Immutable configuration object representing a Pokemon team.

    Args:
        name (str): Human-readable name of the team configuration.
        team (str): Full team definition string in Pokémon Showdown format.
    """

    name: str
    team: str


MEGA_ABSOL_TEAM = TeamConfig(
    name="Mega Absol Team",
    team="""
    Absol-Mega-Z @ Booster Energy
    Ability: Protosynthesis
    Tera Type: Stellar
    EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe
    Lonely Nature
    - Metronome

    Chandelure-Mega @ Mirror Herb
    Ability: Spicy Spray
    EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe
    Hasty Nature
    - Metronome
    """,
)
