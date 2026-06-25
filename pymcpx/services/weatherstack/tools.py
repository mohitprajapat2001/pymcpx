"""
LangChain BaseTool subclasses for the Weatherstack service.
"""

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.weatherstack.SimulationEngine.models import (
    WeatherstackAutocompleteInput,
    WeatherstackCurrentInput,
    WeatherstackForecastInput,
    WeatherstackHistoricalInput,
    WeatherstackHistoricalMarineInput,
    WeatherstackMarineInput,
)
from pymcpx.services.weatherstack.SimulationEngine.utils import (
    get_autocomplete,
    get_current_weather,
    get_historical_marine_weather,
    get_historical_weather,
    get_marine_weather,
    get_weather_forecast,
)


class WeatherstackCurrentTool(BaseTool):
    """Retrieve current weather conditions."""

    name: str = "weatherstack_current"
    description: str = (
        "Retrieve current weather conditions for a location by city name, "
        "latitude/longitude, or auto-detected IP. Returns temperature, "
        "humidity, wind speed, visibility, and more."
    )
    args_schema: type[BaseModel] = WeatherstackCurrentInput

    def _run(
        self,
        query: str,
        units: str = "m",
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_current_weather(query=query, units=units, language=language)
        except Exception as exc:
            return f"Error: {exc}"


class WeatherstackForecastTool(BaseTool):
    """Retrieve weather forecast data."""

    name: str = "weatherstack_forecast"
    description: str = (
        "Retrieve weather forecast data for a location. Supports up to 14 "
        "days of forecast, with optional hourly breakdown at configurable intervals."
    )
    args_schema: type[BaseModel] = WeatherstackForecastInput

    def _run(
        self,
        query: str,
        forecast_days: int = 7,
        hourly: int = 0,
        interval: int | None = None,
        units: str = "m",
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_weather_forecast(
                query=query,
                forecast_days=forecast_days,
                hourly=hourly,
                interval=interval,
                units=units,
                language=language,
            )
        except Exception as exc:
            return f"Error: {exc}"


class WeatherstackHistoricalTool(BaseTool):
    """Retrieve historical weather data."""

    name: str = "weatherstack_historical"
    description: str = (
        "Retrieve historical weather data for a location. Supports single "
        "date or date range lookups (max 60 day range) with optional hourly data."
    )
    args_schema: type[BaseModel] = WeatherstackHistoricalInput

    def _run(
        self,
        query: str,
        historical_date: str | None = None,
        historical_date_start: str | None = None,
        historical_date_end: str | None = None,
        hourly: int = 0,
        interval: int | None = None,
        units: str = "m",
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_historical_weather(
                query=query,
                historical_date=historical_date,
                historical_date_start=historical_date_start,
                historical_date_end=historical_date_end,
                hourly=hourly,
                interval=interval,
                units=units,
                language=language,
            )
        except Exception as exc:
            return f"Error: {exc}"


class WeatherstackMarineTool(BaseTool):
    """Retrieve marine weather forecast."""

    name: str = "weatherstack_marine"
    description: str = (
        "Retrieve marine weather forecast for a specific latitude/longitude "
        "coordinate. Includes wind, wave, and tide data."
    )
    args_schema: type[BaseModel] = WeatherstackMarineInput

    def _run(
        self,
        latitude: float,
        longitude: float,
        tide: str | None = None,
        hourly: int = 0,
        interval: int | None = None,
        units: str = "m",
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_marine_weather(
                latitude=latitude,
                longitude=longitude,
                tide=tide,
                hourly=hourly,
                interval=interval,
                units=units,
                language=language,
            )
        except Exception as exc:
            return f"Error: {exc}"


class WeatherstackHistoricalMarineTool(BaseTool):
    """Retrieve historical marine weather data."""

    name: str = "weatherstack_historical_marine"
    description: str = (
        "Retrieve historical marine weather data for a specific "
        "latitude/longitude coordinate over a date range."
    )
    args_schema: type[BaseModel] = WeatherstackHistoricalMarineInput

    def _run(
        self,
        latitude: float,
        longitude: float,
        historical_date_start: str,
        historical_date_end: str | None = None,
        tide: str | None = None,
        hourly: int = 0,
        interval: int | None = None,
        units: str = "m",
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_historical_marine_weather(
                latitude=latitude,
                longitude=longitude,
                historical_date_start=historical_date_start,
                historical_date_end=historical_date_end,
                tide=tide,
                hourly=hourly,
                interval=interval,
                units=units,
                language=language,
            )
        except Exception as exc:
            return f"Error: {exc}"


class WeatherstackAutocompleteTool(BaseTool):
    """Search for locations by partial name."""

    name: str = "weatherstack_autocomplete"
    description: str = (
        "Search for locations by partial name. Returns matching city and "
        "region names to help identify the correct location for weather queries."
    )
    args_schema: type[BaseModel] = WeatherstackAutocompleteInput

    def _run(
        self,
        query: str,
        **kwargs: Any,
    ) -> str:
        try:
            return get_autocomplete(query=query)
        except Exception as exc:
            return f"Error: {exc}"


class WeatherstackToolkit:
    """Convenience bundle that exposes all weatherstack tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every weatherstack tool instance."""
        return [
            WeatherstackCurrentTool(),
            WeatherstackForecastTool(),
            WeatherstackHistoricalTool(),
            WeatherstackMarineTool(),
            WeatherstackHistoricalMarineTool(),
            WeatherstackAutocompleteTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    WeatherstackCurrentTool(),
    WeatherstackForecastTool(),
    WeatherstackHistoricalTool(),
    WeatherstackMarineTool(),
    WeatherstackHistoricalMarineTool(),
    WeatherstackAutocompleteTool(),
]
