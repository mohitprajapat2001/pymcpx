# ExchangeRate.host Service

MCP-compatible LangChain tools for the [ExchangeRate.host API](https://exchangerate.host/) — real-time and historical foreign exchange & crypto rates for 168 world currencies.

## Prerequisites

- An ExchangeRate.host API access key (free tier available at [exchangerate.host](https://exchangerate.host/))
- Python 3.11+

## Installation

```bash
pip install pymcpx[exchangeratehost]
```

Set your API key as an environment variable:

```bash
export EXCHANGERATEHOST_ACCESS_KEY="your_api_key_here"
```

## Tools

| Tool Name                           | Class                              | Description                                                      | Input Keys                                                    |
| ----------------------------------- | ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- |
| `exchangeratehost_live`             | `ExchangeratehostLiveTool`         | Real-time exchange rates with optional source/currency filter     | `source`, `currencies`                                        |
| `exchangeratehost_historical`       | `ExchangeratehostHistoricalTool`   | Historical rates for a specific date                             | `date`, `source`, `currencies`                                |
| `exchangeratehost_convert`          | `ExchangeratehostConvertTool`      | Currency conversion with optional historical date                 | `from_`, `to`, `amount`, `date`                               |
| `exchangeratehost_timeframe`        | `ExchangeratehostTimeframeTool`    | Daily rates for a date range (max 365 days)                      | `start_date`, `end_date`, `source`, `currencies`              |
| `exchangeratehost_change`           | `ExchangeratehostChangeTool`       | Currency fluctuation (change & change_pct) between two dates     | `start_date`, `end_date`, `source`, `currencies`              |

## Usage Examples

### Individual Tool

```python
import os
os.environ["EXCHANGERATEHOST_ACCESS_KEY"] = "your_key"

from pymcpx.exchangeratehost import ExchangeratehostLiveTool

tool = ExchangeratehostLiveTool()
result = tool.run({"source": "USD", "currencies": "GBP,EUR"})
print(result)
```

### Currency Conversion

```python
from pymcpx.exchangeratehost import ExchangeratehostConvertTool

tool = ExchangeratehostConvertTool()
result = tool.run({"from_": "USD", "to": "GBP", "amount": 100})
print(result)
```

### Toolkit (all tools)

```python
import os
os.environ["EXCHANGERATEHOST_ACCESS_KEY"] = "your_key"

from pymcpx.exchangeratehost import ExchangeratehostToolkit

toolkit = ExchangeratehostToolkit()
tools = toolkit.get_tools()
result = tools[0].run({"source": "USD"})
print(result)
```

### MCP Integration

```python
from pymcpx.exchangeratehost import MCP_TOOLS

for tool in MCP_TOOLS:
    print(f"{tool.name}: {tool.description}")
```
