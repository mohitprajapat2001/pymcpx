# Datetime Service

MCP-compatible LangChain tools for date and time calculations.

## Installation

Install the datetime extra:

```bash
pip install pymcpx[datetime]
```

## Tools

| Tool Name | Class | Description | Input Schema |
|-----------|-------|-------------|--------------|
| `get_current_time` | `GetCurrentTimeTool` | Get current date/time in specific timezone | `timezone: str, format: str` |
| `convert_timezone` | `ConvertTimezoneTool` | Convert datetime string from one timezone to another | `datetime_str: str, to_tz: str, from_tz: str` |
| `get_day_of_week` | `GetDayOfWeekTool` | Get the day of the week for a given date | `date_str: str` |
| `timestamp_to_datetime` | `TimestampToDatetimeTool` | Convert Unix timestamp to a datetime string | `timestamp: float, timezone: str, format: str` |
| `datetime_to_timestamp` | `DatetimeToTimestampTool` | Convert a datetime string to a Unix timestamp | `datetime_str: str, timezone: str` |

## Usage

### Individual Tools

```python
    from pymcpx.datetime import GetCurrentTimeTool

tool = GetCurrentTimeTool()
result = tool.invoke({"timezone": "America/New_York"})
print(result)  # e.g., "2026-06-24T12:00:00-04:00"
```

### Toolkit

You can retrieve all datetime tools at once using the `DatetimeToolkit`:

```python
    from pymcpx.datetime import DatetimeToolkit

toolkit = DatetimeToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
    from pymcpx.datetime import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```

## Simulation (Offline Mode)

You can run these tools offline or with deterministic pinned responses for testing:

```python
    from pymcpx.datetime import DatetimeSimulationEngine

engine = DatetimeSimulationEngine()

# Register a fixture to return a pinned time
engine.register(
    tool_name="get_current_time",
    input_match={"timezone": "UTC"},
    output="2026-06-24T12:00:00Z",
)

result = engine.run("get_current_time", {"timezone": "UTC"})
print(result)  # "2026-06-24T12:00:00Z"
```
