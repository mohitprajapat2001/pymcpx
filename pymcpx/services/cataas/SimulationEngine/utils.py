"""
HTTP client for the Cat as a Service (CATAAS) API.
"""

from __future__ import annotations

import difflib
import json
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from pydantic import BaseModel

BASE_URL = "https://cataas.com"

_PATH_PARAMS = {"id", "tag", "text"}


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _build_cat_url(path: str, params: BaseModel | None = None) -> str:
    """Build a CATAAS URL from a path and a Pydantic model with flat params."""
    if params is None:
        return f"{BASE_URL}{path}"

    dump = params.model_dump(by_alias=True, exclude_none=True)
    query_parts = []
    for k, v in dump.items():
        if k not in _PATH_PARAMS:
            if isinstance(v, bool):
                query_parts.append(f"{k}={str(v).lower()}")
            else:
                query_parts.append(f"{k}={v}")

    query = "&".join(query_parts)
    return f"{BASE_URL}{path}?{query}" if query else f"{BASE_URL}{path}"


def _fetch_json(url: str) -> str:
    """Fetch a URL and return formatted JSON response."""
    with httpx.Client() as client:
        response = client.get(url, timeout=30)

    if response.status_code != 200:
        return f"Error: CATAAS API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def _get_cat_response(path: str, params: BaseModel | None = None) -> str:
    """Get a cat image URL or JSON metadata from a flat params model."""
    wants_json = params is not None and getattr(params, "return_json", None)

    url = _build_cat_url(path, params)
    if wants_json:
        return _fetch_json(url)
    return url


def fuzzy_match_tags(search: str, tags: list[str], limit: int = 20) -> list[str]:
    """Fuzzy-match a search term against a list of tags using difflib."""
    search_lower = search.lower()
    exact_matches = [t for t in tags if search_lower in t.lower()]
    if exact_matches:
        return exact_matches[:limit]

    close_matches = difflib.get_close_matches(search, tags, n=limit, cutoff=0.3)
    return close_matches


def fetch_all_tags() -> list[str]:
    """Fetch all available tags from the CATAAS API."""
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/api/tags", timeout=30)

    if response.status_code != 200:
        return []

    try:
        return response.json()
    except (json.JSONDecodeError, ValueError):
        return []


def list_tags(search: str | None = None, limit: int = 20) -> str:
    """List all tags, optionally fuzzy-filtered by search term."""
    all_tags = fetch_all_tags()
    if not all_tags:
        return "Error: Could not fetch tags from CATAAS API."

    if search:
        matched = fuzzy_match_tags(search, all_tags, limit)
        if not matched:
            matched = all_tags[:limit]
            note = f"No close matches for '{search}'. Showing first {limit} available tags instead."
            return json.dumps({"note": note, "tags": matched}, indent=2, ensure_ascii=False)
        return json.dumps(matched, indent=2, ensure_ascii=False)
    else:
        return json.dumps(all_tags[:limit], indent=2, ensure_ascii=False)


def list_cats(
    limit: int = 10,
    skip: int = 0,
    tags: str | None = None,
    search: str | None = None,
) -> str:
    """List cats, optionally filtered by tags or fuzzy search."""
    if search and not tags:
        all_tags = fetch_all_tags()
        if all_tags:
            matched = fuzzy_match_tags(search, all_tags, limit=5)
            if matched:
                tags = ",".join(matched)

    params: dict[str, Any] = {"limit": limit, "skip": skip}
    if tags:
        params["tags"] = tags

    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{BASE_URL}/api/cats?{query}"
    return _fetch_json(url)


def count_cats() -> str:
    """Count all cats."""
    return _fetch_json(f"{BASE_URL}/api/count")
