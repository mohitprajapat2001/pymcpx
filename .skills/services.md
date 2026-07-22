# Services

## Service Responsibilities

Each service sub-package in `pymcpx/services/<name>/` follows this layout:

```
<name>/
├── __init__.py        ← re-exports full public API
├── tools.py           ← LangChain BaseTool subclasses + MCP_TOOLS list
├── README.md          ← service-specific documentation (auth requirements, tools, usage)
├── SimulationEngine/  ← implementation + offline engine for testing
│   ├── __init__.py    ← re-exports engine, models, utils
│   ├── engine.py      ← SimulationEngine class (run, register, history)
│   ├── models.py      ← Pydantic input/output models (LookupIPInput, etc.)
│   └── utils.py       ← business logic, API clients, helpers
└── tests/
    ├── __init__.py
    └── test_<name>.py  ← unit tests using SimulationEngine
```

Key points:
- **`tools.py`** always lives at service root — defines BaseTool subclasses
- **`models.py`** and **`utils.py`** live inside `SimulationEngine/` — this ensures the simulation layer owns the full implementation
- The service's `__init__.py` re-exports from `SimulationEngine` and `tools`

## Creating a New Service

Create a new directory under `pymcpx/services/<name>/`.

Then implement:
1. `SimulationEngine/models.py` — Pydantic input models for each tool operation
2. `SimulationEngine/utils.py` — business logic, parsing, API client helpers
3. `tools.py` — BaseTool subclasses + MCP_TOOLS list
4. `SimulationEngine/engine.py` — SimulationEngine class (register/run/reset/history)
5. `tests/test_<name>.py` — unit tests using simulation
6. Update `__init__.py` to re-export everything
7. Add `pymcpx/<name>.py` — top-level re-export shim so users can `from pymcpx.<name> import ...`
8. Register optional dependency in `pyproject.toml`
9. Document authentication requirements in the service `README.md` — state the env var name if an API key is needed, or note that no API key is required

Reference: `pymcpx/services/calculator/` is the canonical implementation.

## Installation Strategy

```bash
pip install pymcpx           # core only (pydantic + dotenv)
pip install pymcpx[calculator]   # calculator + langchain-core
pip install pymcpx[converter]    # converter + langchain-core
pip install pymcpx[datetime]     # datetime + langchain-core
pip install pymcpx[ipstack]      # ipstack + langchain-core + httpx
pip install pymcpx[all]          # all services
```

Service extras are declared in `pyproject.toml [project.optional-dependencies]`.
Add a new section for each service you add.

## Service Tools

Services expose tools directly without configuration:

```python
    from pymcpx.calculator import AddTool

tool = AddTool()
result = tool.invoke({"a": 3, "b": 4})
print(result)  # "7"
```
