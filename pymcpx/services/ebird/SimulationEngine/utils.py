"""
HTTP client for the eBird API.
"""

from __future__ import annotations

import difflib
import json
import os
from typing import Any

import httpx

BASE_URL = "https://api.ebird.org/v2"


def _get_api_token() -> str:
    """Retrieve the eBird API token from the environment."""
    token = os.environ.get("X_EBIRD_API_TOKEN")
    if not token:
        raise ValueError(
            "X_EBIRD_API_TOKEN environment variable is not set. "
            "Please set it to your eBird API token."
        )
    return token


def _headers() -> dict[str, str]:
    """Build request headers with the API token."""
    return {"X-eBirdApiToken": _get_api_token()}


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _fetch_json(url: str) -> str:
    """Fetch a URL with auth headers and return formatted JSON."""
    with httpx.Client() as client:
        response = client.get(url, headers=_headers(), timeout=30)

    if response.status_code != 200:
        return f"Error: eBird API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def _build_obs_params(
    back: int | None = None,
    max_results: int | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    spp_locale: str | None = None,
) -> dict[str, Any]:
    """Build query params for observation endpoints, dropping None."""
    params: dict[str, Any] = {}
    if back is not None:
        params["back"] = back
    if max_results is not None:
        params["maxResults"] = max_results
    if hotspot is not None:
        params["hotspot"] = "true" if hotspot else "false"
    if include_provisional is not None:
        params["includeProvisional"] = "true" if include_provisional else "false"
    if spp_locale is not None:
        params["sppLocale"] = spp_locale
    return params


def fuzzy_match_names(
    search: str, names: list[dict[str, str]], limit: int = 50
) -> list[dict[str, str]]:
    """Fuzzy-match a search term against a list of name dicts.

    Each dict should have at least a ``comName`` and ``sciName`` key.
    """
    search_lower = search.lower()
    matches = []
    for entry in names:
        com = (entry.get("comName") or "").lower()
        sci = (entry.get("sciName") or "").lower()
        if search_lower in com or search_lower in sci:
            matches.append(entry)
    if matches:
        return matches[:limit]

    flat_names = [f"{e.get('comName', '')} / {e.get('sciName', '')}" for e in names]
    close = difflib.get_close_matches(search, flat_names, n=limit, cutoff=0.3)
    matched_entries = []
    for n in names:
        label = f"{n.get('comName', '')} / {n.get('sciName', '')}"
        if label in close:
            matched_entries.append(n)
    return matched_entries[:limit]


def _fuzzy_search_list(items: list[str], search: str | None, limit: int) -> list[str]:
    """Fuzzy-search a flat list of strings."""
    if not search:
        return items[:limit]

    search_lower = search.lower()
    exact = [i for i in items if search_lower in i.lower()]
    if exact:
        return exact[:limit]

    close = difflib.get_close_matches(search, items, n=limit, cutoff=0.3)
    return close[:limit] if close else items[:limit]


def get_recent_observations(
    region_code: str,
    back: int | None = None,
    hotspot: bool | None = None,
    include_provisional: bool | None = None,
    max_results: int | None = 50,
    spp_locale: str | None = None,
) -> str:
    """Get recent bird observations in a region."""
    params = _build_obs_params(back, max_results, hotspot, include_provisional, spp_locale)
    query = "&".join(f"{k}={v}" for k, v in params.items()) if params else ""
    url = f"{BASE_URL}/data/obs/{region_code}/recent"
    if query:
        url = f"{url}?{query}"
    return _fetch_json(url)


def get_recent_species_observations(
    region_code: str,
    species_code: str,
    back: int | None = None,
    max_results: int | None = 50,
) -> str:
    """Get recent observations of a specific species in a region."""
    params = _build_obs_params(back, max_results)
    query = "&".join(f"{k}={v}" for k, v in params.items()) if params else ""
    url = f"{BASE_URL}/data/obs/{region_code}/recent/{species_code}"
    if query:
        url = f"{url}?{query}"
    return _fetch_json(url)


def get_nearby_observations(
    species_code: str,
    lat: float,
    lng: float,
    max_results: int | None = 50,
) -> str:
    """Get nearest observations of a species within 50km."""
    params: dict[str, Any] = {"lat": lat, "lng": lng}
    if max_results is not None:
        params["maxResults"] = max_results
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{BASE_URL}/data/obs/geo/recent/{species_code}?{query}"
    return _fetch_json(url)


def get_hotspots(
    region_code: str,
    back: int | None = None,
    max_results: int | None = 50,
) -> str:
    """Get birding hotspots in a region."""
    params: dict[str, Any] = {}
    if back is not None:
        params["back"] = back
    if max_results is not None:
        params["maxResults"] = max_results
    query = "&".join(f"{k}={v}" for k, v in params.items()) if params else ""
    url = f"{BASE_URL}/ref/hotspot/{region_code}"
    if query:
        url = f"{url}?{query}"
    return _fetch_json(url)


def get_taxonomy(
    cat: str | None = None,
    search: str | None = None,
    limit: int = 50,
) -> str:
    """Get eBird taxonomy / species list with optional fuzzy search."""
    params = ""
    if cat:
        params = f"?cat={cat}"
    raw_json = _fetch_json(f"{BASE_URL}/ref/taxonomy/ebird{params}")

    if not search:
        try:
            data = json.loads(raw_json)
            if isinstance(data, list):
                return json.dumps(data[:limit], indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            pass
        return raw_json

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError:
        return raw_json

    if not isinstance(data, list):
        return raw_json

    matched = fuzzy_match_names(search, data, limit)
    if not matched:
        note = f"No close matches for '{search}'. Showing first {limit} species instead."
        return json.dumps({"note": note, "species": data[:limit]}, indent=2, ensure_ascii=False)
    return json.dumps(matched, indent=2, ensure_ascii=False)


def get_species_list(
    region_code: str,
    search: str | None = None,
    limit: int = 50,
) -> str:
    """Get species list for a region with optional fuzzy search."""
    raw_json = _fetch_json(f"{BASE_URL}/product/spplist/{region_code}")

    if not search:
        try:
            data = json.loads(raw_json)
            if isinstance(data, list):
                return json.dumps(data[:limit], indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            pass
        return raw_json

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError:
        return raw_json

    if not isinstance(data, list):
        return raw_json

    matched = _fuzzy_search_list(data, search, limit)
    if not matched:
        matched = data[:limit]
        note = f"No close matches for '{search}'. Showing first {limit} species instead."
        return json.dumps({"note": note, "species": matched}, indent=2, ensure_ascii=False)
    return json.dumps(matched, indent=2, ensure_ascii=False)
