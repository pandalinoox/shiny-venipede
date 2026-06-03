# ✨ Shiny Venipede

> *A wild bot appeared! It's using automated ladder battles!*

A Pokémon Showdown bot built for `gen9metronomebattle` — fully async, stat-tracking, and ready to grind the ladder so you don't have to.

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=flat-square&logo=python&logoColor=white)
![poke-env](https://img.shields.io/badge/poke--env-0.15.0+-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Format](https://img.shields.io/badge/Format-gen9metronomebattle-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## Features

- ⚔️ **Automated ladder battles** — configure once, battle endlessly
- 📊 **Battle stat tracking** — wins, win rate, and rating after every session
- ⚙️ **Easy configuration** — plug in your team and strategy via simple config files
- ⚡ **Fully asynchronous** — faster battle simulations without blocking

---

## Planned Features

- [ ] 🖥️ **TUI** — a slick text user interface for interactive battle management
- [ ] 🧠 **Smart Tera Strategy** — smarter in-battle decision making
- [ ] 📝 **Improved Battle Logging** — detailed per-battle logs
- [ ] 🏆 **Local Tournament Mode** — run multiplayer tournaments locally with multiple bot players

---

## How It Works

```
venipede <n>
    │
    ▼
parse_args()          ← argparse, defaults to 1 battle
    │
    ▼
PlayerManager         ← wraps credentials + MetronomePlayer
  ├── USERNAME / PASSWORD   (from .env)
  ├── FirstTurnTeraStrategy (tera strategy)
  └── MEGA_ABSOL_TEAM       (team config)
    │
    ▼
LadderMode.run_battle(no_of_battles=n)    ← async via asyncio.run()
  └── queues into gen9metronomebattle on Pokémon Showdown
      plays n battles using poke-env under the hood
    │
    ▼
print_stats(player)
  ├── n_won_battles
  ├── win_rate
  └── battles[-1].rating    ← final ladder rating
```

`PlayerManager` wires together the player, credentials, and strategy before handing off to `LadderMode`, which handles the actual Showdown connection via [poke-env](https://github.com/hsahovic/poke-env). Everything runs inside a single `asyncio.run()` call so battles can be awaited cleanly.

---

## Installation

Make sure you have **Python 3.14+** installed. Then install in editable mode:

```bash
pip install -e .
```

This makes the `venipede` command available globally.

> **Heads up:** The project uses [uv](https://github.com/astral-sh/uv) as its build backend. If you're using uv (recommended), `uv sync` will handle everything including dev dependencies.

---

## Usage

```bash
venipede [no_of_battles]
```

| Command | Description |
|---|---|
| `venipede` | Run 1 battle |
| `venipede 5` | Run 5 battles |
| `venipede 100` | Run 100 battles (go touch grass) |

After all battles finish, your session stats are printed:

```
No. of wins: 4
Win rate: 80%
Rating: 1312
```

---

## Configuration

**Step 1 — Create a `.env` file** in the project root:

```env
USERNAME=your_showdown_username
PASSWORD=your_showdown_password
```

**Step 2 — Configure your team and strategy** in:

```
shiny_venipede/configs/team_config.py   ← swap in your own team export
shiny_venipede/strategies/              ← implement a custom tera strategy
```

The default setup uses `MEGA_ABSOL_TEAM` with `FirstTurnTeraStrategy`, which terastallizes on the first available turn.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

## License

MIT License © 2026 — panda
