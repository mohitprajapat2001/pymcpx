# Catfacts Service

MCP-compatible LangChain tools for cat facts via the [Cat Fact Ninja API](https://catfact.ninja).

## Prerequisites

No API key required — the [Cat Fact Ninja API](https://catfact.ninja) is free and open.

## Installation

Install the catfacts extra:

```bash
pip install pymcpx[catfacts]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `get_breeds` | `GetBreedsTool` | Fetch a list of cat breeds | `limit` (optional) |
| `get_random_fact` | `GetRandomFactTool` | Fetch a random cat fact | `max_length` (optional) |
| `get_facts` | `GetFactsTool` | Fetch a list of cat facts | `max_length` (optional), `limit` (optional) |

## Usage

### Individual Tools

```python
    from pymcpx.catfacts import GetRandomFactTool

tool = GetRandomFactTool()
result = tool.invoke({"max_length": 100})
print(result)
```

### Toolkit

```python
    from pymcpx.catfacts import CatfactsToolkit

toolkit = CatfactsToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

```python
    from pymcpx.catfacts import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
