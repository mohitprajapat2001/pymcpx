# Contributing

## Getting Started

```bash
git clone https://github.com/your-org/pymcpx.git
cd pymcpx
pip install -e ".[dev]"
```

## Workflow

1. Create a branch: `git checkout -b feat/my-feature`
2. Make changes following the coding style (see `.skills/coding.md`)
3. Add / update tests
4. Run tests: `pytest`
5. Submit a Pull Request

## Adding a New Service

Create a new directory under `pymcpx/services/<name>/`.

Follow `pymcpx/services/calculator/` as the canonical reference.

Required before merging a new service:
- `models.py` — Config, input/output models
- `tools.py` — At least one BaseTool + `MCP_TOOLS`
- `SimulationEngine/` — SimulationEngine with built-in fixtures
- `tests/test_<name>.py` — Covers tools + simulation
- `README.md` — Tool table, quick start

## Pull Request Requirements

- All tests pass
- No new ruff warnings
- New service includes all required files (see above)

## Continuous Integration

CI (``.github/workflows/tests.yml``) runs automatically on **every push and every pull request** across Python 3.11 and 3.12 with coverage reporting. No manual trigger needed.
