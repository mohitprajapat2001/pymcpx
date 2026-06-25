# Numverify Service

MCP-compatible LangChain tools for phone number validation and country lookup via the [Numverify API](https://numverify.com).

## Prerequisites

A Numverify API access key (free tier available). Set it in your environment:

```
NUMVERIFY_ACCESS_KEY=your_api_key_here
```

## Installation

Install the numverify extra:

```bash
pip install pymcpx[numverify]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `numverify_validate` | `NumverifyValidateTool` | Validate a phone number and get carrier, location, line type | `number` (required), `country_code` |
| `numverify_countries` | `NumverifyCountriesTool` | List all 232 supported countries with dialing codes | *(none)* |

## Usage

### Individual Tools

```python
from pymcpx.numverify import NumverifyValidateTool

tool = NumverifyValidateTool()
result = tool.invoke({"number": "+14158586273"})
print(result)
```

### Toolkit

```python
from pymcpx.numverify import NumverifyToolkit

toolkit = NumverifyToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
from pymcpx.numverify import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
