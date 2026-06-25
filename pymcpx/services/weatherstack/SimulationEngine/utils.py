"""
HTTP client for the Weatherstack API.
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://api.weatherstack.com"


def _get_access_key() -> str:
    """Retrieve the Weatherstack API access key from the environment."""
    key = os.environ.get("WEATHERSTACK_ACCESS_KEY")
    if not key:
        raise ValueError(
            "WEATHERSTACK_ACCESS_KEY environment variable is not set. "
            "Please set it to your Weatherstack API access key."
        )
    return key


def _build_params(access_key: str, **kwargs: Any) -> dict[str, Any]:
    """Build query parameters dict, dropping None values."""
    params: dict[str, Any] = {"access_key": access_key}
    for k, v in kwargs.items():
        if v is not None:
            params[k] = v
    return params


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _call_api(endpoint: str, params: dict[str, Any]) -> str:
    """Make a GET request to the Weatherstack API and return formatted output."""
    url = f"{BASE_URL}/{endpoint}"
    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Weatherstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_current_weather(
    query: str,
    units: str = "m",
    language: str | None = None,
) -> str:
    """Retrieve current weather conditions for a location."""
    access_key = _get_access_key()
    params = _build_params(access_key, query=query, units=units, language=language)
    return _call_api("current", params)


def get_weather_forecast(
    query: str,
    forecast_days: int = 7,
    hourly: int = 0,
    interval: int | None = None,
    units: str = "m",
    language: str | None = None,
) -> str:
    """Retrieve weather forecast for a location."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        query=query,
        forecast_days=forecast_days,
        hourly=hourly,
        interval=interval,
        units=units,
        language=language,
    )
    return _call_api("forecast", params)


def get_historical_weather(
    query: str,
    historical_date: str | None = None,
    historical_date_start: str | None = None,
    historical_date_end: str | None = None,
    hourly: int = 0,
    interval: int | None = None,
    units: str = "m",
    language: str | None = None,
) -> str:
    """Retrieve historical weather data for a location."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        query=query,
        historical_date=historical_date,
        historical_date_start=historical_date_start,
        historical_date_end=historical_date_end,
        hourly=hourly,
        interval=interval,
        units=units,
        language=language,
    )
    return _call_api("historical", params)


def get_marine_weather(
    latitude: float,
    longitude: float,
    tide: str | None = None,
    hourly: int = 0,
    interval: int | None = None,
    units: str = "m",
    language: str | None = None,
) -> str:
    """Retrieve marine weather forecast."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        query=f"{latitude},{longitude}",
        tide=tide,
        hourly=hourly,
        interval=interval,
        units=units,
        language=language,
    )
    return _call_api("marine", params)


def get_historical_marine_weather(
    latitude: float,
    longitude: float,
    historical_date_start: str,
    historical_date_end: str | None = None,
    tide: str | None = None,
    hourly: int = 0,
    interval: int | None = None,
    units: str = "m",
    language: str | None = None,
) -> str:
    """Retrieve historical marine weather data."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        query=f"{latitude},{longitude}",
        historical_date_start=historical_date_start,
        historical_date_end=historical_date_end,
        tide=tide,
        hourly=hourly,
        interval=interval,
        units=units,
        language=language,
    )
    return _call_api("past-marine", params)


def get_autocomplete(query: str) -> str:
    """Search for locations by partial name."""
    access_key = _get_access_key()
    params = _build_params(access_key, query=query)
    return _call_api("autocomplete", params)
