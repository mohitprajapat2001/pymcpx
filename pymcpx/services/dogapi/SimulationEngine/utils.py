"""
HTTP client for the Dog CEO API.
"""

from __future__ import annotations

import difflib
import json
from typing import Any

import httpx

BASE_URL = "https://dog.ceo/api"


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _fetch_json(url: str) -> str:
    """Fetch a URL and return formatted JSON response."""
    with httpx.Client() as client:
        response = client.get(url, timeout=30)

    if response.status_code != 200:
        return f"Error: Dog CEO API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def _flatten_breeds(raw: dict[str, Any]) -> list[str]:
    """Flatten the nested breed object into a list of breed names."""
    breeds = []
    for master, subs in raw.items():
        breeds.append(master)
        for sub in subs:
            breeds.append(f"{sub} {master}")
    return sorted(breeds)


def fuzzy_match_breeds(search: str, breeds: list[str], limit: int = 20) -> list[str]:
    """Fuzzy-match a search term against a list of breeds using difflib."""
    search_lower = search.lower()
    exact_matches = [b for b in breeds if search_lower in b.lower()]
    if exact_matches:
        return exact_matches[:limit]

    close_matches = difflib.get_close_matches(search, breeds, n=limit, cutoff=0.3)
    return close_matches


def list_breeds(search: str | None = None, limit: int = 20) -> str:
    """List all dog breeds, optionally fuzzy-filtered by search term."""
    raw_json = _fetch_json(f"{BASE_URL}/breeds/list/all")

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError:
        return raw_json

    message = data.get("message", {}) if isinstance(data, dict) else {}
    all_breeds = _flatten_breeds(message)

    if search:
        matched = fuzzy_match_breeds(search, all_breeds, limit)
        if not matched:
            matched = all_breeds[:limit]
            note = (
                f"No close matches for '{search}'. Showing first {limit} available breeds instead."
            )
            return json.dumps({"note": note, "breeds": matched}, indent=2, ensure_ascii=False)
        return json.dumps(matched, indent=2, ensure_ascii=False)
    else:
        return json.dumps(all_breeds[:limit], indent=2, ensure_ascii=False)


def get_random_dog_image() -> str:
    """Get a random dog image URL."""
    raw_json = _fetch_json(f"{BASE_URL}/breeds/image/random")

    try:
        data = json.loads(raw_json)
        if isinstance(data, dict) and "message" in data:
            return data["message"]
    except json.JSONDecodeError:
        pass

    return raw_json


def get_random_dog_image_by_breed(breed: str) -> str:
    """Get a random dog image URL for a specific breed."""
    raw_json = _fetch_json(f"{BASE_URL}/breed/{breed}/images/random")

    try:
        data = json.loads(raw_json)
        if isinstance(data, dict) and "message" in data:
            return data["message"]
    except json.JSONDecodeError:
        pass

    return raw_json
