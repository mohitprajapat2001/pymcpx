"""
HTTP client for the Cat Fact Ninja API.
"""

from __future__ import annotations

import json
from typing import Any

import httpx

BASE_URL = "https://catfact.ninja"


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _build_params(
    limit: int | None = None,
    max_length: int | None = None,
) -> dict[str, Any]:
    """Build query parameters dict, dropping None values."""
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_length is not None:
        params["max_length"] = max_length
    return params


def get_breeds(limit: int | None = None) -> str:
    """Fetch a list of cat breeds from the Cat Fact API."""
    params = _build_params(limit=limit)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/breeds", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Cat Facts API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_random_fact(max_length: int | None = None) -> str:
    """Fetch a random cat fact from the Cat Fact API."""
    params = _build_params(max_length=max_length)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/fact", params=params, timeout=30)

    if response.status_code == 404:
        return '{"error": "Fact not found"}'
    if response.status_code != 200:
        return f"Error: Cat Facts API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_facts(max_length: int | None = None, limit: int | None = None) -> str:
    """Fetch a list of cat facts from the Cat Fact API."""
    params = _build_params(limit=limit, max_length=max_length)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/facts", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Cat Facts API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)
