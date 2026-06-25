# MCP Compatibility

## What is MCP?

MCP (Model Context Protocol) is an open standard for exposing tools to AI agents.
Each MCP tool has:
- A `name` (snake_case string, unique)
- A `description` (what the tool does, used by LLMs for selection)
- An `inputSchema` (JSON Schema derived from Pydantic model)

## How PyMCPX Maps to MCP

Each `BaseTool` subclass maps directly to an MCP tool:

```python
class AddTool(BaseTool):
    name: str = "add_numbers"                     # ← MCP tool name
    description: str = "Add two numbers..."       # ← MCP description
    args_schema: type = BinaryFloatInput           # ← MCP inputSchema
```

## Tool Name Convention

`<service>_<operation>` — all lowercase, underscore-separated.

Examples:
- `add_numbers`
- `get_current_time`
- `convert_length`

**Tool names must never be changed after release** — MCP clients hardcode them.

## MCP Tool Registry

Each service exposes a `MCP_TOOLS` list:

```python
from pymcpx.services.calculator import MCP_TOOLS

# Register with an MCP server
mcp_server.register_tools(MCP_TOOLS)
```

## Exporting JSON Schemas

```python
tool = AddTool()
schema = tool.args_schema.model_json_schema()
print(schema)  # → {"title": "BinaryFloatInput", "properties": {...}}
```

## Versioning and Breaking Changes

MCP tool contracts are locked by regression tests.
Any tool name, field rename, or field removal requires a **major version bump**.
