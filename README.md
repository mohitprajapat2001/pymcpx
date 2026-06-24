# PyMCPX

> **MCP-compatible LangChain tools for AI agents — calculator, datetime, converter, and more.**

[![PyPI](https://img.shields.io/pypi/v/pymcpx.svg)](https://pypi.org/project/pymcpx/)
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

---

## Quick Start

### Calculator

```python
from pymcpx.calculator import AddTool, DivideTool

add = AddTool()
result = add.invoke({"a": 3, "b": 4})
print(result)  # "7"

div = DivideTool()
result = div.invoke({"a": 10, "b": 2})
print(result)  # "5"
```

### Offline Simulation (No API Key Needed)

```python
from pymcpx.datetime import DatetimeSimulationEngine

engine = DatetimeSimulationEngine()

result = engine.run("get_current_time", {"timezone": "UTC"})
print(result)  # e.g. "2026-06-24T12:00:00+0000"

# Inspect the call history
for call in engine.history:
    print(f"{call.tool_name}: {call.inputs}")
```

### MCP Registration

```python
from pymcpx.calculator import MCP_TOOLS

# Register all calculator tools with your MCP server
mcp_server.register_tools(MCP_TOOLS)
```

---

## Services

For full details on the tools, schemas, and offline simulation engines of each service, refer to their respective service-level `README.md` files:

| Service        | Status         | Install Extra        | Documentation                                  |
| -------------- | -------------- | -------------------- | ---------------------------------------------- |
| **Calculator** | ✅ Ready       | `pymcpx[calculator]` | [README](pymcpx/services/calculator/README.md) |
| **Datetime**   | ✅ Ready       | `pymcpx[datetime]`   | [README](pymcpx/services/datetime/README.md)   |
| **Converter**  | ✅ Ready       | `pymcpx[converter]`  | [README](pymcpx/services/converter/README.md)  |

**Planned:** GitHub, Slack, Jira, Gmail, Notion, GitLab, Linear, Discord, Google Drive, Weather, News, SerpAPI, Reddit, LinkedIn, YouTube, Twitter

---

## Demos

Interactive Jupyter notebooks are provided under `demos/` to help you explore each service with a real LLM.

```bash
# From the repo root
pip install -e ".[dev]"
pip install -r demos/requirements.txt
cp demos/.env.example demos/.env
# edit demos/.env with your API key (Gemini, Groq, or local Ollama)
jupyter notebook demos/calculator/basic_operations.ipynb
```

The demo notebooks let you choose your LLM provider via `.env`:

| Provider | Env value       | Required key          |
|----------|----------------|-----------------------|
| **Gemini**  | `gemini`    | `GEMINI_API_KEY`      |
| **Groq**    | `groq`      | `GROQ_API_KEY`        |
| **Local**   | `local`     | (Ollama running locally) |

---

## Project Structure

```
pymcpx/
├── pymcpx/
│   ├── services/          ← internal service implementations
│   │   ├── calculator/    ← arithmetic tools + simulation engine
│   │   ├── datetime/      ← date/time tools + simulation engine
│   │   └── converter/     ← unit conversion tools + simulation engine
│   ├── calculator.py      ← re-export shim (public API)
│   ├── datetime.py
│   ├── converter.py
│   └── __init__.py
├── demos/                 ← interactive Jupyter notebooks
├── .skills/               ← project knowledge base
├── .github/workflows/     ← CI, tests
└── pyproject.toml
```

## Adding a New Service

Create a new directory under `pymcpx/services/<name>/` with the following files:

- `__init__.py` — re-export public API
- `models.py` — Pydantic config, input, output models
- `tools.py` — LangChain `BaseTool` subclasses + `MCP_TOOLS` list
- `SimulationEngine/` — offline engine with fixture support
- `README.md` — service documentation
- `tests/` — unit tests

Then create a re-export shim at `pymcpx/<name>.py` (see existing services for reference).

---

## Contributing

See [`.skills/contributing.md`](.skills/contributing.md) for the full guide.

## License

MIT © PyMCPX Contributors
