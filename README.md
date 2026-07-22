# PyMCPX

> **MCP-compatible LangChain tools for AI agents — calculator, datetime, converter, and more.**

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://pypi.org/project/pymcpx/)
[![License: MIT](https://img.shields.io/badge/MIT-red?style=for-the-badge)](LICENSE)
[![Pypi: Pymcpx](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](PyPi)

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

| Service               | Auth     | Status   | Install Extra                   | Documentation                                        |
| --------------------- | -------- | -------- | ------------------------------- | ---------------------------------------------------- |
| **Aviationstack**     | API Key  | ✅ Ready | `pymcpx[aviationstack]`        | [README](pymcpx/services/aviationstack/README.md)    |
| **Calculator**        | None     | ✅ Ready | `pymcpx[calculator]`            | [README](pymcpx/services/calculator/README.md)       |
| **Cataas**            | None     | ✅ Ready | `pymcpx[cataas]`                | [README](pymcpx/services/cataas/README.md)           |
| **Catfacts**          | None     | ✅ Ready | `pymcpx[catfacts]`              | [README](pymcpx/services/catfacts/README.md)         |
| **Converter**         | None     | ✅ Ready | `pymcpx[converter]`             | [README](pymcpx/services/converter/README.md)        |
| **Datetime**          | None     | ✅ Ready | `pymcpx[datetime]`              | [README](pymcpx/services/datetime/README.md)         |
| **Dogapi**            | None     | ✅ Ready | `pymcpx[dogapi]`                | [README](pymcpx/services/dogapi/README.md)           |
| **ExchangeRate.host** | API Key  | ✅ Ready | `pymcpx[exchangeratehost]`      | [README](pymcpx/services/exchangeratehost/README.md) |
| **Fixer**             | API Key  | ✅ Ready | `pymcpx[fixer]`                 | [README](pymcpx/services/fixer/README.md)            |
| **IPstack**           | API Key  | ✅ Ready | `pymcpx[ipstack]`               | [README](pymcpx/services/ipstack/README.md)          |
| **Marketstack**       | API Key  | ✅ Ready | `pymcpx[marketstack]`           | [README](pymcpx/services/marketstack/README.md)      |
| **Numverify**         | API Key  | ✅ Ready | `pymcpx[numverify]`             | [README](pymcpx/services/numverify/README.md)        |
| **Screenshotlayer**   | API Key  | ✅ Ready | `pymcpx[screenshotlayer]`       | [README](pymcpx/services/screenshotlayer/README.md)  |
| **Weatherstack**      | API Key  | ✅ Ready | `pymcpx[weatherstack]`          | [README](pymcpx/services/weatherstack/README.md)     |
| **Zenserp**           | API Key  | ✅ Ready | `pymcpx[zenserp]`               | [README](pymcpx/services/zenserp/README.md)          |

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

## Special Thanks

Special thanks to the [Public APIs](https://github.com/public-apis/public-apis) repository, a manually curated list of public APIs from many domains, which serves as a treasure trove of APIs and inspired our external service integrations.

## License

MIT © PyMCPX Contributors
