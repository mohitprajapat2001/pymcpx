# Weatherstack Service

MCP-compatible LangChain tools for weather data via the [Weatherstack API](https://weatherstack.com).

## Prerequisites

A Weatherstack API access key (free tier available). Set it in your environment:

```
WEATHERSTACK_ACCESS_KEY=your_api_key_here
```

## Installation

Install the weatherstack extra:

```bash
pip install pymcpx[weatherstack]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `weatherstack_current` | `WeatherstackCurrentTool` | Current weather conditions for a location | `query` (required), `units`, `language` |
| `weatherstack_forecast` | `WeatherstackForecastTool` | Weather forecast up to 14 days | `query` (required), `forecast_days`, `hourly`, `interval`, `units`, `language` |
| `weatherstack_historical` | `WeatherstackHistoricalTool` | Historical weather for a date or date range | `query` (required), `historical_date`, `historical_date_start`, `historical_date_end`, `hourly`, `interval`, `units`, `language` |
| `weatherstack_marine` | `WeatherstackMarineTool` | Marine weather forecast at lat/lon | `latitude` (required), `longitude` (required), `tide`, `hourly`, `interval`, `units`, `language` |
| `weatherstack_historical_marine` | `WeatherstackHistoricalMarineTool` | Historical marine weather for a date range | `latitude` (required), `longitude` (required), `historical_date_start` (required), `historical_date_end`, `tide`, `hourly`, `interval`, `units`, `language` |
| `weatherstack_autocomplete` | `WeatherstackAutocompleteTool` | Search locations by partial name | `query` (required) |

## Usage

### Individual Tools

```python
from pymcpx.weatherstack import WeatherstackCurrentTool

tool = WeatherstackCurrentTool()
result = tool.invoke({"query": "New York", "units": "m"})
print(result)
```

### Toolkit

```python
from pymcpx.weatherstack import WeatherstackToolkit

toolkit = WeatherstackToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
from pymcpx.weatherstack import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
