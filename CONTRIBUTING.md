# Contributing to Shiny Venipede

> *You want to join the team? ...*
> *Shiny Venipede wants to battle!*

Thanks for your interest in contributing! Here's everything you need to get started.

---

## Roadmap

These are the open areas where help is most wanted:

| Task | Notes |
|---|---|
| 🖥️ **TUI** | Interactive battle management — `textual` or `rich` would fit well |
| 🧠 **Smarter battle strategies** | Better move selection and tera decision logic |
| 📝 **Better logging** | Structured per-battle logs (JSON or similar) |
| 🏆 **Local tournament mode** | Multi-bot round-robin tournaments |

Feel free to open an issue to discuss an idea before building it.

---

## Dev Setup

**Requirements:** Python 3.14+, [uv](https://github.com/astral-sh/uv) (recommended)

```bash
# Clone and install with all dev dependencies
git clone https://github.com/your-username/shiny-venipede
cd shiny-venipede
uv sync --all-groups
```

Copy `.env.example` to `.env` and fill in your Showdown credentials:

```env
USERNAME=your_showdown_username
PASSWORD=your_showdown_password
```

---

## Project Structure

```
shiny_venipede/
├── __main__.py               ← CLI entry point
├── configs/
│   └── team_config.py        ← team definitions
├── modes/
│   └── ladder_mode.py        ← LadderMode: runs n battles
├── players/
│   └── metronome_player.py   ← MetronomePlayer with stat tracking
├── strategies/
│   └── tera/
│       └── first_turn_tera_strategy.py
└── utils/
    └── player/
        └── player_manager.py ← wires player + credentials + strategy
```

---

## Pre-commit Hooks

Pre-commit runs ruff lint, ruff format, and pyrefly automatically before every commit. Install the hooks once after cloning:

```bash
uv run pre-commit install
```

From then on, every `git commit` will:

1. Fix trailing whitespace and ensure files end with a newline
2. Validate `.yaml` and `.toml` files
3. Run `ruff check --fix` on staged Python files
4. Run `ruff format` on staged Python files
5. Run `pyrefly check` across the whole project

If any hook fails, the commit is blocked until the issues are resolved. Ruff will auto-fix what it can; pyrefly errors need manual attention.

You can also run all hooks manually at any time:

```bash
uv run pre-commit run --all-files
```

---

## Running Tests

**Unit tests** — fast, no network required:

```bash
uv run pytest tests/unit -v --cov=src --cov-report=term-missing
```

**Integration tests** — require a local Pokémon Showdown server (see below):

```bash
uv run pytest tests/integration -v
```

**E2e tests** — require a live Showdown ladder connection, excluded by default:

```bash
uv run pytest -m e2e
```

### Local Showdown Server (required for integration tests)

Integration tests run against a local Pokémon Showdown instance with security disabled. To set one up:

```bash
git clone https://github.com/smogon/pokemon-showdown.git
cd pokemon-showdown
npm install
node pokemon-showdown start --no-security
```

Leave the server running in a separate terminal, then run the integration tests. The CI workflow does this automatically on every PR to `main`.

---

## CI Workflows

Three GitHub Actions workflows run on PRs and pushes:

| Workflow | Trigger | What it runs |
|---|---|---|
| **Quality** | `develop`, `main`, PRs to `main` | `ruff check`, `ruff format --check`, `pyrefly check` |
| **Unit Tests** | `develop`, `main`, PRs to `main` | `pytest tests/unit` with coverage |
| **Integration Tests** | `main`, PRs to `main`, manual | Spins up a local Showdown server, runs `pytest tests/integration` |

All three must pass before a PR can be merged. If you're only working on `develop`, integration tests won't run until you open a PR to `main`.

---

## Writing Tests

```
tests/
├── unit/          ← fast, no network
├── integration/   ← requires a local Showdown server
└── e2e/           ← requires a live Showdown ladder connection
```

Mark any test that needs the real ladder with `@pytest.mark.e2e`. These are excluded from `pytest` by default and never run in CI.

---

## Submitting a PR

1. Fork the repo and create a branch: `git checkout -b feature/your-feature`
2. Make your changes — keep them focused (one feature or fix per PR)
3. Ensure pre-commit hooks, unit tests, and (if relevant) integration tests pass locally
4. Open a PR to `main` with a clear description of what changed and why

If you're fixing a bug, a short note on how to reproduce it is very helpful.

---

## Code Style

- **Formatter:** ruff (double quotes, space indent, LF line endings)
- **Type annotations:** required on all public functions — pyrefly runs in strict mode
- **Docstrings:** Google style, as seen in `__main__.py`
- **Async:** use `async`/`await` throughout; avoid blocking calls in async contexts

---

*May your PRs merge cleanly and your crit rates stay high.* 🎲
