"""
HTTP client for the Fixer API.
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://data.fixer.io/api"


def _get_access_key() -> str:
    """Retrieve the Fixer API access key from the environment."""
    key = os.environ.get("FIXER_ACCESS_KEY")
    if not key:
        raise ValueError(
            "FIXER_ACCESS_KEY environment variable is not set. "
            "Please set it to your Fixer API access key."
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
    """Make a GET request to the Fixer API and return formatted output."""
    url = f"{BASE_URL}/{endpoint}"
    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Fixer API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_symbols() -> str:
    """List all supported currency symbols."""
    access_key = _get_access_key()
    params = _build_params(access_key)
    return _call_api("symbols", params)


def get_latest_rates(
    base: str = "EUR",
    symbols: str | None = None,
) -> str:
    """Retrieve latest exchange rates."""
    access_key = _get_access_key()
    params = _build_params(access_key, base=base, symbols=symbols)
    return _call_api("latest", params)


def get_historical_rates(
    date: str,
    base: str = "EUR",
    symbols: str | None = None,
) -> str:
    """Retrieve historical exchange rates for a specific date."""
    access_key = _get_access_key()
    params = _build_params(access_key, base=base, symbols=symbols)
    return _call_api(date, params)


def convert_currency(
    from_: str,
    to: str,
    amount: float,
    date: str | None = None,
) -> str:
    """Convert an amount from one currency to another."""
    access_key = _get_access_key()
    params: dict[str, Any] = {"access_key": access_key, "from": from_, "to": to, "amount": amount}
    if date is not None:
        params["date"] = date
    return _call_api("convert", params)


def get_time_series(
    start_date: str,
    end_date: str,
    base: str = "EUR",
    symbols: str | None = None,
) -> str:
    """Retrieve daily exchange rates for a date range."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        start_date=start_date,
        end_date=end_date,
        base=base,
        symbols=symbols,
    )
    return _call_api("timeseries", params)


def get_fluctuation(
    start_date: str,
    end_date: str,
    base: str = "EUR",
    symbols: str | None = None,
) -> str:
    """Retrieve currency fluctuation data (change and change_pct)."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        start_date=start_date,
        end_date=end_date,
        base=base,
        symbols=symbols,
    )
    return _call_api("fluctuation", params)
