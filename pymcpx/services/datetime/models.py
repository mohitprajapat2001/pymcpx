"""
Pydantic models for the datetime service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class CurrentTimeInput(BaseModel):
    """Input schema for get_current_time tool."""

    timezone: str = Field(
        default="UTC",
        description="The target timezone (e.g., 'UTC', 'America/New_York', 'Asia/Kolkata').",
    )
    format: str = Field(
        default="%Y-%m-%dT%H:%M:%S%z",
        description="strftime-style format string for the output.",
    )


class ConvertTimezoneInput(BaseModel):
    """Input schema for convert_timezone tool."""

    datetime_str: str = Field(
        description="The datetime string to convert (e.g., '2026-06-24T12:00:00' or with offset)."
    )
    from_tz: str = Field(
        default="UTC",
        description="The timezone of the input datetime_str if not specified in the string.",
    )
    to_tz: str = Field(
        description="The target timezone to convert to (e.g., 'Europe/London', 'Asia/Tokyo')."
    )


class DayOfWeekInput(BaseModel):
    """Input schema for get_day_of_week tool."""

    date_str: str = Field(
        description="Date string to query (e.g., '2026-06-24' or ISO-8601 format)."
    )


class TimestampToDatetimeInput(BaseModel):
    """Input schema for timestamp_to_datetime tool."""

    timestamp: float = Field(description="Unix timestamp (seconds since epoch).")
    timezone: str = Field(
        default="UTC",
        description="Target timezone for the output datetime (e.g., 'UTC', 'America/Chicago').",
    )
    format: str = Field(
        default="%Y-%m-%dT%H:%M:%S%z",
        description="strftime-style format string for the output.",
    )


class DatetimeToTimestampInput(BaseModel):
    """Input schema for datetime_to_timestamp tool."""

    datetime_str: str = Field(
        description="The datetime string to convert to timestamp (e.g., '2026-06-24T12:00:00')."
    )
    timezone: str = Field(
        default="UTC",
        description="The timezone of the input datetime string if not specified in the string.",
    )
