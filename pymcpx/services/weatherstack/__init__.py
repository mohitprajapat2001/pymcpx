"""
pymcpx.services.weatherstack - MCP-compatible LangChain tools for Weatherstack.
"""

from pymcpx.services.weatherstack.SimulationEngine import (
    WeatherstackAutocompleteInput,
    WeatherstackCurrentInput,
    WeatherstackForecastInput,
    WeatherstackHistoricalInput,
    WeatherstackHistoricalMarineInput,
    WeatherstackMarineInput,
    WeatherstackSimulationEngine,
    get_autocomplete,
    get_current_weather,
    get_historical_marine_weather,
    get_historical_weather,
    get_marine_weather,
    get_weather_forecast,
)
from pymcpx.services.weatherstack.tools import (
    MCP_TOOLS,
    WeatherstackAutocompleteTool,
    WeatherstackCurrentTool,
    WeatherstackForecastTool,
    WeatherstackHistoricalMarineTool,
    WeatherstackHistoricalTool,
    WeatherstackMarineTool,
    WeatherstackToolkit,
)

__all__ = [
    "MCP_TOOLS",
    "WeatherstackAutocompleteInput",
    "WeatherstackAutocompleteTool",
    "WeatherstackCurrentInput",
    "WeatherstackCurrentTool",
    "WeatherstackForecastInput",
    "WeatherstackForecastTool",
    "WeatherstackHistoricalInput",
    "WeatherstackHistoricalMarineInput",
    "WeatherstackHistoricalMarineTool",
    "WeatherstackHistoricalTool",
    "WeatherstackMarineInput",
    "WeatherstackMarineTool",
    "WeatherstackSimulationEngine",
    "WeatherstackToolkit",
    "get_autocomplete",
    "get_current_weather",
    "get_historical_marine_weather",
    "get_historical_weather",
    "get_marine_weather",
    "get_weather_forecast",
]
