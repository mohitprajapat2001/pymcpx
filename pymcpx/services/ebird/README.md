# Ebird Service

MCP-compatible LangChain tools for bird observations via the [eBird API](https://ebird.org/api/).

## Prerequisites

An eBird API token. Get one at [ebird.org/api/request](https://ebird.org/api/request/).

Set it in your environment:

```
X_EBIRD_API_TOKEN=your_token_here
```

## Installation

Install the ebird extra:

```bash
pip install pymcpx[ebird]
```

## Tools

| Tool Name | Class | Description | Key Parameters |
|-----------|-------|-------------|----------------|
| `get_recent_observations` | `GetRecentObservationsTool` | Recent bird observations in a region | `region_code` (required), `back`, `hotspot`, `include_provisional`, `max_results`, `spp_locale` |
| `get_recent_species_observations` | `GetRecentSpeciesObservationsTool` | Recent observations of a specific species | `region_code`, `species_code`, `back`, `max_results` |
| `get_nearby_observations` | `GetNearbyObservationsTool` | Nearest observations (50km radius) | `species_code`, `lat`, `lng`, `max_results` |
| `get_hotspots` | `GetHotspotsTool` | Birding hotspots in a region | `region_code`, `back`, `max_results` |
| `get_taxonomy` | `GetTaxonomyTool` | eBird taxonomy with fuzzy search | `cat`, `search`, `limit` |
| `get_species_list` | `GetSpeciesListTool` | Species list for a region | `region_code`, `search`, `limit` |

All list endpoints default to 50 results (max 200) and support fuzzy search where applicable.

## Usage

```python
    from pymcpx.ebird import GetRecentObservationsTool

tool = GetRecentObservationsTool()
result = tool.invoke({"region_code": "US-NY-103", "max_results": 10})
print(result)
```

### MCP Integration

```python
    from pymcpx.ebird import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
