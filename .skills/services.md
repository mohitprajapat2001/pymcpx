# Services

## Service Responsibilities

Each service sub-package in `pymcpx/services/<name>/` follows this layout:

```
<name>/
├── __init__.py      ← re-exports full public API
├── models.py        ← Pydantic input + output models
├── tools.py         ← LangChain BaseTool subclasses + MCP_TOOLS
├── utils.py         ← helpers (parsing, conversion logic)
├── README.md        ← service-specific documentation
├── SimulationEngine/← offline engine for testing
│   ├── __init__.py
│   ├── engine.py    ← SimulationEngine class
│   ├── models.py    ← SimulatedResponse, SimulationCall
│   └── utils.py     ← inputs_match(), deep_merge()
└── tests/
    ├── __init__.py
    └── test_<name>.py
```

## Creating a New Service

Create a new directory under `pymcpx/services/<name>/`.

Then implement:
1. `models.py` — input/output models per operation
2. `utils.py` — parsing, conversion helpers
3. `tools.py` — BaseTool subclasses + MCP_TOOLS
4. `SimulationEngine/engine.py` — SimulationEngine with built-in fixtures
5. `tests/test_<name>.py` — unit tests using simulation
6. Update `__init__.py` to re-export everything

Reference: `pymcpx/services/calculator/` is the canonical implementation.

## Installation Strategy

```bash
pip install pymcpx           # core only (pydantic + dotenv)
pip install pymcpx[calculator]   # calculator + langchain-core
pip install pymcpx[datetime]     # datetime + langchain-core
pip install pymcpx[converter]    # converter + langchain-core
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
