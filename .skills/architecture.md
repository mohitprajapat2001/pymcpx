# Architecture

## Design Philosophy

PyMCPX follows a **service-first architecture**. Each external service is a
fully self-contained module that lives in `pymcpx/services/<name>/`.

## Directory Structure

```
pymcpx/
├── pymcpx/
│   ├── services/          ← one sub-package per external service
│   │   └── github/
│   │       ├── __init__.py     ← public API re-exports
│   │       ├── tools.py        ← LangChain BaseTool subclasses
│   │       ├── models.py       ← Pydantic v2 models
│   │       ├── utils.py        ← helpers (headers, errors, pagination)
│   │       ├── simulation/     ← offline engine + fixtures
│   │       └── tests/          ← service-level unit tests
│   ├── regression_tests/  ← cross-release contract tests
│   ├── scenario_tests/    ← multi-step agent workflow tests
│   └── skills/            ← shared cross-service primitives
```

## Import Convention

Every `services/<name>/__init__.py` re-exports the complete public surface
so users never need to know internal file structure:

```python
from pymcpx.services.github import GitHubSearchRepositoriesTool
from pymcpx.services.github import *  # wildcard also works
```

## Tool Design

Each tool:
1. Extends `langchain_core.tools.BaseTool`
2. Declares `args_schema: type = <InputModel>` (Pydantic v2)
3. Is MCP-compatible: `name`, `description`, `args_schema` map directly to MCP tool definitions
4. Lives in `tools.py` alongside a `MCP_TOOLS: list[BaseTool]` registry

## Separation of Concerns

| File | Responsibility |
|------|---------------|
| `tools.py` | LangChain tools, MCP definitions, HTTP calls |
| `models.py` | Pydantic config, input, output models |
| `utils.py` | Headers, error classes, pagination, string helpers |
| `simulation/` | Offline engine, fixtures, replay |
| `tests/` | Unit + integration tests |

## Adding a New Service

```bash
python scripts/create_service.py <service_name>
```

Follow `pymcpx/services/github/` as the reference implementation.
