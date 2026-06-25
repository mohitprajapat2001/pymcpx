# Fixer Service

MCP-compatible LangChain tools for foreign exchange rates via the [Fixer API](https://fixer.io).

## Prerequisites

A Fixer API access key (free tier available). Set it in your environment:

```
FIXER_ACCESS_KEY=your_api_key_here
```

## Installation

Install the fixer extra:

```bash
pip install pymcpx[fixer]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `fixer_symbols` | `FixerSymbolsTool` | List all 170+ supported currencies | *(none)* |
| `fixer_latest_rates` | `FixerLatestRatesTool` | Latest real-time exchange rates | `base`, `symbols` |
| `fixer_historical_rates` | `FixerHistoricalRatesTool` | Historical rates for any date (back to 1999) | `date` (required), `base`, `symbols` |
| `fixer_convert` | `FixerConvertTool` | Convert amount from one currency to another | `from` (required), `to` (required), `amount` (required), `date` |
| `fixer_timeseries` | `FixerTimeSeriesTool` | Daily rates between two dates (max 365 days) | `start_date` (required), `end_date` (required), `base`, `symbols` |
| `fixer_fluctuation` | `FixerFluctuationTool` | Currency fluctuation analysis | `start_date` (required), `end_date` (required), `base`, `symbols` |

## Usage

### Individual Tools

```python
from pymcpx.fixer import FixerLatestRatesTool

tool = FixerLatestRatesTool()
result = tool.invoke({"base": "USD", "symbols": "EUR,GBP,JPY"})
print(result)
```

### Toolkit

```python
from pymcpx.fixer import FixerToolkit

toolkit = FixerToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
from pymcpx.fixer import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
