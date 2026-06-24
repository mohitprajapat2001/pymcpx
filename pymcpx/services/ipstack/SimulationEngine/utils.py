"""
HTTP client for the IPstack API.
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://api.ipstack.com"


def _get_access_key() -> str:
    """Retrieve the IPstack API access key from the environment."""
    key = os.environ.get("IPSTACK_ACCESS_KEY")
    if not key:
        raise ValueError(
            "IPSTACK_ACCESS_KEY environment variable is not set. "
            "Please set it to your IPstack API access key."
        )
    return key


def _build_params(
    access_key: str,
    fields: str | None = None,
    hostname: int | None = None,
    security: int | None = None,
    language: str | None = None,
    output: str | None = None,
    callback: str | None = None,
) -> dict[str, Any]:
    """Build query parameters dict, dropping None values."""
    params: dict[str, Any] = {"access_key": access_key}
    if fields is not None:
        params["fields"] = fields
    if hostname is not None:
        params["hostname"] = hostname
    if security is not None:
        params["security"] = security
    if language is not None:
        params["language"] = language
    if output is not None:
        params["output"] = output
    if callback is not None:
        params["callback"] = callback
    return params


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def lookup_ip(
    ip_address: str,
    fields: str | None = None,
    hostname: int | None = None,
    security: int | None = None,
    language: str | None = None,
    output: str | None = None,
    callback: str | None = None,
) -> str:
    """Perform a Standard Lookup for a single IP address."""
    access_key = _get_access_key()
    params = _build_params(access_key, fields, hostname, security, language, output, callback)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/{ip_address}", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: IPstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def lookup_requester_ip(
    fields: str | None = None,
    hostname: int | None = None,
    security: int | None = None,
    language: str | None = None,
    output: str | None = None,
    callback: str | None = None,
) -> str:
    """Detect and return geolocation for the requester's own IP."""
    access_key = _get_access_key()
    params = _build_params(access_key, fields, hostname, security, language, output, callback)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/check", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: IPstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def bulk_lookup(
    ip_addresses: str,
    fields: str | None = None,
    hostname: int | None = None,
    security: int | None = None,
    language: str | None = None,
    output: str | None = None,
    callback: str | None = None,
) -> str:
    """Bulk lookup up to 50 comma-separated IP addresses."""
    access_key = _get_access_key()
    params = _build_params(access_key, fields, hostname, security, language, output, callback)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/{ip_addresses}", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: IPstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)
