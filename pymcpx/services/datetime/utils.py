"""
Utility helpers for the datetime service.
"""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def get_zone_info(tz_name: str) -> ZoneInfo:
    """Get ZoneInfo object by name, raising a clear ValueError for invalid timezones."""
    try:
        return ZoneInfo(tz_name)
    except ZoneInfoNotFoundError as exc:
        raise ValueError(
            f"Invalid timezone '{tz_name}'. Must be a valid IANA timezone name "
            "(e.g., 'America/New_York', 'UTC')."
        ) from exc


def parse_datetime_str(datetime_str: str, default_tz: str = "UTC") -> datetime:
    """Parse a datetime string into a timezone-aware datetime object.

    Handles ISO-8601 format natively (including offsets), and falls back
    to common formats with the specified default timezone if naive.
    """
    dt_str = datetime_str.strip()

    # Try ISO format parsing first
    try:
        dt = datetime.fromisoformat(dt_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=get_zone_info(default_tz))
        return dt
    except ValueError:
        pass

    # Try common formats
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
        "%d-%m-%Y %H:%M:%S",
        "%d-%m-%Y",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(dt_str, fmt)
            return dt.replace(tzinfo=get_zone_info(default_tz))
        except ValueError:
            continue

    raise ValueError(
        f"Unable to parse datetime string '{datetime_str}'. Supported formats include "
        "ISO-8601 (e.g., 'YYYY-MM-DDTHH:MM:SS+HH:MM') and 'YYYY-MM-DD HH:MM:SS'."
    )
