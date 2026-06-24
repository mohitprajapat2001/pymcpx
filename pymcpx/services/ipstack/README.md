# IPstack Service

MCP-compatible LangChain tools for IP geolocation via the [IPstack API](https://ipstack.com).

## Prerequisites

An IPstack API access key. Set it in your environment:

```
IPSTACK_ACCESS_KEY=your_api_key_here
```

## Installation

Install the ipstack extra:

```bash
pip install pymcpx[ipstack]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `lookup_ip` | `LookupIPTool` | Geolocation for a single IPv4 or IPv6 address | `ip_address` (required), `security`, `hostname`, `fields`, `language`, `output`, `callback` |
| `lookup_requester_ip` | `LookupRequesterIPTool` | Detect geolocation for the requester's own IP | `security`, `hostname`, `fields`, `language`, `output`, `callback` |
| `bulk_lookup_ip` | `BulkLookupIPTool` | Look up multiple IPs at once (up to 50) | `ip_addresses` (required, comma-separated), `security`, `hostname`, `fields`, `language`, `output`, `callback` |

## Usage

### Individual Tools

```python
    from pymcpx.ipstack import LookupIPTool

tool = LookupIPTool()
result = tool.invoke({"ip_address": "134.201.250.155", "security": 1})
print(result)
```

### Toolkit

```python
    from pymcpx.ipstack import IpstackToolkit

toolkit = IpstackToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
    from pymcpx.ipstack import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
