"""
HTTP client for the Numverify API.
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://apilayer.net/api"


def _get_access_key() -> str:
    """Retrieve the Numverify API access key from the environment."""
    key = os.environ.get("NUMVERIFY_ACCESS_KEY")
    if not key:
        raise ValueError(
            "NUMVERIFY_ACCESS_KEY environment variable is not set. "
            "Please set it to your Numverify API access key."
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
    """Make a GET request to the Numverify API and return formatted output."""
    url = f"{BASE_URL}/{endpoint}"
    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Numverify API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def validate_phone_number(number: str, country_code: str | None = None) -> str:
    """Validate a phone number and return its details."""
    access_key = _get_access_key()
    params = _build_params(access_key, number=number, country_code=country_code)
    return _call_api("validate", params)


def get_supported_countries() -> str:
    """Retrieve list of supported countries with dialing codes."""
    access_key = _get_access_key()
    params = _build_params(access_key)
    return _call_api("countries", params)
