"""
pymcpx.services.datetime
------------------------
MCP-compatible LangChain tools for date and time calculations.
"""

from pymcpx.services.datetime.models import (
    ConvertTimezoneInput,
    CurrentTimeInput,
    DatetimeToTimestampInput,
    DayOfWeekInput,
    TimestampToDatetimeInput,
)
from pymcpx.services.datetime.SimulationEngine import (
    DatetimeSimulationEngine,
    SimulatedResponse,
    SimulationCall,
    deep_merge,
    inputs_match,
)
from pymcpx.services.datetime.tools import (
    MCP_TOOLS,
    ConvertTimezoneTool,
    DatetimeToolkit,
    DatetimeToTimestampTool,
    GetCurrentTimeTool,
    GetDayOfWeekTool,
    TimestampToDatetimeTool,
)

__all__ = [
    "MCP_TOOLS",
    "ConvertTimezoneInput",
    "ConvertTimezoneTool",
    # Input schemas
    "CurrentTimeInput",
    # Simulation engine
    "DatetimeSimulationEngine",
    "DatetimeToTimestampInput",
    "DatetimeToTimestampTool",
    # Toolkit
    "DatetimeToolkit",
    "DayOfWeekInput",
    # Tools
    "GetCurrentTimeTool",
    "GetDayOfWeekTool",
    "SimulatedResponse",
    "SimulationCall",
    "TimestampToDatetimeInput",
    "TimestampToDatetimeTool",
    "deep_merge",
    "inputs_match",
]
