"""
LangChain BaseTool implementations for the datetime service.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.datetime.models import (
    ConvertTimezoneInput,
    CurrentTimeInput,
    DatetimeToTimestampInput,
    DayOfWeekInput,
    TimestampToDatetimeInput,
)
from pymcpx.services.datetime.utils import get_zone_info, parse_datetime_str


class GetCurrentTimeTool(BaseTool):
    """Get the current date and time in a specific timezone."""

    name: str = "get_current_time"
    description: str = (
        "Get the current date and time in a specific timezone. "
        "Allows customizing the strftime format."
    )
    args_schema: type[BaseModel] = CurrentTimeInput

    def _run(
        self, timezone: str = "UTC", format: str = "%Y-%m-%dT%H:%M:%S%z", **kwargs: Any
    ) -> str:
        try:
            tz = get_zone_info(timezone)
            now = datetime.now(tz)
            return now.strftime(format)
        except Exception as exc:
            return f"Error: {exc}"


class ConvertTimezoneTool(BaseTool):
    """Convert a datetime string from one timezone to another."""

    name: str = "convert_timezone"
    description: str = (
        "Convert a datetime string from one timezone to another. "
        "Returns the converted datetime string."
    )
    args_schema: type[BaseModel] = ConvertTimezoneInput

    def _run(self, datetime_str: str, to_tz: str, from_tz: str = "UTC", **kwargs: Any) -> str:
        try:
            target_tz = get_zone_info(to_tz)
            dt = parse_datetime_str(datetime_str, default_tz=from_tz)
            converted = dt.astimezone(target_tz)
            return converted.isoformat()
        except Exception as exc:
            return f"Error: {exc}"


class GetDayOfWeekTool(BaseTool):
    """Get the day of the week for a given date."""

    name: str = "get_day_of_week"
    description: str = "Get the day of the week (e.g. 'Monday', 'Sunday') for a given date string."
    args_schema: type[BaseModel] = DayOfWeekInput

    def _run(self, date_str: str, **kwargs: Any) -> str:
        try:
            dt = parse_datetime_str(date_str)
            return dt.strftime("%A")
        except Exception as exc:
            return f"Error: {exc}"


class TimestampToDatetimeTool(BaseTool):
    """Convert a Unix timestamp to a datetime string."""

    name: str = "timestamp_to_datetime"
    description: str = "Convert a Unix timestamp (seconds since epoch) to a datetime string."
    args_schema: type[BaseModel] = TimestampToDatetimeInput

    def _run(
        self,
        timestamp: float,
        timezone: str = "UTC",
        format: str = "%Y-%m-%dT%H:%M:%S%z",
        **kwargs: Any,
    ) -> str:
        try:
            tz = get_zone_info(timezone)
            dt = datetime.fromtimestamp(timestamp, tz)
            return dt.strftime(format)
        except Exception as exc:
            return f"Error: {exc}"


class DatetimeToTimestampTool(BaseTool):
    """Convert a datetime string to a Unix timestamp."""

    name: str = "datetime_to_timestamp"
    description: str = (
        "Convert a datetime string in a given timezone to a Unix timestamp (seconds since epoch)."
    )
    args_schema: type[BaseModel] = DatetimeToTimestampInput

    def _run(self, datetime_str: str, timezone: str = "UTC", **kwargs: Any) -> str:
        try:
            dt = parse_datetime_str(datetime_str, default_tz=timezone)
            return str(dt.timestamp())
        except Exception as exc:
            return f"Error: {exc}"


class DatetimeToolkit:
    """Convenience bundle that exposes all datetime tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every datetime tool instance."""
        return [
            GetCurrentTimeTool(),
            ConvertTimezoneTool(),
            GetDayOfWeekTool(),
            TimestampToDatetimeTool(),
            DatetimeToTimestampTool(),
        ]


# ---------------------------------------------------------------------------
# MCP registration list
# ---------------------------------------------------------------------------

MCP_TOOLS: list[BaseTool] = [
    GetCurrentTimeTool(),
    ConvertTimezoneTool(),
    GetDayOfWeekTool(),
    TimestampToDatetimeTool(),
    DatetimeToTimestampTool(),
]
