# Architecture

## Design Philosophy

PyMCPX follows a **service-first architecture**. Each external service is a
fully self-contained module that lives in `pymcpx/services/<name>/`.

## Directory Structure

```
pymcpx/
├── pymcpx/
│   ├── services/          ← one sub-package per service
│   │   ├── calculator/    ← arithmetic tools + simulation engine
│   │   ├── datetime/      ← date/time tools + simulation engine
│   │   └── converter/     ← unit conversion tools + simulation engine
```

## Import Convention

Every `services/<name>/__init__.py` re-exports the complete public surface
so users never need to know internal file structure:

```python
    from pymcpx.calculator import AddTool
    from pymcpx.calculator import *  # wildcard also works
```

## Tool Design

Each tool:
1. Extends `langchain_core.tools.BaseTool`
2. Declares `args_schema: type = <InputModel>` (Pydantic v2)
3. Is MCP-compatible: `name`, `description`, `args_schema` map directly to MCP tool definitions
4. Lives in `tools.py` (or `arithmetic_tools.py`) alongside a `MCP_TOOLS: list[BaseTool]` registry

## Separation of Concerns

| File | Responsibility |
|------|---------------|
| `tools.py` | LangChain tools, MCP definitions |
| `models.py` | Pydantic config, input, output models |
| `utils.py` | Helpers, conversion logic |
| `SimulationEngine/` | Offline engine, fixtures, replay |
| `tests/` | Unit tests |

## Adding a New Service

Create a new directory under `pymcpx/services/<name>/` with `__init__.py`, `tools.py`, `models.py`, `SimulationEngine/`, and `tests/`.

Follow `pymcpx/services/calculator/` as the reference implementation.
