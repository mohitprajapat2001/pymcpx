# PyMCPX

> **MCP-compatible LangChain tools for AI agents — calculator, datetime, converter, and more.**

[![Python](https://img.shields.io/pypi/pyversions/pymcpx.svg)](https://pypi.org/project/pymcpx/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Features

- 🔌 **MCP-compatible** — every tool exposes a stable name and JSON schema consumable by any MCP host
- 🦜 **LangChain-native** — each tool extends `BaseTool` with typed `args_schema`
- 🧱 **Pydantic v2** — validated inputs and outputs
- 🧪 **Simulation engine** — run agent workflows offline without any API keys
- 📦 **Service extras** — install only what you need: `pip install pymcpx[calculator]`

---

## Installation

```bash
# Core package (no service dependencies)
pip install pymcpx

# Specific service
pip install pymcpx[calculator]
pip install pymcpx[datetime]
pip install pymcpx[converter]

# All services
pip install pymcpx[all]

# Development
pip install pymcpx[dev]
```

## Services

For full details on the tools, schemas, and offline simulation engines of each service, refer to their respective service-level `README.md` files:

| Service          | Status         | Install Extra          | Documentation                                        |
| ---------------- | -------------- | ---------------------- | ---------------------------------------------------- |
| **Calculator**   | ✅ Ready       | `pymcpx[calculator]`   | [README](pymcpx/services/calculator/README.md)       |
| **Converter**    | ✅ Ready       | `pymcpx[converter]`    | [README](pymcpx/services/converter/README.md)        |
| **Datetime**     | ✅ Ready       | `pymcpx[datetime]`     | [README](pymcpx/services/datetime/README.md)         |
| **IPstack**      | ✅ Ready       | `pymcpx[ipstack]`      | [README](pymcpx/services/ipstack/README.md)          |
| **Marketstack**  | ✅ Ready       | `pymcpx[marketstack]`  | [README](pymcpx/services/marketstack/README.md)      |
| **Weatherstack** | ✅ Ready       | `pymcpx[weatherstack]` | [README](pymcpx/services/weatherstack/README.md)     |
| **Numverify**    | ✅ Ready       | `pymcpx[numverify]`    | [README](pymcpx/services/numverify/README.md)        |
| **Fixer**        | ✅ Ready       | `pymcpx[fixer]`        | [README](pymcpx/services/fixer/README.md)            |
| **Aviationstack** | ✅ Ready       | `pymcpx[aviationstack]` | [README](pymcpx/services/aviationstack/README.md)   |

## Contributing

### Getting Started

```bash
git clone https://github.com/your-org/pymcpx.git
cd pymcpx
pip install -e ".[dev]"
```

### Workflow

1. Create a branch: `git checkout -b feat/my-feature`
2. Make changes following the coding conventions
3. Add / update tests
4. Run tests: `pytest`
5. Submit a Pull Request

### Adding a New Service

Create a new directory under `pymcpx/services/<name>/` following the layout of `pymcpx/services/ipstack/`:

- `SimulationEngine/models.py` — Pydantic input models
- `SimulationEngine/utils.py` — business logic, API clients
- `tools.py` — `BaseTool` subclasses + `MCP_TOOLS` list
- `SimulationEngine/engine.py` — offline simulation engine
- `tests/test_<name>.py` — unit tests with `respx` mocks
- `README.md` — service documentation including:
  - Prerequisites (API key setup)
  - Installation command
  - Tools table with names, classes, descriptions, and input keys
  - Usage examples (individual tools, toolkit, MCP integration)

Then add a re-export shim at `pymcpx/<name>.py`, register the optional dependency in `pyproject.toml`, and add the service row to the README Services table.

### Pull Request Requirements

- All tests pass
- No new ruff warnings
- New services include all required files (see above)

### Continuous Integration

CI (`.github/workflows/tests.yml`) runs automatically on every push and pull request across Python 3.11 and 3.12 with coverage reporting.

## License

MIT © PyMCPX Contributors
