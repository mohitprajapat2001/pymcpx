# Contributing

## Getting Started

```bash
git clone https://github.com/your-org/pymcpx.git
cd pymcpx
python scripts/bootstrap.py
```

## Workflow

1. Create a branch: `git checkout -b feat/my-feature`
2. Make changes following the coding style (see `.skills/coding.md`)
3. Add / update tests
4. Run pre-commit: `pre-commit run --all-files`
5. Run tests: `python scripts/test.py`
6. Submit a Pull Request

## Adding a New Service

```bash
python scripts/create_service.py <name>
```

Follow `pymcpx/services/github/` as the canonical reference.

Required before merging a new service:
- `models.py` — Config, at least one Input + Output model
- `tools.py` — At least one BaseTool + `MCP_TOOLS`
- `simulation/engine.py` — SimulationEngine with built-in fixtures
- `tests/test_<name>.py` — Covers models + simulation
- `regression_tests/<name>/test_<name>_regression.py` — Locks tool names + schema
- `scenario_tests/<name>/test_<name>_scenarios.py` — At least one multi-step scenario
- `README.md` — Tool table, quick start, env vars

## Pre-commit Checks

Pre-commit runs automatically on `git commit`:
- `trailing-whitespace`
- `end-of-file-fixer`
- `check-yaml` / `check-toml`
- `pyupgrade` (Python 3.11+ syntax)
- `ruff` (lint + auto-fix)
- `ruff-format` (format)

## Pull Request Requirements

- All tests pass
- No new ruff warnings
- New service includes all required files (see above)
- CHANGELOG.md updated for user-facing changes
