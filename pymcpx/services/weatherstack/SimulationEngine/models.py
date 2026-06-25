"""
Pydantic input models for the Weatherstack service tools.
"""

from pydantic import BaseModel, Field


class WeatherstackCurrentInput(BaseModel):
    """Input schema for current weather lookup."""

    query: str = Field(
        description="Location query — city name (e.g., 'New York'), 'latitude,longitude', or 'fetch:ip'."
    )
    units: str = Field(
        default="m",
        description="Unit system: 'm' for Metric (Celsius, cm, m/s), 's' for Scientific (Kelvin, mm, m/s), 'f' for Fahrenheit.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code (e.g., 'en', 'de', 'fr') for localized weather descriptions.",
    )


class WeatherstackForecastInput(BaseModel):
    """Input schema for weather forecast lookup."""

    query: str = Field(
        description="Location query — city name (e.g., 'London'), 'latitude,longitude', or 'fetch:ip'."
    )
    forecast_days: int = Field(
        default=7,
        description="Number of forecast days (1-14). Defaults to 7.",
    )
    hourly: int = Field(
        default=0,
        description="Set to 1 to enable hourly weather data in the forecast.",
    )
    interval: int | None = Field(
        default=None,
        description="Hourly interval in hours (1, 3, 6, 12, or 24). Only applies when hourly=1.",
    )
    units: str = Field(
        default="m",
        description="Unit system: 'm' for Metric, 's' for Scientific, 'f' for Fahrenheit.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized weather descriptions.",
    )


class WeatherstackHistoricalInput(BaseModel):
    """Input schema for historical weather lookup."""

    query: str = Field(
        description="Location query — city name, 'latitude,longitude', or 'fetch:ip'."
    )
    historical_date: str | None = Field(
        default=None,
        description="Single historical date (Format: 'YYYY-MM-DD'). Use this or historical_date_start.",
    )
    historical_date_start: str | None = Field(
        default=None,
        description="Start date for historical date range (Format: 'YYYY-MM-DD'). Max 60 day range.",
    )
    historical_date_end: str | None = Field(
        default=None,
        description="End date for historical date range (Format: 'YYYY-MM-DD').",
    )
    hourly: int = Field(
        default=0,
        description="Set to 1 to include hourly historical data.",
    )
    interval: int | None = Field(
        default=None,
        description="Hourly interval in hours (1, 3, 6, 12, or 24).",
    )
    units: str = Field(
        default="m",
        description="Unit system: 'm' for Metric, 's' for Scientific, 'f' for Fahrenheit.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized weather descriptions.",
    )


class WeatherstackMarineInput(BaseModel):
    """Input schema for marine weather forecast lookup."""

    latitude: float = Field(description="Latitude coordinate (e.g., 40.7128).")
    longitude: float = Field(description="Longitude coordinate (e.g., -74.0060).")
    tide: str | None = Field(
        default=None,
        description="Tide data level: 'tidal' or 'extremes'. Omit for no tide data.",
    )
    hourly: int = Field(
        default=0,
        description="Set to 1 to enable hourly marine weather data.",
    )
    interval: int | None = Field(
        default=None,
        description="Hourly interval in hours (1, 3, 6, 12, or 24).",
    )
    units: str = Field(
        default="m",
        description="Unit system: 'm' for Metric, 's' for Scientific, 'f' for Fahrenheit.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized weather descriptions.",
    )


class WeatherstackHistoricalMarineInput(BaseModel):
    """Input schema for historical marine weather lookup."""

    latitude: float = Field(description="Latitude coordinate (e.g., 40.7128).")
    longitude: float = Field(description="Longitude coordinate (e.g., -74.0060).")
    historical_date_start: str = Field(
        description="Start date for historical marine data (Format: 'YYYY-MM-DD')."
    )
    historical_date_end: str | None = Field(
        default=None,
        description="End date for historical marine data (Format: 'YYYY-MM-DD').",
    )
    tide: str | None = Field(
        default=None,
        description="Tide data level: 'tidal' or 'extremes'. Omit for no tide data.",
    )
    hourly: int = Field(
        default=0,
        description="Set to 1 to enable hourly historical marine data.",
    )
    interval: int | None = Field(
        default=None,
        description="Hourly interval in hours (1, 3, 6, 12, or 24).",
    )
    units: str = Field(
        default="m",
        description="Unit system: 'm' for Metric, 's' for Scientific, 'f' for Fahrenheit.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized weather descriptions.",
    )


class WeatherstackAutocompleteInput(BaseModel):
    """Input schema for location autocomplete lookup."""

    query: str = Field(description="Partial location name to search for (e.g., 'New Yor').")


class _WeatherstackMarinePositionalInput(BaseModel):
    """Shared lat/lon base for marine endpoints (not directly exposed as a tool)."""

    latitude: float = Field(description="Latitude coordinate.")
    longitude: float = Field(description="Longitude coordinate.")
